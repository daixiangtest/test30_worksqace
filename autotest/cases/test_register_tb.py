"""
===============***===============
Auther : Lee
Date   : 2022-11-25 - 11:00
File   : test_register_tb.py
===============***===============
"""
import os

import allure
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.dbutils import DBUtils
from autotest_03.comms.log_utils import logger
from autotest_03.comms.ptrhon_xfj import get_yaml_data


@pytest.mark.T2
@allure.epic('第六天的测试')
@allure.feature('注册测试')
class Test_Register_Tb:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'register_tb.yaml'))
    ids = [case['case_title'] for case in cases]
    db = DBUtils()
    db.cud(
        'delete from tb_user where name="hehe678" or name="dx12345" or phone="15352633452" or phone="13825699883" or email="986631321@qq.com"')
    db.close()

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_register(self, case):
        response = requests.post(url=case['url'], data=case['case_data'])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        try:
            if case["expect"] in res['msg'] and '注册成功' in res['msg']:
                db = DBUtils()
                count = db.find_count("select * from tb_user where name='hehe678'")
                db.close()
                assert count >= 1
            else:
                assert case["expect"] in res['msg']
        except Exception as e:
            logger.error('断言失败，期望结果为:{},实际结果为{}'.format(case['expect'], res))
            logger.exception(e)
            raise e  # 处理异常后需要手动提起异常否则测试报告会默认通过
        else:
            logger.info('运行成功，测试编号为{}'.format(case['case_id']))


if __name__ == '__main__':
    pytest.main([__file__])
