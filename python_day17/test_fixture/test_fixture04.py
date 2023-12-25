"""
===============***===============
Auther : Lee
Date   : 2022-11-18 - 11:23
File   : test_fixture03.py
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
    5.固件又可以使用多个固件,固件之间可以相互依赖
"""

#
@pytest.fixture(name='lee')  # 注意一旦重命名固件,原固件名称不可用
def function01():
    print("====这是嵌套的函数级别固件开始====")
    yield
    print("====这是嵌套的函数级别固件结束====")


@pytest.fixture(scope="function")
def func_fix():
    print("----------------case执行之前----------------")
    yield 1000    #yield后面的数值必须打包到固件名中当作参数给case的时候才会返回该数值
    print("----------------case执行后后----------------")

ids = ['小花', '小兰', '小黑', '大白']
params1=['xiaohua', 'xiaolan', 'xiaohei', 'dabai']

@pytest.fixture(params=params1, ids=ids)
#当参数输入为多个值时固件会依次给执行其中的参数，且ids中需要输入对象的ids的值ids中的值相当于给固件执行同一个case时区分的方法名
def fix_params(request):  #case执行固件的参数时case中必须输入request请求才能依次返回固件中的参数
    print("这是一个参数化的固件,开始...")
    yield request.param
    print("这是一个参数化的固件,结束...")


class TestFixture:
    def test_fixture01(self,func_fix):  # 只有把固件名当作参数传给case的时候才可以使用固件返回的参数
        print("这是第一条测试用例!")
        print(func_fix)  # 1000 返回的时固件名yield后面的值

    @pytest.mark.usefixtures("func_fix")
    def test_fixture02(self):
        print("这是22222测试用例!")

    def test_fixture03(self, fix_params):
        print("这是000333测试用例!")
        print(fix_params)


if __name__ == '__main__':
    pytest.main(['-vs', "./test_fixture04.py"])
