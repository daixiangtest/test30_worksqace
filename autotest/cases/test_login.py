"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 15:54
File   : test_pytest05.py
===============***===============
"""
import pytest
import requests
import allure
from autotest_03.comms.log_utils import logger
from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.ptrhon_xfj import get_yaml_data
import os

"""
pytest的参数化
测试数据和测试代码分离,你写多少条case就会有多少个测试用例场景
"""


@pytest.mark.T1
@allure.epic('第一天的测试')
@allure.feature('登录测试')
class TestLogin:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'login_yaml.yaml'))
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    @pytest.mark.usefixtures('function')
    @pytest.mark.parametrize("case", cases, ids=ids)
    def test_login(self, case):
        response = requests.post(url=case['url'], data=case["case_data"])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        try:
            assert res == case["expect"]
        except AssertionError as e:
            logger.error('断言失败，期望结果为：{},实际结果为{}'.format(case['expect'], res))
            logger.exception(e)
            raise e
        else:
            logger.info('运行成功，测试编号为{}'.format(case['case_id']))


if __name__ == '__main__':
    pytest.main([__file__])
