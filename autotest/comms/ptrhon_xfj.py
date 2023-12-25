"""
===============***===============
Auther : Lee
Date   : 2022-11-24 - 19:25
File   : ptrhon_xfj.py
===============***===============
"""
from configparser import ConfigParser

import requests
import yaml


from autotest.comms.constants import CFI
from autotest.comms.dbutils import DBUtils


def login_token():
    respones = requests.post(url='http://127.0.0.1:6666/business/token_login',
                             data={"username": "AutoTrue", "password": "AutoTrue", "typeId": 101})
    res = respones.json()
    tk = res['token']
    return tk


def get_yaml_data(file):
    try:
        with open(file, mode='r', encoding='utf-8') as fr:
            cases = yaml.safe_load(fr)
        return cases
    except Exception as e:
        print("从yaml文件读取测试数据失败!", e)


def true_value(cases):
    db = DBUtils()
    db_user = db.find_one("select * from tb_user order by rand() limit 1")
    db_name, db_pwd = db_user[1], db_user[2]
    for case in cases:
        if 'usname' in case["case_data"].values():
            case["case_data"]["username"] = db_name
        if 'psw' in case["case_data"].values():
            case["case_data"]["password"] = db_pwd
    return cases


# 读取conf中的config.ini文件
def get_ini_data(section, option):
    try:
        cp = ConfigParser()  # 创建 解析器对象
        cp.read(CFI, encoding="utf-8")  # 加载ini文件
        return cp.get(section, option)  # 通过 标头和选项获取对应的值
    except Exception as e:
        print("从ini文件中读取数据失败", e)


if __name__ == '__main__':
    a = get_ini_data('user', 'name')
    print(a)
