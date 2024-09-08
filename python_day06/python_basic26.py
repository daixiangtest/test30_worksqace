"""
===============***===============
Auther : Lee
Date   : 2022-11-07 - 18:39
File   : python_basic26.py
===============***===============
"""
import random

"""
randow随机数
"""

# 随机一个1-10的数字
print(random.randint(1, 10))  # randint代表的时从1到10随机随机取一个数，要求数据类型时整数类型

# 班级随机点名器
student = ['汪圣文', '黄江林', '薛龙龙', '田晗', '杨丹', '杨培斯']

print(random.choice(student))  # choice代表的时从列表中的多个值中随机抽取一值出来
print(random.choice(('s', 'c', 'b')))

# 扑克牌洗牌

pai = ['A', '1', '2', '3', '4', '5', '6', '7', 'J', 'K']
random.shuffle(pai)  # 该函数会将数组里面的元素打乱重新排序
print(pai)
