"""
===============***===============
Auther : Lee
Date   : 2022-11-22 - 15:31
File   : constants.py
===============***===============
"""
import os

"""
获取动态的地址
"""
# 获取工程的根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# D:\WorkSpace\autotest_03

# 获取测试数据目录
DATA_DIR = os.path.join(BASE_DIR, 'data')
# print(DATA_DIR)  D:\WorkSpace\autotest_03\data

# 日志输入路径
INFO_LOG = os.path.join(BASE_DIR, 'logs/info.log')
ERROR_LOG = os.path.join(BASE_DIR, 'logs/error.log')
# print(INFO_LOG,ERROR_LOG) #D:\WorkSpace\autotest_03\logs/info.log D:\WorkSpace\autotest_03\logs/error.log
# 报告输入目录
REPORT_JSON = os.path.join(BASE_DIR, 'reports/allure_json')
REPORT_HTML = os.path.join(BASE_DIR, 'reports/allure_html')

# 获取用例目录
CASE_DIR = os.path.join(BASE_DIR, 'cases')

# 获取config.ini目录
CFI = os.path.join(BASE_DIR, 'conf/config.ini')
# print(CFI) #D:\WorkSpace\autotest_03\conf/config.ini
