"""
===============***===============
Auther : Lee
Date   : 2022-11-04 - 18:30
File   : python_basic20.py
===============***===============
"""
"""
for 循环
for 变量 in 可迭代数据（str/list/tuple/dict/set/range()）:
    循环体
"""
# 遍历：就是把对象中的每一个成员都过一遍
str1 = '快要周六休息了'
print(len(str1))  # 7

# 值遍历
for i in str1:  # 把后面可迭代对象中的值赋值给i，每赋值一次，循环体执行一次
    print(i, end='')  # 快要周六休息了
print()  # 换行

# 下标遍历
for i in range(len(str1)):  # range(0,15) 生成了0-14的队列，刚好就是斯托瑞字符的串的下标
    print(str1[6-i], end='')  # 把i当作下标，去str1中取值  快要周六休息了
print()  # 换行

# 两种方式统计下面的字符串中h 出现的次数，手动实现了count函数
str1 = 'i like python so much'

count = 0
for i in str1:
    if i == 'h':
        count += 1
print('str1字符串中’h出现了{}次'.format(count))  # str1字符串中'h' 出现了2次

count = 0
for i in range(len(str1)):
    if str1[i] == 'h':
        count += 1
print('str字符串中"h"出现了{}次'.format(count))  # str1字符串中'h'出现了2次

# 使用while循环实现count函数
i = 0
count = 0
while i < len(str1):
    if str1[i] == 'h':
        count += 1
    i += 1
print("str1字符串中'h'出现了{}次".format(count))  # str1 字符串中"h '出现了2次

# 使用for循环遍历元组
tup1 = (1, 2, 3, 4, 5, 6)
for i in tup1:
    print(i)

for i in range(len(tup1)):
    print(tup1[i])

# 使用for循环遍历列表
list1 = [1, 2, 3, 4, 5]
for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])

# 使用for循环遍历集合
set = {1, 2, 3, 4, 5}
for i in set:
    print(i)

# 注意没有下标只可以使用值遍历

# 使用for循环遍历字典
dict1 = {'nanme': 'xiaohua', 'age': 18, 'set': '女'}

for i in dict1:  # 默认遍历的是字典的键
    print(i)  # nanme  age  set

# 如何遍历字典的值
for i in dict1.values():
    print(i)  # xiaohua  18  女

# 遍历字典的键值对
for i, j in dict1.items():
    print('字典的键是：', i, '字典的值是：', j)

# 使用while循环遍历字典
i = 0
while i < len(dict1):
    print(list(dict1.items())[i],end='')  # 转换列表的字典的值，和字典的长度是一致的
    i += 1

# 总结：字符串，列表，元组，集合，字典，都可以使用for循环遍历，集合没有下标，不能使用while遍历
