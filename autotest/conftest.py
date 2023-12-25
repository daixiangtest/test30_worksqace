"""
===============***===============
Auther : Lee
Date   : 2022-11-21 - 13:50
File   : conftest.py
===============***===============
"""
import pytest

from autotest_03.comms.dbutils import DBUtils


# conftest.py模块中声明的固件试可以供当前所在目录下的所有case来调用的，一个目录中只能有一个conftest

@pytest.fixture(scope="function")
def function():
    print("====这是conftest.py的函数级别固件开始====")
    yield
    print("====这是conftest.py的函数级别固件结束====")


@pytest.fixture(scope="class")
def db():
    db = DBUtils()
    yield db
    db.close()


# @pytest.fixture(scope="class")
# def class_fixture():
#     print("----====这是conftest.py的类级别固件开始====----")
#     yield
#     print("----====这是conftest.py的类级别固件结束====----")

def pytest_collection_modifyitems(items):  # 钩子函数
    """
    测试用例收集完成时，将收集到的name和nodeid的中文显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        print(i.nodeid)
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")

# 以上代码的作用是将当前目录下的默认编码unicode更改为utf-8的编码格式这样更加有利于中文的展示

# hook函数/钩子函数: 是pytest框架的默认行为,pytest框架的运行会自动调用钩子函数执行
# pytest中的钩子函数按功能一共分为6类：引导钩子，初始化钩子、用例收集钩子、用例执行钩子、报告钩子、调试钩子
# 共享办公平台wiki平台  swagger和yapi
# 常见的配置文件类型:   .ini  .yaml  .json  .xml  .properties

