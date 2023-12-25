"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 13:52
File   : test_pytest01.py
===============***===============
"""
import pytest
import requests


"""
pytest的安装：pip install pytest
2.查看是否安装成功：pytest--version
3.测试用例的规则：
    1.模块名必须一test_开头或者_test结尾
    2.测试类必须以    Test开头，并且不能有__init__方法
    3.测试case必须以test开头
    4可以使用原生的断言方式assert（断言：比对实际结果和预期结果是否一致）
    assert A==B
    assertA>B
    assertA in  B
"""

class Testlogin:
    # 1.正确流程
    def test01(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd123',
                                       'password': 'hbcd123'})

        res = response.json()
        assert res == {'code': 1007, 'msg': '登录成功!'}

    # 2.用户名不能为空
    def test02(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': '',
                                       'password': 'hbcd123'})

        res = response.json()
        assert res == {'code': 1003, 'msg': '用户名输入不能为空!'}

    # 3.密码不能为空
    def test03(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd123',
                                       'password': ''})

        res = response.json()
        assert res == {'code': 1004, 'msg': '密码输入不能为空!'}

    # 4.用户名不存在
    def test04(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd12335',
                                       'password': '25645'})

        res = response.json()
        assert res == {'code': 1005, 'msg': '用户名不存在!'}

    # 5.密码错误
    def test05(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd123',
                                       'password': '125'})

        res = response.json()
        print('hello,word')
        assert res == {'code': 1006, 'msg': '密码错误!'}


if __name__ == '__main__':
    # pytest.main()  # 默认执行当前目录下所有符合条件的case
    pytest.main(['./test_pytest01.py'])  # 运行指定模块下所有符合条件的case
    pytest.main(['./test_pytest01.py::TestLogin'])  # 运行指定模块的指定类下所有符合条件的case
    pytest.main(['./test_pytest01.py::TestLogin::test03'])  # 运行指定的case
    # 命令参数
    pytest.main(['-q', './test_pytest01.py'])  # 静默模式，只展示运行结果
    pytest.main(['-v', './test_pytest01.py'])  # 详细信息模式，展示详细的执行结果
    pytest.main(['-s', './test_pytest01.py'])  # 输出case中的打印和日志信息
    pytest.main(['-vs', './test_pytest01.py'])  # 命令参数可以组合使用
    pytest.main(['-k test', './'])  # 匹配指定目录下所有包含关键字的包，模板，类，case符合条件的case
    pytest.main(['-k test and lee', './'])  # 匹配指定目录下所有包含关键字的包，模块，类，case符合条件的case
    pytest.main(['-k not test', '-vs', './'])  # 匹配指定目录下所有不包含test关键字的包，模块，类，case的case
