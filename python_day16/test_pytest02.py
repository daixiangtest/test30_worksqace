"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 14:10
File   : test_pytest02.py
===============***===============
"""
import requests
import pytest
import pytest
"""
1.-m 标记,我们可以为测试用例添加标记,并且指定运行某个标记,可以在类和方法上使用
2.创建pytest.ini文件,并且添加标记到ini文件中
    常见的pytest.ini文件修改pytest框架默认的运行模式
    1.addopts = -vs  # addopts参数可以更改默认的运行命令参数
    2.可以在pytest.ini文件中声明测试文件的匹配规则
        python_files = check_* *_check  # 模块名必须以check_ 开头或者 _check结尾
        python_classes = Check  # 测试类必须以Check开头,并且不能有__init__方法
        python_functions = check_*  # 测试case必须以check_开头
    这样就相当于重写了pytest的默认的命名规则
    这种用法一般在一些大公司会有要求命名符合自己公司的命名规范去使用,在一般情况,尽量不要去修改默认的命名规则
    3.markers = tester01  这就创建了tester01标记,给case进行标记,@pytest.mark.tester01 标记了一个case
    4.testpaths = ./testcase  # 修改默认查找测试用例的路径,路径相当于pytest.ini文件的路径
3.更改case默认执行顺序,需要下载第三方插件库完成 pip install pytest-ordering
然后在给case标记 @pytest.mark.run(order=执行顺序)
4.跳过指定用例
@pytest.mark.skip(reason=原因)  这是直接跳过
@pytest.mark.skipif(条件,reason=原因)  符合条件才跳过
"""

age = 19


class Testlogin:
    # 1正确流程
    def test01(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd123',
                                       'password': 'hbcd123'})
        res = response.json()
        assert res == {'code': 1007, 'msg': '登录成功!'}

    # 2.用户名不能为空
    @pytest.mark.run(ordre=3)
    @pytest.mark.skip(reason='不需要测')
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

    # 4.用户名不能为空
    @pytest.mark.account
    def test04(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd12335',
                                       'password': '25645'})
        res = response.json()
        assert res == {'code': 1005, 'msg': '用户名不存在!'}

    # 5.密码错误
    @pytest.mark.cash_loan
    @pytest.mark.run(order=3)
    @pytest.mark.skipif(age > 18, raason='可以测了')
    def check05(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd123',
                                       'password': '125'})
        res = response.json()
        assert res == {'code': 1006, 'msg': '密码错误!'}


if __name__ == '__main__':
    pytest.main(['-m cash_loan or account','-vs','./test_pytest02.py'])  # 执行标记为cash_loan 或标记为account的case
    # pytest.main(['-m not account'])   #执行没有标记为account的所有case
    # pytest.main(['-q', './test_pytest02.py'])
