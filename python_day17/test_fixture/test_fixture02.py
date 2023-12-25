"""
===============***===============
Auther : Lee
Date   : 2022-11-18 - 11:23
File   : test_fixture02.py
===============***===============
"""
import pytest

"""
测试固件(测试夹具)
使用固件的4种方式:
    1.@pytest.fixture(autouse=True): 声明固件时设置autouse=True会自动使用固件
    2.在需要使用固件的case上使用装饰器@pytest.mark.usefixtures("固件名1","固件名2"...)
    3.在需要使用固件的case参数传入固件名即可
    4.使用conftest.py配置文件中声明的固件,当前目录下的conftest.py只作用于当前目录下,不同目录下可以存在其他的conftest.py
    当根目录下的conftest.py与当前目录下的conftest.py的固件冲突时,按就近原则
固件的作用域: 依次从大到小  会话session -> 包package -> 模块module -> 类class -> 用例/函数function
默认的固件作用域是用例/函数级别
"""


@pytest.fixture(scope="class", autouse=True)
def class_fix():
    print("----------------测试类执行之前----------------")
    yield  # yield之前的代码会在一个测试类执行之前执行,yield之后的代码会一个测试类执行之后执行
    print("----------------测试类执行后后----------------")

@pytest.fixture(scope="function")  # scope默认的作用级别就是function级别
def func_fix1():
    print("-------------====case执行之前===-------------")
    yield  # yield之前的代码会在case执行之前执行,yield之后的代码会case执行之后执行
    print("--------------===case执行后后===-------------")

class TestFixture:
    def test_fixture01(self):
        print("这是第一条测试用例!")

    @pytest.mark.usefixtures("class_fix")  # 在需要使用的固件的case上使用装饰器
    def test_fixture02(self):
        print("这是22222测试用例!")

    def test_fixture03(self):
        print("这是000333测试用例!")


class TestFixture01:
    def test_fixture01(self):
        print("这是第一条测试用例!")

    def test_fixture02(self):
        print("这是22222测试用例!")


def test_fixture03():  # 单独写的case会被当作一个测试类
    print("这是000333测试用例!")


if __name__ == '__main__':
    pytest.main(['-vs', "./test_fixture02.py"])
