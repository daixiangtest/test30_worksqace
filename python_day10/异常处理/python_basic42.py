"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 18:48
File   : python_basic42.py
===============***===============
"""
"""
异常处理
try:
    语句块1
except  异常类型1：
    语句块2
except 异常类型2：
    语句块3

[else:]else可选择内容，如果语句块1没有异常，则执行else的语句块
[finally：]finally也是可选内容，不管语句块1有没有出现异常，都会执行finally的语句块
"""
# try处理异常的目的是当一个模块中有多个代码运行，当其中一个代码出现问题时为了不影响其他代码的运行我们需要通过try来处理一些异常情况
try:
    num = int(input('请输入整数'))
    print(100 / num)
except ValueError:  # 只要出现了值异常就执行语句块
    print('请输入正确的数字')
else:
    print('没有出现异常')  # 没有出现异常执行else语句块
finally:
    print('程序执行完成')  # 不管有没有异常都会执行finally的语句块

"""分别处理多种异常"""
try:
    num = int(input('请输入一个整数'))
    print(100 / num)
except ValueError:  # 只要出现了值异常就执行语句块
    print('请输入正确的数字')
except ZeroDivisionError:
    print('请输入0以外的整数')  # 出现了除0的异常拦截
else:
    print('没有出现异常')  # 没有出现异常执行else语句块
finally:
    print('程序执行完成')  # 不管有没有异常都会执行finally的语句块

"""万能的异常处理方式"""
try:
    num = int(input("请输入一个整数"))
    print(100 / num)
except Exception as e:  # 只要出现了异常就执行finally的语句块
    print('请输入正确的数字', e)  # e是报错原因
