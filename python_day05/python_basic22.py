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

# 列表的循环推导式
# 获取1到20直接的勾股定理函数a**2+b**2==c**2
x2 = []
for a in range(1, 20):
    for b in range(a, 20):
        for c in range(b, 20):
            if a ** 2 + b ** 2 == c ** 2:
                x2.append([a, b, c])
print(x2)
# 使用推导式的方式可以简化代码量
x = [[a, b, c] for a in range(1, 20) for b in range(a, 20) for c in range(b, 20) if a ** 2 + b ** 2 == c ** 2]
print(x)

# enumerate()函数
lits1 = ["香蕉", "苹果", "橘子", "葡萄"]
for i, j in enumerate(lits1, 1):  # 遍历列表中的元素并为每个元素计数，i为计数，j为元素，1代表从1开始遍历
    print(i, j)

# 将连个列表合并不能有重复的元素
plays = ['张三', "李四", "王二", "马五"]
teams = ['michael', "张三", "马五", "tom"]
print(dir(plays))
a = plays + teams
b = list(set(a))
print(b)
