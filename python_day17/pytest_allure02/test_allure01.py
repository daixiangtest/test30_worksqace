"""
===============***===============
Auther : Lee
Date   : 2022-11-18 - 16:59
File   : test_allure01.py
===============***===============
"""
import pytest
import os
import allure

"""
使用allure生成测试报告
    1.https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/  官网下载allure的zip压缩包
    2.解压到tools目录下,如: D:\tools\allure-2.17.0
    3.添加allure的bin目录到path环境变量中
    4.打开cmd输入allure --version 验证是否安装配置成功
    5.pip install allure-pytest,安装pytest框架的allure插件
    6.重启pycharm!!!
"""


@allure.suite("[suite] 这是测试套件层的分级")
@allure.epic("[epic] 这是史诗层的分级")
class TestDemo:

    @allure.feature("[feature] 这是功能层的分级")
    @allure.story("[story] 这是用户故事层的分级")
    @allure.title("这是一个测试用例标题!")
    @allure.description("这是一个完美的case")
    def test01(self):
        allure.dynamic.title("这是动态的标题,优先级高!")
        pass

    @allure.feature("[feature] 功能层分级02")
    @allure.story("[story] 用户故事层的分级02")
    def test02(self):
        with allure.step("这是开始执行步骤一:"):
            pass
        with allure.step("这是开始执行步骤二:"):
            pass
        with allure.step("这是开始执行步骤三:"):
            pass


if __name__ == '__main__':
    pytest.main(["--alluredir", "./report/allure_json", "--clean-alluredir", "./test_allure01.py"])
    os.system("allure generate ./report/allure_json -o ./report/allure_html --clean")
