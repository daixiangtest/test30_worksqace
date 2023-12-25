"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 15:54
File   : test_pytest05.py
===============***===============
"""
import pytest
import requests

"""
pytest的参数化
测试数据和测试代码分离,你写多少条case就会有多少个测试用例场景
"""


class TestLogin:
    cases = [
        {'case_data': {"username": "xiaohua", "password": "a123456"}, 'exp': {'code': 9999, 'msg': '登录成功!'}},
        {'case_data': {"username": "", "password": "a123456"}, 'exp': {'code': 1003, 'msg': '用户名不能为空!'}},
        {'case_data': {"username": "xiaohua", "password": ""}, 'exp': {'code': 1004, 'msg': '密码不能为空!'}},
        {'case_data': {"username": "xiaohu1", "password": "a123456"},
         'exp': {'code': 1000, 'msg': '用户名或密码错误!'}},
        {'case_data': {"username": "xiaohua", "password": "a123457"},
         'exp': {'code': 1000, 'msg': '用户名或密码错误!'}}]

    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        response = requests.post(url='http://127.0.0.1:5000/sign', data=case["case_data"])
        res = response.json()
        assert res == case["exp"]


if __name__ == '__main__':
    pytest.main(["./test_pytest06.py"])
