"""
===============***===============
Auther : Lee
Date   : 2022-11-10 - 20:14
File   : python_basic45.py
===============***===============
"""
from python_day10.import03.login_register import user, login

# from day10.import.login_register import * # 引入指定模块的所有内容，不推荐

"""
模块导入：当前模块导入其他模块的内容，我们就可以使用其他模块的变量，函数，类...

模块导入方式二：
导入其他模块内容，这种方式用什么，拿什么：from 包名.模块名 import 函数1，函数2，变量1.....
"""
print(user)  # {'username': 'xiaohua', 'password': 'a123456'}
print(login('xiaohua', 'a123456'))  # {'code': 9999, 'msg': '登录成功'}
