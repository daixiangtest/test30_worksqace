"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 18:47
File   : python_basic41.py
===============***===============
"""
"""
错误和异常的区别
错误：不能通过解释器的编译（静态检查），这种叫错误
异常：编译通过，但是运行时出现的问题叫做异常
"""

# 常见的错误
#  print()    缩进错误
# print(      语法错误

# 常见的异常
list = [1, 2, 3, 4]
# print(list[4])  # 下标越界异常  list index out of range
# print(int('10a'))  # 值异常   ValueError: invalid literal for int() with base 10: '10a'
# print(10 / 0)  # 除0异常  ZeroDivisionError: division by zero
