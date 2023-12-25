"""
===============***===============
Auther : Lee
Date   : 2022-11-28 - 17:26
File   : test_regist_json.py
===============***===============
"""
import os

import allure
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.dbutils import DBUtils
from autotest_03.comms.ptrhon_xfj import get_yaml_data

@pytest.mark.T3
@allure.epic("第九天测试")
@allure.title("登录测试")
class Test_Regist_Json:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'regist_json.yaml'))
    ids = [case['case_title'] for case in cases]
    db=DBUtils()
    db.cud('delete from tb_user where name="xiaobai1"')

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_regist_json(self, case):
        response = requests.post(url=case['url'], json=case['case_data'])
        allure.title(case['case_title'])
        res = response.json()
        assert case['expect'] in res['msg']


if __name__ == '__main__':
    pytest.main([__file__])
