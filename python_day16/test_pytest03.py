"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 15:25
File   : test_pytest03.py
===============***===============
"""
import pytest
import pytest_check

"""
pytest断言分为两种: 一种是原生的assert断言,另一种是多重断言
1.可以使用原生的断言方式 assert (断言: 比对实际结果和预期结果是否一致)
    assert A==B
    assert A>B
    assert A in B 
2.多重断言:
    1.使用pytest-assume插件,pip install pytest-assume, 特点一个断言失败后会继续执行
    2.使用pytest-check插件,pip install pytest-check,特点一个断言失败后会继续执行,会显示详细断言信息
    
    多重断言与原生断言的区别是，一个测试case里原生断言只能断言一次，而多重断言可以断言断言多次
"""


class TestAssert:
    # 使用原生的断言，一旦失败就会停止case
    # def test_assert01(self):
    #     assert 1+4==5
    #
    # def test_assert02(self):
    #     assert 'x' in 'python'
    #     print(666)
    #     assert 8+5>11
    def test_assert03(self):
        print('第一个断言')
        pytest.assume('a' == 'b')
        print('第二个断言')
        pytest.assume('a' in 'abc')
        print('第三个断言')
        pytest.assume(2 == 2)

    def test01(self):
        a = 'x'
        b = 'huahua'
        print('第一次断言')
        pytest_check.is_in(a, b, 'b不包含a')  # 断言a再b的里面
        print('第二次断言')
        pytest_check.equal(a, b, 'a不等于b')  # 断言a与b相等
        print('第三次断言')
        pytest_check.is_not_in(a, b, 'b包含a')  # 断言a不在b的里面


if __name__ == '__main__':
    pytest.main(['-vs', './test_pytest03.py'])
