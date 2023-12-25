"""
===============***===============
Auther : Lee
Date   : 2022-11-24 - 14:11
File   : test_cdq_businessdb.py
===============***===============
"""
import pytest
import requests
import allure
from autotest_03.comms.dbutils import DBUtils
from autotest_03.comms.log_utils import logger
from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.ptrhon_xfj import get_yaml_data, get_ini_data, true_value
import os

"""
pytest的参数化
测试数据和测试代码分离,你写多少条case就会有多少个测试用例场景
"""


@pytest.mark.T2
@allure.epic('第三天的测试')
@allure.feature('登录测试')
class Test_Commodity_Query:
    name = get_ini_data('tb_user', 'username')
    pwd = get_ini_data('tb_user', 'psw')
    tp_id = get_ini_data('tb_user', 'tlb')

    response = requests.post(url='http://127.0.0.1:6666/business/token_login',
                             data={'username': name, 'password': pwd, 'typeId': tp_id})
    res = response.json()
    tk = res['token']
    cases = get_yaml_data(os.path.join(DATA_DIR, 'test_cdq_businessdb.yaml'))
    ids = [case['case_title'] for case in cases]

    @pytest.mark.usefixtures('function')
    @pytest.mark.parametrize("case", cases, ids=ids)
    def test_login(self, case):
        if 'tkk&' in case['case_data'].values():
            case['case_data']['token'] = self.tk
        response = requests.post(url=case['url'], data=case["case_data"])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        assert case["expect"] in res['msg']

        if case["expect"] in res['msg']:
            logger.error('断言失败，期望结果为：{},实际结果为{}'.format(case['expect'], res['msg']))
        else:
            logger.info('运行成功，测试编号为{}'.format(case['case_id']))


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
