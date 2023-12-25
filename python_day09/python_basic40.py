"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 18:36
File   : python_basic40.py
===============***===============
"""
"""
方法重写/方法覆盖：子类继承父类，子类和父类具有相同的方法，子类重写了父类的方法
"""


class Animal:
    def run(self):
        print('这是父类的run方法')


class Pig(Animal):
    def run(self):
        print('这是子类的run方法')


am1 = Animal()
am1.run()  # 这是父类的run方法

pp = Pig()
pp.run()  # 这是子类的run方法

# 多态：子类调用父类的重写的方法
super(Pig, pp).run()  # 这是父类的run方法 代表子类的实例对象pp调用的是父类的run方法
# super(子类名,子类实例对象）.父类的方法
