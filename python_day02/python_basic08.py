"""
===============***===============
Auther : Lee
Date   : 2022-11-01 - 18:26
File   : python_basic08.py
===============***===============
"""
"""
if 语句
if 条件：
    语句块
如果条件满足则执行语句块，反之不执行语句块
"""

a, b = 10, 20
if a > b:  # True
    print('a<b成立')  # a<b成立

print("hello")  # hello

num = 10
if num % 2 == 0:  # True  奇数取余2结果是1，就是True,偶数取余 结果是0，也就是False
    print(num)  # 10

num1 = 20
if num1 % 2:  # False  奇数取余2结果是1，就是True,偶数取余 结果是0，也就是False
    print(num1)  # 20

"""
if 条件：
    语句块1
else：
    语句块2
如果条件成立则执行语句块1，条件不成立则执行语句块2
"""

a, b = 10, 20
if a > b:  # False
    print('a>b成立')
else:
    print('a>b不成立')

# 用户输入一个整数,判断是奇数还是偶数
num = int(input('请输入整数'))
if num % 2:
    print('{}是奇数'.format(num))
else:
    print('%d是偶数' % num)
# 判断是否可以退休,用户输入年龄,如果大于60岁则可以退休,反之输出再坚持几年
age = int(input('请输入年龄'))
if age > 60:
    print('恭喜您可以退休了')
else:
    print('再坚持几年')
