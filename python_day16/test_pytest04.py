"""
===============***===============
Auther : Lee
Date   : 2022-11-17 - 15:54
File   : test_pytest04.py
===============***===============
"""
import pytest

"""
pytest的参数化
"""

cases = ['A', 'B', "C", "D", 'E']


# @pytest.mark.parametrize(变量名:str, 数据源:list)  参数化测试用例,数据源列表中有多少个成员,测试用例就执行多少次
@pytest.mark.parametrize('case', cases)  # 把cases中的成员循环赋值给case,每赋值一次测试用例执行一次
def test_params(case):  # 定义一个函数方法把每次赋值的值入参
    print("这是一条测试case", case)


if __name__ == '__main__':
    pytest.main(["./test_pytest04.py"])
