"""
===============***===============
Auther : Lee
Date   : 2022-11-23 - 11:36
File   : test_login_businessdb.py
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
@allure.epic('第二天的测试')
@allure.feature('登录测试')
class TestLogin:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'businessdb.yaml'))
    cases = true_value(cases)
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    # db = DBUtils()
    # db1 = db.find_one("select * from tb_user order by rand() limit 1")
    # name = db1[1]
    # pswd = db1[2]
    name=get_ini_data('tb_user','username')
    pswd=get_ini_data('tb_user','psw')
    db.close()
    @pytest.mark.usefixtures('function')
    @pytest.mark.parametrize("case", cases, ids=ids)
    def test_login(self, case):
        if 'usname' in case['case_data'].values():
            case['case_data']['username'] = self.name
        if 'psw' in case['case_data'].values():
            case['case_data']['password'] = self.pswd
        response = requests.post(url=case['url'], data=case["case_data"])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        try:
            if case['case_id'] == 1:
                assert case["expect"] in res['msg']
            else:
                assert case["expect"] == res
        except AssertionError as e:
            logger.error('断言失败，期望结果为：{},实际结果为{}'.format(case['expect'], res))
            logger.exception(e)
            raise e
        else:
            logger.info('运行成功，测试编号为{}'.format(case['case_id']))


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
