"""
===============***===============
Auther : Lee
Date   : 2022-11-04 - 18:11
File   : python_basic19.py
===============***===============
"""
"""
for 循环
for 变量 in 可迭代数据（str/list/tuple/dict/set/range)）
     循环体
遍历：就是把对象中的每一个成员都过一遍
"""


# range() 函数，生成一个包前不包后的整数队列,如果只写一个参数,默认从0开始
for i in range(0, 5):  # [0,1,2,3, 4] 把整数队列中的值循环赋值给i,每赋值一 一次循环体执行-次
    print(i)  # 0,1,2,3,4

for i in range(5):
    print(i)  # 0,1,2,3,4

print(list(range(1, 101, 2)))  # 生成1-100的奇数, 第三个参数是步长
# 使用for循环,求出1 -100的奇数和
sm = 0
for i in range(1, 101):
    if i % 2:
        sm += i
print(sm)  # 1-100的奇数和为2500

sm=0
for i in range (1,101,2):
    sm +=i
print('1-100的奇数和：',sm)   #1-100的奇数和：2500

# 使用for循环打印1-2022年所有的闰年
# y = 1
# cou = 0
# for y in range(1, 2023):
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         cou += y
#         print(y)
# print(cou)
# 使用for循环打印1-2022年所有的闰年的数量




