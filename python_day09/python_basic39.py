"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 16:10
File   : python_basic39.py
===============***===============
"""
"""
封装：
第一层的封装：就是把某一类操作写在一个类中，供以后调用，就是封装
第二层的封装：类中把某些属性和方法隐藏起来（或者说定义为私有），只能在类的内部使用，外部无法访问，或者留下少量的函数供外部去访问
"""

# 怎么形容小花这个学生
name = 'xiaohua'
age = 18
sex = '女'


# 声明三个变量去形容一个学生 有什么弊端？
# 弊端：很零散，不能重复使用，如果学生多了则需要不断的新建变量去描述

class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.aex = sex


one = Student('xiaohua', 18, '女')
two = Student('xiaolan', 20, '女')

print(one.name, one.age)  # xiaohua 18


# 第二层面的封装，控制访问权限
# 我们可以把属性私有，不在允许对象访问
class Stu:
    def __init__(self, name, age, sex):
        self.__name = name  # __name 代表把属性私有化
        self.__age = age
        self.__sex = sex


three = Stu('xiaoshuai', 33, '男')


# print(three.name)    #把属性变为私有，外部无法访问AttributeError:name 'one' is not defined

# 那么问题来了，现在我们又想通过某种我们允许的方式访问修改
class Stu1:
    def __init__(self, name, age, sex):
        self.__name = name  # 私有的类属性中无法直接通过实例对象去掉调用，但是可以通过定义实例方法来调用出类中的私有属性
        self.__age = age
        self.__sex = sex

    def get_name(self):  # 允许你通过对象访问name属性
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age  # 允许你通过对象修改age属性

    def get_sex(self):
        return self.__sex


four = Stu1('xiaoxu', 28, '男')
print(four.get_name(), four.get_age(), four.get_sex())  # xiaoxu 28 男
four.set_age(30)
print(four.get_name(), four.get_age(), four.get_sex())  # xiaoxu 30 男
