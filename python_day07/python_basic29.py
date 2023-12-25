"""
===============***===============
Auther : Lee
Date   : 2022-11-08 - 13:58
File   : python_basic29.py
===============***===============
"""
"""
函数参数的定义：
1.必须参数（位置参数） 2.默认参数 3.不定长参数（可变参数） 4.关键字参数
"""


# 1.必须参数（位置参数）：入参按照位置传递值，在调用函数时，入参的个数必需和传参的个数一致
def fun1(a, b, c):
    return a + b + c


print(fun1(10, 20, 30))  # 60 默认按位置赋值，把10，20，30分别赋值给了a,b,c
print(fun1(b=50, c=60, a=100))  # 210


# 2.默认参数：可以在声明函数的时候给入参设置默认值，默认参数的值在声明时就固定了，后面不会被调用修改
def fun2(a, b=10):  # b 参数的默认值为10
    return a + b


print(fun2(10))  # 20 把10赋值给了a,b使用默认值
print(fun2(10, 20))  # 把10赋值给了a,b使用传入的值


# 3.不定长参数（可变参数）：可以保存0-N个入参，一般使用*args来表示，调用该方法时如果传入多个参数会自动组包成元组
def fun3(*args):
    print('入参是：', args)


fun3()  # 入参是：（）
fun3(10)  # 入参是：（10，）
fun3(10, 20, 30, 0, 100)  # 入参是：（10，20，30，0，100）


# 定义一个函数，可以输入任意多个整数，返回他们的和
def fun4(*args):
    sm = 0
    for i in args:
        sm += i
    return sm


print(fun4(1, 2, 3, 4, 5, 6, 7, 8, 9))  # 45
print(fun4())  # 0


# 4.关键字参数，用来接收key_value格式的入参，保存成一个字典
def fun5(**kwargs):
    print('入参是：', kwargs)


fun5(a=1, b=2, c=3)  # 入参是：{'a':1, 'b':2,'c':3}  #入参一般是键=值的格式
fun5(name='xiaohua', age=18, sex='女', sal=15000)  # 入参是：{'name':'xiaohua','age':18,'sex':'女','sal':15000}


# 多种参数混合使用
# 1.必须参数（位置参数） 2.默认参数 3.不定长参数（可变参数） 4.关键字参数
def fun6(x, y=5, z=6, *args, **kwargs):
    print(" x的值是{}, y的值是{}, z的值是{} , args的值是{}, kwargs的值是{}".format(x, y, z, args, kwargs))


# fun6() # TypeError: fun6() missing 1 required positional argument: 'X
fun6(10)  # x的值是10, y的值是5, z的值是6 , args的值是(), kwargs的值是{}
fun6(1, 2, 3)  # x的值是1, y的值是2, z的值是3 , args的值是(), kwargs的值是{}
fun6((1, 2), 3)  # x的值是(1, 2), y的值是3, z的值是6 , args的值是(), kwargs的值是{}
fun6(1, 2, 3, 4, (5, 6))  # x的值是1, y的值是2, z的值是3 , args的值是(4, (5, 6)), kwargs的值是{}
fun6(4, 5, 6, num=1)  # x的值是4, y的值是5, z的值是6 , args的值是(), kwargs的值是{'num': 1}
