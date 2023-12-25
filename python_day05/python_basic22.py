"""
===============***===============
Auther : Lee
Date   : 2022-11-06 - 15:48
File   : python_basic22.py
===============***===============
"""

"""
冒泡排序
"""

# 数据交换，将a和b的值进行交换
a = 10
b = 20
# 传统写法
t = a  # 把a的值先给t
a = b  # 再把b的值给a
b = t  # 最后再把t的值给b

# pythonic的写法
a, b = b, a

print(a)  # a的值：10
print(b)  # b的值：20

a = a + b
b = a - b
a = a - b

print(a)  # a的值：10
print(b)  # b的值：20

# 有一个成员为int的类型的列表，[10,39,18,67,99,2],怎么互换0号和1号下标成员的位置
list1 = [10, 39, 18, 67, 99, 2]
list1[0], list1[1] = list1[1], list1[0]
print(list1)  # [39, 10, 18, 67, 99, 2]

# 怎么把列表中最大的成员放到最后一位
list1 = [10, 39, 18, 67, 99, 2]
for j in range(len(list1) - 1):
    if list1[j] > list1[j + 1]:
        list1[j], list1[j + 1] = list1[j + 1], list1[j]
print(list1)  # [10, 18, 39, 67, 2, 99]

# 给列表排序
list1 = [10, 39, 18, 67, 99, 2]
for i in range(len(list1) - 1):
    for j in range(len(list1) - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)

# 精简循环，第一次外循环结束，最大值已经再最后面了，所有第二次外循环的时候，最后一位数无需在内循环中比较大小了，所以内循环的循环次数就可以递减
# 所以通过内循环的循环次数减去i所以当i为0时内循环循环5次，当i为1时内循环就循环4次，以此类推
list1 = [10, 39, 18, 67, 99, 2]
for i in range(len(list1) - 1):  # 0,1,2,3,4
    for j in range(len(list1) - 1 - i):  # 01234，0123，012，01
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

print(list1)
