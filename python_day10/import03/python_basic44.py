"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 20:04
File   : python_basic44.py
===============***===============
"""
import python_day10.import03.login_register as lr

"""
模块导入：当前模块导入其他模块的内容，我们就可以使用其他模块的变量，函数，类...

模块导入方式一：
导入整个模块：import 包名.模块名 as 别名
"""

print(lr.user)  # {'username': 'xiaohua', 'password': 'a123456'}
print(lr.login('xiaohuaa', 'a1323456'))  # {'code': 1003, 'msg': '用户名或密码错误'}
print(lr.register('xiaolan', '123456', '123456'))  # {'code': 9999, 'msg': '注册成功'}
print(lr.__name__)  # python_day10.import03.login_register   展示的是引入包的路径
print(__name__)  # __main__   展示的是本模板对自己的自称
