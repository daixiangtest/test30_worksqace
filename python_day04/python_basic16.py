"""
===============***===============
Auther : Lee
Date   : 2022-11-03 - 18:53
File   : python_basic16.py
===============***===============
"""
"""
本章讲解：多分支条件判断
语法：
if  条件1：
    语句块1
    elif 条件2：
    语句块2
    elif 条件3：
    语句块3
else：
    语句块4
"""
#
# #日(初生) -6岁为婴幼儿; 7-12岁为少儿; 13-17岁为青少年; 18-45岁为青年: 46-69岁为中年: 69岁及以上为老年。
# age = int(input(" 请输入您的年龄:\n"))
# if 0<=age<= 6:
#     print('婴幼儿')
# elif 7 <=age<12:
#     print('少儿阶段')
# elif 13<=age<17:
#     print('青少年阶段')
# elif 18 <=age<=45:
#     print('青年阶段')
# elif 46<=age<=69:
#     print('中年阶段')
# elif 69<age<=150:
#     print('老年阶段')
# else:
#     print('飞升阶段')

# # 练习1  BMI体质指数的计算公式是用体重（公斤）除以身高（米）的平方 根据分类判断体重标准

weight = int(input('请输入体重'))
height = int(input('请输入升高'))
bmi = weight / ((height / 100) ** 2)
print(bmi)
if bmi <= 18.4:
    print('你太瘦了，要补充营养')
elif 18.5 <= bmi <= 23.9:
    print('你的身材太完美了')
elif 24.0 <= bmi <= 27.9:
    print('你有点重了，要注意减肥')
elif 100 >= bmi >= 28.0:
    print('你太胖了，快去运动吧')
else:
    print('你流弊')

# 水仙花数: 用户输入一个数,判断是否是水仙花数,1000以内的水仙花数是指一个3位数，它的每个位上的数字的 3次幂之和等于它本身
number = input('请输入数字')
if not (number.isnumeric()):
    print('请输入纯数字')
elif int(number) <= 100:
    print('请输入3位数字')
elif len(number) != 3:
    print('请输入3位数字')
elif (int(number[0]) ** 3) + (int(number[1]) ** 3) + (int(number[2]) ** 3) == int(number):
    print(f'{number}水仙花数')
else:
    print(f'{number}是普通数字')

