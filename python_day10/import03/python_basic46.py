"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 20:23
File   : python_basic46.py
===============***===============
"""
# 使用两种引包方式，引入python_basic28模块下area（）函数并调用
# from python_day06.python_basic28 import area
# import python_day06.python_basic28 as lv

# print(area(10, 20))
# print(lv.area(10, 20))
# 使用两种引包方式，引入python_basic34模块下Emp类并新建对象，通过对象调用方法
# from python_day08.python_basic34 import Emp
import python_day08.python_basic34 as ld

# emp1=Emp()
# emp1.emp_name='xiaohei'
# emp1.emp_no=1001
# emp1.emp_sal=18
# print(emp1.emp_no,emp1.emp_sal,emp1.emp_name)
emp2 = ld.Emp()
emp2.emp_name = 'dahei'
emp2.emp_no = 1002
emp2.emp_sal = 15
print(emp2.emp_no, emp2.emp_sal, emp2.emp_name)
