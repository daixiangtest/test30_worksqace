"""
===============***===============
Auther : Lee
Date   : 2022-11-02 - 17:53
File   : python_basic12.py
===============***===============
"""

"""
本章讲解：集合
集合：用来保存一组数据，特征：无序，没有索引，不能重复，不能保存可变的数据
集合本身是可变类型，值可以改变
"""

# 1.集合的声明
student = set()  # 声明了一个空集合，set代表集合
print(type(student), student)  # <class 'set'> set()
student1 = {'孙权', '陆逊', '孙坚', '吕蒙', '孙策', '陆逊'}
print(student1)  # {'吕蒙', '孙权', '孙坚', '陆逊', '孙策'}
# print(student1[0])  #集合是没有索引的

# 增加元素
student1.add('鲁肃')  # 增加单个元素
student1.add('黄盖')
print(student1)  # {'吕蒙', '黄盖', '孙坚', '孙权', '孙策', '陆逊', '鲁肃'}
student1.update({'甘宁', '太史慈', '孙策'})  # 增加多个元素
print(student1)  # {'太史慈', '陆逊', '吕蒙', '黄盖', '孙坚', '孙策', '鲁肃', '孙权', '甘宁'}

# 删除元素
# student1.pop()  # 不推荐，每次删除第一个元素
student1.remove('太史慈')
print(student1)  # {'黄盖', '孙权', '甘宁', '吕蒙', '鲁肃', '陆逊', '孙坚', '孙策'}
# del 被删对象
del student1
# print(student1)  # 因为已经被从内存释放了所以打印报错变量为定义

# set 集合中的元素不能重复
set1 = {'老刘', '老王', '老徐', '大程', '老刘'}
print(set1)  # {'老刘', '老王', '大程', '老徐'}

# 怎么快速去除一个列表中的重复数据
list1 = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6]
print(list(set(list1)))  # 利用集合自动去重的特性可以帮我们把其他数据去重

# 集合的交集intersection()  和 并集union()
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {3, 4, 5, 6, 7, 8, 9}

print(set1.intersection(set2))  # 取相同的值{3, 4, 5, 6, 7}
print(set1.union(set2))  # 取所有的值去重 {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1.symmetric_difference(set2))  # {1, 2, 8, 9} 差集，取两个列表中不相同的值
