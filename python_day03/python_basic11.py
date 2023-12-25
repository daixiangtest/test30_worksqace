"""
===============***===============
Auther : Lee
Date   : 2022-11-02 - 16:16
File   : python_basic11.py
===============***===============
"""
"""
本章讲解：元组（tuple）用来保存一组任意类型数据，注意：元组是不可变类型，创建后数据不能修改元组也有下标序列
三大序列：字符串，列表，元组
"""

# 1.元组的声明
tup1 = ()  # 创建了一个空元组
print(type(tup1))  # <class 'tuple'>
student = ('刘备', '关羽', '张飞', '赵云')
print(student)  # ('刘备', '关羽', '张飞', '赵云')

# 2.元组在声明时候，一定要注意，如果元组只有一个成员，一定要加逗号
student1 = '曹操'
print(type(student1), student1)  # <class 'str'> 曹操
student1 = ('曹操',)
print(type(student1), student1)  # <class 'tuple'> ('曹操',)
student1 = '曹操', '夏侯惇'
print(type(student1), student1)  # 自动组包：任意无符号对象以逗号分离都会组包成元组，<class 'tuple'> ('曹操', '夏侯惇')
print(type(student1), student1)
stu2 = [1, 2, 3], 1, '2'
print(type(stu2), stu2)  # <class 'tuple'> ([1, 2, 3], 1, '2')

# 3.查看元组中的数据,通过下标访问
student = ('刘备', '关羽', '张飞', '赵云')
print(student[-1])  # 赵云
print(student[:-1])  # ('刘备', '关羽', '张飞')
print(student[::2])  # ('刘备', '张飞')

# 4.元组是不可变类型，所以不能修改值
student = ('刘备', '关羽', '张飞', '赵云')
# student[1] ='黄忠'  #TypeError: 'tuple' object does not support item assignment

"""
元组和列表的区别？
1元组用小括号（）声明，列表用中括号[]声明
2元组和列表都是有序的
3元组和列表都可以存放任意类型的数据
4列表是可变的，元组是不可变的
"""

# 序列的特性,有下标、可以切片,可以+号拼接, *号重复,有通用的API,比如:in、not in. max(). min(). sum()...
tup2 = (1, 2, 3, 4, 5, 6, 7)

print(max(tup2))  # 最大值7
print(min(tup2))  # 最小值1
print(2 in tup2)  # 布尔类型 True
print(sum(tup2) / len(tup2))  # 平均值 4.0
