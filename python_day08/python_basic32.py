"""
===============***===============
Auther : Lee
Date   : 2022-11-09 - 11:54
File   : python_basic32.py
===============***===============
"""

"""
面对对象：一切皆对象，面向对象是一个编程思想，好处是利用面向对象的思想好实现业务
什么是类？
    1.类是对一类事物的描述
    2.类中包含属性和方法，属性就是变量，方法就是函数
什么是对象？
    对象是类的具体实例，对象能调用类的属性和方法
对象和类的关系？
    一个类可以有无数个对象
简单的说我们可以把一类操作放在一个类中，以后对象调用方便
"""


# 创建一个类
class Cat:
    color = ''
    name = ''
    sex = ''
    age = ''

    def eat(self, food):
        print('{}很好吃！'.format(food))

    def sleep(self):
        print('一天能睡十几个小时!')

    def play(self, thing):
        print('{}真好玩！'.format(thing))


# 创建实例对象
one = Cat()  # 必须要有括号
two = Cat()  # 创建了Cat类的试例对象，一只具体的猫
three = Cat

# 给对象的属性赋值
one.name = 'Tom'
one.color = 'blue'
one.age = 3
one.sex = 'male'
print(one.name, one.age, one.sex)  # Tom  3  male
one.age = 83
print(one.name, one.age, one.sex)  # Tom  83  male

# 对象调用方法
one.eat('牛排')  # 牛排很好吃
one.sleep()  # 一天能睡十几个小时
one.play('Jerry')  # Jerry真好玩

two.eat('腥味的东西')  # 腥味的东西很好吃
two.sleep()  # 一天能睡十几个小时

# 定义一个类，声明属性和方法，创建该类的实例对象，并且为对象调用方法
class House:
    style = ''
    area = ''
    seat = ''
    ownership = ''

    def live(self, type):
        print(type)

    def function(self, use):
        print('可以用来使用')

    def price(self, money):
        print("市场价格是：", money)


one = House()
two = House()
there = House()

one.style = '中国古典风'
one.area = '北京'
one.seat = '天安门广场'
one.owneiship = '住宅'

print(one.style, one.area)

one.live('宫殿')
one.function('居住')
one.price('10000000￥')

two.live('别墅')
two.function('居住')
one.price('10000000￥')