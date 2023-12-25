"""
===============***===============
Auther : Lee
Date   : 2022-11-12 - 10:47
File   : read_properties.py
===============***===============
"""
from configparser import ConfigParser

# config配置  parser解析器

"""
常见的配置文件类型：.ini .yaml .json .xml .propertise....
配置文件主要放一些固定的内容
"""

# 创建一个配置文件解析器的对象
cp = ConfigParser()

# 读取配置文件
# 绝对路径：从根目录开始的路径，比如：D/tools
# 相对路径：相对于当前文件的路径，比如：./config.ini.ini
# ./代表当前目录下../当前目录的上层目录
cp.read(r'./config.ini', encoding='utf-8')  # 读取cp这个对象的路径在config.ini这个模板下，格式默认时utf-8

name = cp.get('user', 'name')
print(name)  # xiaohua

pwd = cp.get("user", 'pwd')
print(pwd)  # 123456
print(type(pwd))  # <class 'str'>

pwd = cp.getint('user', 'pwd')  # 转化为整数类型
print(pwd, type(pwd))  # 123456 <class 'int'>

port = cp.getint('mysql', 'port')
print(port, type(port))  # 3306 <class 'int'>
