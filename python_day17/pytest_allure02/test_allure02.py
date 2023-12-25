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


@allure.suite("[suite] 这是测试套件层的分级")  # 测试套件层,最大的层级
@allure.epic("[epic] 这是史诗层的分级")  # epic层级
class TestDemo:

    @allure.feature("[feature] 这是功能层的分级")  # 功能模块层级
    @allure.story("[story] 这是用户故事层的分级")  # 用户故事层级
    @allure.title("这是一个测试用例标题!")  # title 测试用例的标题
    @allure.description("这是一个完美的case")  # description 测试用例的描述
    @allure.issue(url='https://www.baidu.com', name='缺陷地址')  # 连接对应的bug地址
    @allure.link(url='https://www.sina.com.cn', name='需求文档')  # 可以连接你想连接的地址
    @allure.severity("critical")  # 测试用例的优先级
    def test01(self):
        allure.dynamic.title("这是动态的标题,优先级高!")
        # 添加一些自定义的测试内容,注意body只可以是字符串格式
        allure.attach(body="{'name':'xiaohua','age':18,'sex':'女'}", name='请求数据')
        allure.attach(body="{'code': 1000, 'msg': '用户名或密码错误!'}", name="响应结果")
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
    pytest.main(["--alluredir", "./report/allure_json", "--clean-alluredir", "./test_allure02.py"])
    os.system("allure generate ./report/allure_json -o ./report/allure_html --clean")
    # pytest.main(['--alluredir', './report/allure_json1', '--clean-alluredir', './test_register.py'])
    # os.system('allure generate ./report/allure_json1 -o ./report/allure_html1 --clean')