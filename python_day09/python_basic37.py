"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 14:01
File   : python_basic37.py
===============***===============
"""
"""
面向对象语言的三大特征：封装继承多态
继承：派生类继承基类，派生类就可以使用基类的所有属性和方法
继承的好处：减少代码冗余，提高代码重用性
Java是单继承，python是多继承
继承的语法：在声明的时候在类名之后使用（父类1，父类2，父类3......)
"""


class Animal:
    name = ""
    age = 0
    country = ""

    def run(self):
        print("{}正在高速移动".format(self.name))

    def say(self):
        print("{}正在沟通....".format(self.name))


class Dog(Animal):
    def look_door(self):
        print("你过来就咬死你，你不过来我也咬你",self.name)


dog1 = Dog()  # 新建了Dog类的实例对象dog1
dog1.name = "富贵"
dog1.age = 10
dog1.country = 'china'
dog1.run()  # 富贵正在高速移动
dog1.say()  # 富贵正在沟通.....
dog1.look_door()  # 你过来就要死你，你不过来我也咬你

"""
子类继承父类，子类和父类都重写了构造方法，子类的构造方法类必须优先满足父类的构造方法
"""


class People:
    def __init__(self, name, age, sex):  # 父类有构造方法子类也有构造方法，子类必须优先满足父类的构造方法
        self.name = name
        self.age = age
        self.sex = sex


class Child(People):
    def __init__(self, name, age, sex, sal):
        People.__init__(self, name, age, sex)
        self.sal = sal


child01 = Child('xiaohua', 8, '女', 500)
print(child01.name, child01.age, child01.sex, child01.sal)  # xiaohua  8  女  500
