"""
===============***===============
Auther : Lee
Date   : 2022-11-03 - 18:34
File   : python_basic17.py
===============***===============
"""
"""
本章讲解
"""

"""
条件判断分为单分支语句，双分支语句，多分支语句

单分支语句法：
if 条件：
    语句块
如果条件成立则执行语句块，否则不执行语句块
"""

# case2 优化
date = input('请输入今天是星期几：\n')
if date in ('周五', '星期五', '礼拜五', '五', '5', 'Friday'):
    print('明天不用上课了，去hign')

# 模oracle登录
name = input('请输入用户名:\n')
password = input('请输入密码:\n')

if name == 'scott' and password == '1234':
    print('恭喜您登录成功')
else:
    print('用户名或密码错误，请重新输入')

"""
双分支语法：
     语句块1
else：
    语句块2
如果条件成立执行语句块1，不成立则执行语句块2

"""

# case1:如果今天天气好,我就郊游,其他情况就学习
weather = input("请输入 今天的天气:\n")
if weather == '好':
    print("去郊游吧")
    print("好开心啊")
else:
    print("在家沉浸在知识的海洋中")

# case2: 如果今天是周五,明天就不用上课了,其他情况好好上课
date = input('请输入今天是星期几：\n')
if date in ('周五', '星期五', '礼拜五', '五', '5', 'Friday'):
    print('明天不用上课')
else:
    print('好好学习')

# 练习: 用户输入一个年份,判断是否为闰年(能被4整除,但不能被100整除,或者能被400整除是世纪闰年)
years = input('请输入年份')
if (int(years) % 4 == 0 or int(years) % 400) == 0 and (int(years) % 100) == False:
    print('闰年')
else:
    print('不是闰年')

print(int(years) % 100)

# 模拟注册,要求用户名不能重复注册,注册成功后,把数据添加到user_dict字典中
user_dict = {"xiaohua": '123456', "xiaolan": "1234", "xiaoliu": "112233"}  # 已存在的用户

name = input('请输入您的姓名')
password = input('请输入用户名')
if name in user_dict:
    print('用户名已经注册')
else:
    user_dict[name] = password
print(user_dict)
