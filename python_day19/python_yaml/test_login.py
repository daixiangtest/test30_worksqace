"""
===============***===============
Auther : Lee
Date   : 2022-11-22 - 14:43
File   : test_login.py
===============***===============
"""
import pytest
import requests
import allure

import yaml

"""
pytest的参数化
测试数据和测试代码分离,你写多少条case就会有多少个测试用例场景
"""


@allure.epic('第一天的测试')
@allure.feature('登录测试')
class TestLogin:
    with open('login_yaml.yaml', mode='r', encoding='utf-8')as fr:
        cases=yaml.safe_load(fr)

    #@pytest.mark.usefixtures('function')
    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        response = requests.post(url=case['url'], data=case["case_data"])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        try:
            assert res == case["expect"]
        except AssertionError as e:
            logger.error('断言失败，期望结果为：[{}],实际结果为[{}]'.format(case['expect'], res))
            logger.exception(e)
            raise e
        else:
            logger.info('运行成功，测试编号为[{}]'.format(case['case_id']))


if __name__ == '__main__':
    pytest.main(['-vs', "./test_login.py"])