"""
===============***===============
Auther : Lee
Date   : 2022-11-07 - 18:56
File   : python_basic27.py
===============***===============
"""

"""
组包/装包:通俗的说,组包就是把多个数据装在一个元组中
拆包/解包:把一组数据拆分成单个对象,比如列表、元组、字典拆成单个对象
"""

# 自动组包
tup1 = 1, 2, 3, 4, 5
print(tup1)  # (1, 2, 3, 4, 5)
print(type(tup1))  # <class 'tuple'> 任意无符号对象,以逗号隔开会自动组包成元组

teacher = '老刘', '老徐', '老王', '小李'
print(teacher, type(teacher))  # (' 老刘"，'老徐'，'老王'，'小李) <class 'tuple'>

# 自动拆包
tup1 = (1, 2, 3)
a, b, c = tup1  # 变量个数要和被拆包对象的成员个数一致
print(a, b, c)  # 1 2 3

star = ['老刘', '老徐', '老王', '小李']
print(teacher, type(teacher))  # (' 老刘"，'老徐'，'老王'，'小李) <class 'tuple'>

# 自动拆包
tup1 = (1, 2, 3)
a, b, c = tup1  # 变量个数要和被拆包对象的成员个数一致
print(a, b, c)  # 1 2 3

star = ['老刘', '老徐', '老王', '小李']
F1, F2, F3, F4 = star
print(F1, F2, F3, F4)  # 老刘老徐老王小李

dict1 = {"name": "xiaohua", "age": 18, "sex": "女"}

a, b, c = dict1  # 字典默认操作都是操作键,拆出来键
print(a, b, c)  # name age sex

a, b, c = dict1.values()  # 拆字典的值
print(a, b, c)  # xiaohua 18 女

# 手动拆包/组包
teacher = ('老李', '老徐', '老王', '小李')
print(*teacher)  # 这里*代表拆包,老刘,老徐,老王,小李

F1, *F = teacher  # 这*号代表组包,把除第一 个对象之外的成员都打包到一-个列表中
print("F1的值是:", F1)  # F1的值是:老刘
print("F的值是:", F)  # F的值是: ['老徐'， '老王'，'小李]

*F, F4 = teacher
print("F4的值是:", F4)  # F4的值是:小李
print("F的值是:", F)  # F的值是: ['老刘"，' 老徐'，'老王]

F1, *F, F4 = teacher
print("F1的值是:", F1)  # F1的值是:老刘
print("F的值是:", F)  # F的值是: ['老徐"，'老王']
print("F4的值是:", F4)  # F4的值是:小李
