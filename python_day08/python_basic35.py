"""
===============***===============
Auther : Lee
Date   : 2022-11-09 - 21:26
File   : python_basic35.py
===============***===============
"""
"""
魔法方法:在某些情况下自动触发调用的方法,就是python解释器的默认行为
__new__():创建对象时自动调用,负责把当前类的对象new出来
__init__(): 构造方法,在__new__()之后被调用,负责初始化实例对象
__del__(): 会在删除对象时自动调用

魔法方法中的__ init__ () 方法会在初始化对象是自动调用,我们可以利用该特性在创建实例对象完成一些操作
一般写一个类, 如果不声明__init__() 构造方法会自动使用默认的,默认的构造方法一般不显示，同时也没有特殊操作,
注意:一个类中不能有多个__init__()方法
"""


class Emp:
    # def__init__(self): #新建Emp类实例对象时,会自动触发构造方法的调用,我们重写构造方法向控制台输出了一一个字符串
    # print("构造方法被调用! ")
    def __init__(self, emp_no, emp_name, emp_sal):
        # 重写了Emp类的构造方法,在新建Emp类的实例对象时必须要传3了个参数,并且分别赋值给当前绑定对象的实例属性
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.emp_sal = emp_sal

    def __del__(self):  # 当我们重写了__del__()方法，在使用del删除时会自动触发调用，完成我们的预期操作
        print('有对象被删除')


# emp01=Emp()  #新建Emp类的实例对象
emp02 = Emp(1001, 'scott', 5000)  # 当我们重写了构造方法，必须要按照我们重写后的要求传参才可以新建实例对象

print(emp02.emp_no, emp02.emp_name, emp02.emp_sal)  # 1001 scott 5000

emp03 = Emp(1002, 'xiaohua', 15000)
print(emp03.emp_no, emp03.emp_name, emp03.emp_sal)  # 1002 xiaohua 15000

# del  emp02,emp03 #万物皆可del,从内存中释放

print('hello')

print(isinstance(123, int))  # True   判定 123 是否是整数类型 返回值是布尔类型
print(isinstance(emp02, Emp))  # True  判定 emp02是否属于Emp, 返回值是布尔类型
print(type(123))  # <class 'int'>

# 当前模块执行完成后,会释放当前模块所占用的内存空间,垃圾自动回收机制也会触发我们重写后的__ del__ () 方法
