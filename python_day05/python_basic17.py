"""
===============***===============
Auther : Lee
Date   : 2022-11-04 - 10:54
File   : python_basic17.py
===============***===============
"""

"""
while 循环语法
while 条件：
    语句块
当条件成立的时候，一直执行语句块，语句块每执行一次都会再次判断是否成立，成立则判断执行语句块，反之则会停止循环
"""

# 循环案列1；打印1-100的字数
i = 1
while i <= 100:
    print(i)  # i=1,2,3....100
    i += 1  # i自增1，i=i+1

# 循环案例2：打印1-100的偶数
i = 1
while i <= 100:
    if i % 2 == 0:  # 判断i是不是偶数，是偶数才执行
        print(i)
    i += 1

# 第二种方法
i=2
while i<=100:
    i+=2
    print(i)   #2,4,6,8,10,12……

# # 求 0-100 偶数的数量
# i = 2
# le = 0
# while i <= 100:
#     if i % 2 == 0:
#         le += 1
#     i += 2
# print(le)

# 求1-2022年之间的闰年的数量
# y = 1
# lee = 0
# while y <= 2022:
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         lee += 1
#     y += 1
# print(lee)

# 求 0-100 偶数的和
# i = 1
# su = 0
# while i <= 100:
#     if i % 2 == 0:
#         su += i
#     i += 1
# print(su)

# 求 0-100 奇数的和
# i = 1
# su = 0
# while i <= 100:
#     if i % 2 != 0:
#         su += i
#     i += 1
# print(su)

# 求1-10的阶乘值,1*2*3*4...*10
num = 1
a = 1
while 1 <= num <= 10:
    a *= num
    num += 1
print(a)
