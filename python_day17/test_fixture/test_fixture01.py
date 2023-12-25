"""
===============***===============
Auther : Lee
Date   : 2022-11-18 - 11:23
File   : test_fixture01.py
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
"""


@pytest.fixture(scope="function", autouse=True, )  # 声明了一个固件（夹具）
# scope代表作用域 ，autouse默认是Flase代表固件的运行状态，当autouse=True时执行当前目录下所有的作用层级都会执行
def func_fix():  # 定义固件的名称下面为执行的语句内容
    print("----------------case执行之前----------------")
    yield  # yield之前的代码会在case执行之前执行,yield之后的代码会case执行之后执行
    print("----------------case执行后后----------------")


@pytest.fixture(scope="function")  # scope默认的作用级别就是function级别
def func_fix1():
    print("-------------====case执行之前===-------------")
    yield  # yield之前的代码会在case执行之前执行,yield之后的代码会case执行之后执行
    print("--------------===case执行后后===-------------")


class TestFixture:
    @pytest.mark.usefixtures("func_fix1")  # 括号中输入固件的名称就会调用该固件，可以同时执行多个固件，固件名以字符串格式输入，以逗号分割
    def test_fixture01(self):
        print("这是第一条测试用例!")

    def test_fixture02(self):
        print("这是22222测试用例!")

    @pytest.mark.usefixtures('funtion')   #括号中输入不存在的夹具名时无法执行
    def test_fixture03(self):
        print("这是000333测试用例!")


if __name__ == '__main__':
    pytest.main(['-vs', "./test_fixture01.py"])
