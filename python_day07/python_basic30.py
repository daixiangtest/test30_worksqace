"""
===============***===============
Auther : Lee
Date   : 2022-11-08 - 17:17
File   : python_basic30.py
===============***===============
"""
"""
作用域：为了编写可维护代码，我们很多代码在不同的区域当中
模块：一个.py文件称之为一个模板
"""

# 知识点1：变量的作用域：变量分为全局变量（定义在模块中，任何地方都可以访问）和局部变量（定义在函数中，只有在该函数内生效）
a = 10  # a是一个全局变量


def fun1():
    b = 20  # b是一个局部变量
    print(a)  # a可以访问，因为a是全局变量
    print(b)  # b可以访问，因为b在fun1函数内访问


fun1()  # 10,20
# print(b)  #该行代码报错，因为b属于fun1函数，在能在fun1函数内使用 NameError:name 'b' is not defined

# 知识点2：global  使用global修饰就可以在函数内使用全局变量，只有在该函数内运行过后，才会生效
c = 100  # 全局变量


def fun2():
    global c  # 当在函数内使用全局变量时，使用global修饰，以后的c就是全局变量c了
    c = 200
    print(c)


print(c)  # 100
fun2()  # 200
print(c)  # 200


# 知识点3：函数嵌套
def fun3():
    x = 10

    def fun4():
        print('这是一个内部函数')

    fun4()  # 调用fun4函数
    print(x)


fun3()


# 知识点4：nonlocal 用来修改外部嵌套函数作用域的值，nonlocal只能写在嵌套函数中
def fun5():
    y = 10

    def fun6():
        nonlocal y
        y = 100
        print(y)

    print(y)  # 10
    fun6()  # 100
    print(y)  # 100


fun5()
