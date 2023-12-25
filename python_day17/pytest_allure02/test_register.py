"""
===============***===============
Auther : Lee
Date   : 2022-11-19 - 18:55
File   : test_register.py
===============***===============
"""
import pytest
import requests

"""
注册接口的参数化
"""


class Test_Tianmao:
    cases = [{'case_data': {"username": "", "psw": "asn12456", "re_psw": "asn12456", "phone": 13556545654,
                           "email": "98364@qq.com"},
              'exp': {"code": 1006, "msg": "用户名输入不能为空!"}},
             {'case_data': {"username": "xiaoyao1", "psw": "", "re_psw": "", "phone": "", "email": ""},
              'exp': {"code": 1007, "msg": "密码不能为空!"}},
             {'case_data': {"username": "xiaoyao01", "psw": "abd3826", "re_psw": "abd3826", "phone": "", "email": ""},
              'exp': {"code": 1008, "msg": "手机号不能为空!"}},
             {'case_data': {"username": "xiaoyao01", "psw": "abd3826", "re_psw": "abd3826", "phone": '156.6a355632',
                           "email": "983643@163.com"},
              'exp': {"code": 1009, "msg": "手机号格式错误!"}},
             {'case_data': {"username": "xiaoyao01", "psw": "adb3826", "re_psw": "adb3826", "phone": 15656355632,
                           "email": ""},
              'exp': {"code": 1010, "msg": "邮箱格式输入不能为空!"}},
             {'case_data': {"username": "xiaoyao01", "psw": "adb3826", "re_psw": "abd3826", "phone": 15656355632,
                           "email": "9864@qq.com"},
              'exp': {"code": 1011, "msg": "两次密码不一致!"}},
             {'case_data': {"username": "xiaoyao01", "psw": "adb3826", "re_psw": "adb3826", "phone": 15656356532,
                           "email": "6543."},
              'exp': {"code": 1012, "msg": "邮箱格式不正确!"}},
             {'case_data': {"username": "hbcd123", "psw": "hbcd123", "re_psw": "hbcd123", "phone": 15656356532,
                           "email": "9865@qq.com"},
              'exp': {"code": 1013, "msg": "用户名已经注册!"}},
             {'case_data': {"username": "xiaoyao11", "psw": "hbcd123", "re_psw": "hbcd123", "phone": 15656356532,
                           "email": "9864@qq.com"},
              'exp': {"code": 1014, "msg": "邮箱已经使用!"}},
             {'case_data': {"username": "xiaoyao", "psw": "abd1254", "re_psw": "abd1254", "phone": 15896535251,
                           "email": "9865@qq.com"},
              'exp': {"code": 1015, "msg": "手机号已经注册!"}},
             {'case_data': {"username": "xiaoy2", "psw": "abd145", "re_psw": "abd145", "phone": 13556356588,
                           "email": "9861@163.com"},
              'exp': {"code": 1016, "msg": "登录成功!"}}, ]

    @pytest.mark.parametrize('case', cases)
    def test_tianmao(self, case):
        response = requests.post(url='http://127.0.0.1:5800/tianmao', data=case['case_data'])
        res = response.json()
        assert res == case['exp']

