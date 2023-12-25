"""
===============***===============
Auther : Lee
Date   : 2022-11-06 - 15:01
File   : python_basic21.py
===============***===============
"""

"""
循环嵌套
"""

print(1)  # 打印1，并且换行
print(2, end='')  # 打印2，并且不换行
print()  # 换行

"""
打印一个4行5列用*好组成的长方形

"""

for i in range(4):
    print('*****')

# 用for循环打印
for i in range(4):
    for j in range(5):
        print('*', end='')
    print()

"""
用*打印一个三角形
"""
# 第一打印一个*，第二次打印2个**，第三打印3个**……

for i in range(4):
    for j in range(i + 1):
        print('*', end='')
    print()

# 打印99乘法口诀表
for i in range(1, 10):  # =123456789
    for j in range(1, i + 1):  # j=1 12 123 1234 12345 123456 1234567 12345678 123456789
        print('{}*{}={}'.format(j, i, j * i), end='')
    print()

for i in range(9):
    for j in range(i+1):
        print('{}*{}={}'.format(j+1,i+1,(j+1)*(i+1)),end='')
    print()