"""
===============***===============
Auther : Lee
Date   : 2022-11-16 - 17:44
File   : python_senior13.py
===============***===============
"""
import requests

"""
requests怎么模拟接口关联
接口关联：一个接口的出参是另外一个接口的入参
"""
# 1.先进行登录
response = requests.post(url='http://127.0.0.1:6666/business/token_login',
                         data={'username': 'hbcd123',
                               'password': 'hbcd123',
                               'typeId': '101'})

res = response.json()
print(res)  # {'code': 1000, 'msg': '登录成功',}
tk = res['token']  # MTY2ODYyOTUyNy4yMTg0NzU6MWE5ZmZlNDc5NWQzNmU0ZDMyMDUzZmQ4ZmQxMTMyZjhmMjdkM2I0Yw==

# 2引用变量
response = requests.post(url='http://127.0.0.1:6666/business/token_goodsInfo',
                         data={'token': tk,
                               'goodsId': '',
                               'isOnSale': '',
                               'isPromote': ''})
res = response.json()
print(res)

response=requests.get(url='http://127.0.0.1:6666/business/token_goodsInfo?token=%s&goodsId=&isOnSale=&isPromote='%tk)
res=response.json()
print(res)