"""
===============***===============
Auther : Lee
Date   : 2022-11-16 - 17:42
File   : python_senior12.py
===============***===============
"""
import requests
import json

"""
json.dumps()  把python中的字典类型的数据转换为json格式
json.loads() 把json格式的数据转换为python中的字典类型的数据
json.dums()  和  json.loads 都是对文件流数据的处理
"""
"""
requests怎么发起请求体为json格式的请求
"""

# 方式1，使用json.dumps()把字典数据转换为json,然后再请求头中声明请求参数代码为：connect-type:application/json
# response = requests.post(url='http://127.0.0.1:6666/business/regist_json',
#                          data=json.dumps({'username': 'liuyifei',  # 把python中的字典类型转换为json格式
#                                           'password': 'a123456',
#                                           're_password': 'a123456',
#                                           'phone': '18610055566',
#                                           'sex': '',
#                                           'birthday': '',
#                                           'qq': '',
#                                           'email': ''}),
#                          headers={'Content-Type': 'application/json'})  # 声明请求头的内容应用为json的格式
# res = response.json()  # 响应数据为json格式
# print(res)  # {'code': 1000, 'msg': '注册成功'}

# 方式二，直接使用json传参
response = requests.post(url='http://127.0.0.1:6666/business/regist_json',
                         json={'username': 'liyeye',  # 直接以json声明入参
                               'password': 'dsx12564',
                               're_password': 'dsx12564',
                               'phone': '15658965816',
                               'sex': '',
                               'birthday': '',
                               'qq': '',
                               'email': ''})
res = response.json()  # 声明响应数据数据为json
print(res)  # {'code': 1000, 'msg': '注册成功'}
