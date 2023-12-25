"""
===============***===============
Auther : Lee
Date   : 2022-11-21 - 16:14
File   : log01.py
===============***===============
"""
"""
log可以使用文件 记录 日志
日志的级别

debug:记录详细信息，主要用来调试
info：记录正确情况下的日志
warning：记录警告日志
error：记录错误日志
"""

# 导入python自带的logging
import logging

# 第二部：创建日志对象
logger = logging.getLogger()
logger.setLevel('DEBUG')  # 设置默认的日志级别

# 第三步：设置输出方向和日志级别
sh1 = logging.FileHandler(filename="./logs/info.log", mode='a', encoding='utf-8')  # 设置输入的内容到文件地址，添加的格式，以及编码格式
sh1.setLevel('INFO')  # 设置该文件记录 INFO及以后的所有日志

sh2 = logging.FileHandler(filename='./logs/error.log', mode='a', encoding='utf-8')
sh2.setLevel('ERROR')  # 括号中的级别名需要大写

# 第四步 创建对象与处理器关联
logger.addHandler(sh1)
logger.addHandler(sh2)

# 设置输出格式
my_fml = logging.Formatter('%(asctime)s-[%(filename)s -%(lineno)s]-%(levelname)s:%(message)s')
sh1.setFormatter(my_fml)
sh2.setFormatter(my_fml)

logger.info('123')

