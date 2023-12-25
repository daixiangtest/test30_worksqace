"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 15:54
File   : test_pytest05.py
===============***===============
"""
import pytest

"""
pytest的参数化
测试数据和测试代码分离,你写多少条case就会有多少个测试用例场景
"""


def add(a, b):
    return a + b


print(add(1, 2))  # 3

cases = [{"params1": 10, "params2": 20, "result": 30},
         {"params1": -10, "params2": 20, "result": 10},
         {"params1": 15, "params2": 25, "result": 40},
         {"params1": 333, "params2": 777, "result": 1110},
         {"params1": -11, "params2": 26, "result": 15}]


@pytest.mark.parametrize('case', cases)  # 会执行五条测试用例,因为cases有五个成员
def test_params(case):
    res = add(case["params1"], case['params2'])  # params1对应的值赋值给参数a ，params2对应的值赋值给参数b
    assert res == case["result"]  # 断言参数a+b的值与result对应的值是否一致


if __name__ == '__main__':
    pytest.main(["./test_pytest05.py"])
