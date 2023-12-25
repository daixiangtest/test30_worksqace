"""
===============***===============
Auther : Lee
Date   : 2022-11-07 - 19:06
File   : python_basic28.py
===============***===============
"""
"""
函数:函数是一段可以重复使用的代码,比如:print()/len()/input()/max()....

函数的定义的规则:
def 函数名([参数1,参数2,参数3...]):
    函数名(你想要实现的功能代码)
    [return]代表该函数并且返回return后面的数据
"""


def add():  # 声明了一个函数,名字加add,没有入参,也没有返回值
    print('该函数被调用')


add()  # 函数调用必须要有小括号


def add1(a, b):  # 声明了一个函数,名字叫add1,需要两个入参,没有返回值
    print(a + b)


add1(10, 20)  # 30
add1('10', '20')  # 1020   调用了add1函数并且传入2个参数,把'10'赋值给a,把'20'赋值给b
add1(999, 666)  # 1665 函数可以多次调用


def add2(a, b, c):  # 声明了一个函数,名字叫add2,需要3个入参,并且返回3个参数相加
    return a + b + c


num = add2(10, 20, 30)
print(num)  # 60
print(add2(33, 66, 77))  # 176

print('===' * 50)


# 练习:设计一个函数,有两个入参(长和宽),该函数返回矩形的面积,并且调用该函数三次
def area(length, width):
    return length * width


print(area(7, 5))  # 35


# 声明一个函数,判断是奇数还是偶数,并且返回判断结果
def judge(number: int):
    if number % 2:
        return '{}是奇数'.format(number)
    else:
        return f'{number}是偶数'


print(judge(1018))  # 1018是偶数


# 函数可以返回多个值
def math(a, b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c, d, e, f  # 如果返回多个值,会自动组成一个元组


print(math(10, 20))  # (30, -10, 200, 0.5)
c, d, e, f = math(100, 200)
print(c, d, e, f)  # 300 -100 20000 0.5


# 写一个函数,模拟用户登录,参数:用户名、密码， 正确的用户名xiaohua,密码是huahua
# 如果密码错了，登录失败,如果用户名错了,返回用户不存在

def register(user, pw):
    """

    :param user:   用户名
    :param pw:     密码
    :return:      登录结果
    """
    if user == 'xiaohua':
        if pw == 'huahua':
            return '登录成功'
        if pw != 'huahua':
            return '密码错误'
    else:
        return '用户名未注册'


print(register('xiaohua', 'huahua'))  # 登录成功
