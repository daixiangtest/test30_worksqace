"""
===============***===============
Auther : Lee
Date   : 2022-11-16 - 20:33
File   : python_senior15.py
===============***===============
"""
import requests

"""
测试自己写的接口
"""
# 正确流程
response = requests.post(url='http://127.0.0.1:5000/sign',
                         data={'username': 'hbcd123',
                               'password': 'hbcd123'})
res = response.json()
print(res)

# 2.用户名不能为空
response = requests.post(url='http://127.0.0.1:5000/sign',
                         data={'username': '',
                               'password': 'hbcd123'})
rse = response.json()
print(rse)

# 3.密码不能为空
response = requests.post(url='http://127.0.0.1:5000/sign',
                         data={'username': 'hbcd123',
                               'password': ''})
res = response.json()
print(res)  # {'code': 1004, 'msg': '密码输入不能为空!'}

# 4.用户名不存在
response = requests.post(url='http://127.0.0.1:5000/sign',
                         data={'username': 'hbcd12335',
                               'password': '25645'})
res = response.json()
print(res)  # {'code': 1005, 'msg': '用户名不存在!'}

# 密码错误
ress = requests.post(url='http://127.0.0.1:5000/sign',
                     data={'username': 'hbcd123',
                           'password': '125'})
res = ress.text
print(res)  # {'code': 1006, 'msg': '密码错误!'}
