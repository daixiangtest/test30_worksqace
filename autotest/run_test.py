"""
===============***===============
Auther : Lee
Date   : 2022-11-18 - 16:30
File   : run_test.py
===============***===============
"""
import os

import pytest

from comms.constants import CASE_DIR

"""
使用allure生成测试报告
    1.使用allure生成测试报告
    1.https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/  官网下载allure的zip压缩包
    2.解压到tools目录下,如: D:\tools\allure-2.17.0
    3.添加allure的bin目录到path环境变量中
    4.打开cmd输入allure --version 验证是否安装配置成功
    5.pip install allure-pytest,安装pytest框架的allure插件
    6.重启pycharm!!!

"""

if __name__ == '__main__':
    # 在当前目录下的report目录下allure_json目录下生成test_login.py模块测试用例的结果，并且每次清除上一次的执行结果
    pytest.main(["--alluredir", './reports/allure_json', '--clean-alluredir', CASE_DIR, '-m T2'])
    os.system("allure generate ./reports/allure_json -o ./reports/allure_html --clean")
