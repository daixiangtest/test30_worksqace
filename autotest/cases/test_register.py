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
注册接口的参数化
"""


@pytest.mark.T1
@allure.epic('第一天的测试')
@allure.feature('注册测试')
class Test_Tianmao:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'register_yaml.yaml'))
    ids = [case['case_title'] for case in cases]

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_tianmao(self, case):
        response = requests.post(url=case['url'], data=case['case_data'])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        try:
            assert res == case['expect']
        except Exception as e:
            logger.error('断言失败，期望结果为:{},实际结果为{}'.format(case['expect'], res))
            logger.exception(e)
            raise e  # 处理异常后需要手动提起异常否则测试报告会默认通过
        else:
            logger.info('运行成功，测试编号为{}'.format(case['case_id']))


if __name__ == '__main__':
    pytest.main(['./test_register.py'])
