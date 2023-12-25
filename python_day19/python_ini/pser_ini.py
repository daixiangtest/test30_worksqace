"""
===============***===============
Auther : Lee
Date   : 2022-11-22 - 19:18
File   : pser_ini.py
===============***===============
"""
# 解析ini文件
from configparser import ConfigParser  # 导入工具类包

cp = ConfigParser()
cp.read(r'D:\WorkSpace\python_day19\python_ini\config.ini', encoding='utf-8')  # 加载ini文件
ip = cp.get('mysql', 'host')  # 通过标头和选项获取对应的值
print(ip)


# 封装
def get_ini_data(section, option):
    try:
        cp = ConfigParser()
        cp.read(r'D:\WorkSpace\python_day19\python_ini\config.ini', encoding='utf-8')
        result = cp.get(section, option)  # 通过入参的标头和选项获取对应的值
        return result
    except Exception as e:
        print('从ini文件中读取数据失败', e)


result1 = get_ini_data('user', '111')
result2 = get_ini_data('mysql', 'port')  # 注意ini文件读取的所有内容都是str类型
print(type(result1), type(result2))
