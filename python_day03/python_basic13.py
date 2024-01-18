"""
===============***===============
Auther : Lee
Date   : 2022-11-02 - 18:48
File   : python_basic13.py
===============***===============
"""
"""
字典：以key(键)：value（值） 格式来保存一组数据{key1:value1,key2:value2,key3:value3……}
字典是可变类型，字典的键不能重复且必须是不可变类型，字典的值是任意类型，对字典的一切操作默认操作键
"""

# 1.声明一个字典
dict1 = {}  # 声明了一个字典
print(type(dict1), dict1)  # <class 'dict'> {}
# 声明一个有值的字典，注意key键不能重复
dict1 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}
print(dict1)  # {'name': 'xiaohua', 'age': 18, 'sex': '女'}

# 2.通过key获取value
# 方式一：
print(dict1.get('name'))  # name键对应的值 xiaohua
# 方式二：
print(dict1['name'])  # xiaohua
# 方法三：
print(dict1.setdefault('name'))
print(dict1.setdefault('nex'))  # 与get函数不同，当key不存在时，会默认添加一个可以加入到字典中
print(dict1)
# 3.通过key修改值，把年龄修改为25
dict1['age'] = 25
print(dict1)  # {'name': 'xiaohua', 'age': 25, 'sex': '女'}

# 4.增加键值对
dict1['class'] = 30
print(dict1)  # {'name': 'xiaohua', 'age': 25, 'sex': '女', 'class': 30}
dict1.update({'hobby': 'coding', 'phone': '110'})
print(dict1)  # {'name': 'xiaohua', 'age': 25, 'sex': '女', 'class': 30, 'hobby': 'coding', 'phone': '110'}

# 5.删除键值对，根据key删除value
dict1.pop('hobby')
print(dict1)  # {'name': 'xiaohua', 'age': 25, 'sex': '女', 'class': 30, 'phone': '110'}

#  字典的其他知识点
# 字典的键不能重复且必须是不可变类型，字典的值是任意类型，对字典的一切操作默认操作键
dict1 = {1: [1, 2, 3], (1, 2, 3): (4, 5, 6), '3': 'xiaohua'}
print(dict1)  # {1: [1, 2, 3], (1, 2, 3): (4, 5, 6), '3': 'xiaohua'}
print(dict1[1])  # [1, 2, 3]

dict1 = {'name': 'xiaohua', 'age': 18, 'sex': '女'}
# 获取字典所有的键
print(list(dict1.keys()))  # ['name', 'age', 'sex']
# 获取字典所有的值
print(list(dict1.values()))  # ['xiaohua', 18, '女']
# 获取键值对，重点：他是把每个键值对打包成元组返回
print(list(dict1.items()))  # [('name', 'xiaohua'), ('age', 18), ('sex', '女')]

class1 = {"张三": 11, "李四": 12, "王二": 13, "马五": 15, "刘大": 18}

for i in sorted(class1.keys()):  # sorted函数可以为字典里面的键与值排序
    print(i)
    print(class1[i])

# fromkeys()函数在字典中的应用
lst001 = ['a', 'b', 'c']
lis_dict = dict.fromkeys(lst001)  # 将列表里面的值边为key,value默认为None也可以自定义
print(lis_dict)
tupl001 = (1, 2, 3)
tup_dict2 = dict.fromkeys(tupl001, "a")
print(tup_dict2)
