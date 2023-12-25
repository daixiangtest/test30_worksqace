"""
===============***===============
Auther : Lee
Date   : 2022-11-21 - 11:05
File   : test_pytest01_1.py
===============***===============
"""
import requests
import pytest

"""
# 失败重跑: 在实际接口自动化运行的过程中，因为 网络、服务器延时等问题，可能造成 接口调用失败。
所以，我们添加失败重跑，如果失败了，可以重新再跑。
1、 安装插件： pip install pytest-rerunfailures
2、再在 pytest.ini 文件中指定 重复运行次数 和每次运行后等待时间
 addopts = -vs --reruns=5 -- reruns-delay=3
 reruns= 5 代表运行5次  reruns-delay=3 代表每次间隔三秒
"""

"""
# 多线程运行: 如果接口很多，整个测试过程很长，我们就可以利用 多线程 运行脚本，
减少运行时间，提高效率。
1、安装插件：pytest-xdist
2、在运行中指定  '-n=线程数'，比如-n=2 代表2个线程运行脚本，-n=auto 代表最大线程运行脚本
3、劣势: 对编码要求高，如果编码有运行顺序，最好不要用这个。
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
        assert res == {'code': 1005, 'msg': '用户名存在!'}

    # 5.密码错误
    def test05(self):
        response = requests.post(url='http://127.0.0.1:5000/sign',
                                 data={'username': 'hbcd123',
                                       'password': '125'})

        res = response.json()
        print('hello,word')
        assert res == {'code': 1006, 'msg': '密码错误!'}


if __name__ == '__main__':
    pytest.main(['./test_pytest01_1.py', '-n=6'])
