"""
===============***===============
Auther : Lee
Date   : 2022-11-18 - 16:30
File   : run_test.py
===============***===============
"""
import pytest
import os

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

import pytest
import os
import allure


@allure.epic('系统登录模块')
class TestLogin:
    @allure.story('登录用例1')
    def test_login01(self):
        with allure.step('读取数据'):
            pass
        with allure.step('调用登录接口'):
            pass
        with allure.step('响应结果'):
            pass
        assert True


if __name__ == '__main__':
    # 在当前目录下的report目录下allure_json目录下生成test_login.py模块测试用例的结果，并且每次清除上一次的执行结果
    pytest.main(["--alluredir", './report/allure_json', '--clean-alluredir', './test_login.py'])
    os.system("allure generate ./report/allure_json -o ./report/allure_html --clean")
    # 当前目录下生成测试报告，对当前目录下report下的allure文件输出当前目录下的report文件包生成html格式的文件包，并且清除上一次的结果
    # pytest.main(['--alluredir', './report/allure_json1', '--clean-alluredir', './test_register.py'])
    # os.system('allure generate ./report/allure_json1 -o ./report/allure_html1 --clean')
