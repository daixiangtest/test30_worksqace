"""
===============***===============
Auther : Lee
Date   : 2022-11-03 - 13:59
File   : python_basic14.py
===============***===============
"""
"""
python的数据类型: number数字/str字符串/list列表/tuple元组/set集合/dict字典

可变类型: 列表、集合、字典
不可变类型: 数字、字符串、元组
可变类型和不可变类型的区别: 
可变类型可以对数据进行增删改,物理地址不变,也就是增删改后还是原来的对象,不可变类型增删改后,物理地址发生改变,是一个新的对象

有序的: 字符串、列表、元组
无序的: 数字、集合、字典
有序的和无序的数据类型区别: 有序的有下标,可以通过下标访问值、切片截取等操作,还有一些通用的api。无序的则没有

"""
"""
我们发现列表、元组、集合、字典都可以保存一组数据,不过他们有不同的特征
1.从保存值的方式来看,列表、元组、字典、集合都可以保存一组值
2.列表和元组是可以通过下标去访问，而字典、集合没有下标,字典通过key获取value
3.增删改的方式不同
4.可变类型:列表、集合、字典(值可以被修改), 不可变类型:数字、字符串、元组(值不能改变)
"""

# 1.列表、元纽、集合都是保存单个值,而字典是以键值对的形式来保存数据
list1 = [1, 2, 3, 4, 5]
tup1 = (1, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
dict1 = {'name': 'xiaohua', 'age': 20, 'sex': 'nv'}

# 2.列表和元组是可以通过下标去访问,而集合没有下标,字典访问值是通过key
print("list列表是通过下标访问值，比如获取下标0位置的元素:", list1[0])
print("tuple元组也是通过下标访问值，比如获取下标0位置的元素:", tup1[0])
print('集合不能通过key获取value', dict1["name"])
print("字典通过key获取value:", dict1.get("name"))

# 3.增加元素
list1.append(6)  # 列表新增单个元素
list1.extend([7, 8, 9])  # 列表新增多个元素
print("元组是不可变类型,不可以增删改")
set1.add(6)  # 集合增加单个元素
set1.update({7, 8, 9})  # 集合增加多个元素
dict1["class"] = 30  # 字典增加单个键值对
dict1.update({"phone": 110, 'id': 1001})  # 宇典增加多个键值对

# 5.修改
list1[0] = 999  # 列表通过下标修改
print("元组是不可变类型,不可以增删改")
print('集合没有下标，不能直接进行修改')
dict1["age"] = 25  # 字典通过key键修改value值

# 以上是对列表,元组,集合,字典的总结，还有一些通用的api
list1 = [1, 2, 3, 4, 5]
tup1 = (1, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
dict1 = {'name': 'xiaohua', 'age': 20, 'sex': '女儿'}

# 1.字符串、列表、元组都是有序的,可以通过下标访问值,切片截取等操作
str1 = 'qwerqwerqwer'
print(str1[1])  # w
print(str(-2))  # e
print(str1[1:5])  # werg
print(str1[1:5:2])  # wr
print(str1[:6])  # gwergw
print(list1[1])  #
print(tup1[4])  # 5
print(tup1[3:])  # (4,5)

# 2.求长度用Len()
print(len(str1))  # 12
print(len(list1))  # 5
print(len(tup1))  # 5
print(len(set1))  # 5
print(len(dict1))  # 3

# 3.判断某个值是否在字符串、列表、元组、集合、字典(字典比较特殊,判断是key)使用in /not in
print('x' in str1)  # False
print(4 in list1)  # True
print(5 in tup1)  # True
print(3 not in set1)  # False
print('name' in dict1)  # True

# 4.求列表，元组，集合，字典中的：马修（）最大值  min（）最小值  sun（）求和
list1 = [1, 2, 3, 4, 5]
tup1 = (1, 2, 3, 4, 5)
set1 = {1, 2, 3, 4, 5}
dict1 = {'class': 30, 'age': 20, 'score': 100}
print('列表中的最大值、最小值、和为:', max(list1), min(list1), sum(list1))  # 列表中的最大值、最小值、和为: 5 1 15
print('元组中的最大值、最小值、和为:', max(tup1), min(tup1), sum(tup1))  # 元组中的最大值、最小值、和为: 5 1 15
print('集合中的最大值、最小值、和为:', max(set1), min(set1), sum(set1))  # 集合中的最大值、最小值、和为: 5 1 15
print('字典中的最大值，最小值，和为：', max(dict1.values()), min(dict1.values()), sum(dict1.values()))
# 字典中的最大值，最小值，和为： 100 20 150

# 5.字符串，列表，元组中统计元素出现的次数 count()
str1 = 'good good study and day day up'
print(str1.count('o'))  # 4
list1 = [1, 2, 3, 4, 1, 2, 3]
print(list1.count(1))  # 2
tup1 = (2, 3, 4, 5, 6, 7, 1, 2, 3)
print(tup1.count(2))  # 2

# 6.字符串， 列表 元组都可以使用+号拼接，*号重复
str1, str2, str3 = 'i', 'love', 'you'
str4 = str1 + str2 + str3
print(str4)  # iloveyou

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # [1, 2, 3, 4, 5, 6]

tup1 = (9, 8, 7)
print(tup1 * 3)  # (9, 8, 7, 9, 8, 7, 9, 8, 7)

# 7.列表，元组，字符串，集合的相互转换
phone = '18656032222'
list1 = list(phone)
print(list1)  # ['1', '8', '6', '5', '6', '0', '3', '2', '2', '2', '2']

# 列表转字符串
list1 = [1, 2, 3]
print(str(list1))  # [1, 2, 3]

# 列表转元组
list1 = [1, 2, 3]
print(tuple(list1))  # (1,2,3)

# 元组转列表
tup1 = (1, 2, 3)
print(list(tup1))  # [1,2,3]

# 字符串转元组
phone = '18656032222'
print(tuple(phone))  # ('1', '8', '6', '5', '6', '0', '3', '2', '2', '2', '2')

