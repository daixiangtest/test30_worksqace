"""
===============***===============
Auther : Lee
Date   : 2022-11-16 - 20:19
File   : python_senior14.py
===============***===============
"""
import requests

"""
使用requests调用senior鉴权接口
"""

# 1.先创建一个session对象，然后使用senssion对象发起请求
session = requests.session()  # 创建一个session鉴权请求对象
response = session.post(url='http://127.0.0.1:6666/business/session_login',
                        data={'username': 'AutoTrue',
                              'password': 'AutoTrue',
                              'typeId': '101'})
res = response.json()
print(res)  # {'code': 1000, 'msg': '登录成功'}

# 2.在使用session对象访问session鉴权的接口
response=session.post(url='http://127.0.0.1:6666/business/session_goodsInfo',
                      data={'goodsId':'',
                            'isOnSale':'',
                            'isPromote':''})
res=response.json()
print(res)

print(session.cookies.values())   #查看cookie