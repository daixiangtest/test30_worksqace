"""
===============***===============
Auther : Lee
Date   : 2022-11-16 - 17:43
File   : homwork.py
===============***===============
"""
import requests

"""
resquests 用来模拟HTTP请求
为什么要学习resquests库，因为我们要脱离工具的测试，改成使用代码调用接口进行测试
"""

# 案例1 百度一下
# response = requests.get(url='https://www.baidu.com/s?wd=宇宙职业选手')  # get请求入参
# res = response.text  # 响应数据参数为文本格式
# print(type(res), res)  # <class 'str'>

# 案列2调用自己的接口
# response = requests.get(url="http://127.0.0.1:5000/sign?username=大脚&password=sss8888")  # json格式入参
# res = response.json()  # 响应数据参数为json格式
# print(type(res), res)  # <class 'dict'> {'code': 1007, 'msg': '登录成功!'}

response = requests.post(url="http://127.0.0.1:5800/tianmao",
                         data={'username': 'xianwan',
                               'psw': 'dx12345',
                               're_psw': 'dx12345',
                               'phone': '18556988523',
                               'email': '98546@qq.com'})
res = response.json()
print(type(res), res)  # <class 'dict'> {'code': 1016, 'msg': '登录成功!'}
