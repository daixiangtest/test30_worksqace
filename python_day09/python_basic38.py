"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 14:01
File   : python_basic38.py
===============***===============
"""
"""
多继承：一个派生类可以继承多个基类
多继承的情况下，子类会出现在自己类中去寻找需要的内容，找不到再去父类中找
"""


class Father(object):
    def fun1(self):
        print('这是父类')


class Mother:
    def fun1(self):
        print('这是母类')


class Bady(Mother, Father):
    def fun1(self):
        print("这是宝贝类")


by1 = Bady()
by1.fun1()
print(Bady.__mro__)  # 查看方法解析顺序


# 菱形继承
class A:
    def fun2(self):
        print("From A")


class B(A):
    def fun2(self):
        print('From B')


class C(A):
    def fun2(self):
        print('From C')


class D(B, C):
    def fun2(self):
        print('From D')


dd = D()
dd.fun2()  # D B C A O
print(D.__mro__)


# 钻石继承
class A:
    def fun2(self):
        print("From A")


class B(A):
    def fun2(self):
        print("From B")


class C(A):
    def fun2(self):
        print("From C")


class D(B):
    def fun2(self):
        print('From D')


class E(C):
    def fun2(self):
        print("From E")


class F(D, E):
    def fun2(self):
        print('From F')


ff = F()
ff.fun2()  # F D B E C A O    #继承搜索的顺序是先找自己的，自己没有就找父类的，父类的顺序从左到右去找，没有则找超类
print(F.__mro__)

