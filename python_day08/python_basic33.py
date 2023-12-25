"""
===============***===============
Auther : Lee
Date   : 2022-11-09 - 19:55
File   : python_basic33.py
===============***===============
"""
"""
self代表当前对象，谁调用就代表谁
"""


class Student:
    name = ''  # 类属性
    age = 0
    sex = ''
    stu_id = 1000

    def study(self):
        print('{}正在学习python,并说了一句python真简单!'.format(self.name))

    def sleep(self):
        print("12点前在{}宿舍睡觉,早睡早起身体棒棒!".format(self.sex))


stu01 = Student()  # 创建了Student类的实例对象stu01
stu01.stu_id = 1001  # 给实例对象赋值
stu01.name = 'xiaohua'
stu01.sex = '女'

stu01.study()  # xiaohua正在学习python,并说了一句python真简单!
stu01.sleep()  # 12点前在女宿舍睡觉,早睡早起身体棒棒!
print(stu01.age)  # 0 当实例对象没有赋值时，则是使用类属性默认的值
stu01.age = 18  # 给属于实例对象的实例赋值
print(stu01.age)  # 18
stu01.class_id = 30
print(stu01.class_id)

stu02 = Student()  # 当新键的实例对象没有赋值时输出默认的类属性值
print(stu02.age)  # 0
stu02.study()  # 正在学习python,并说了一句python真简单!
