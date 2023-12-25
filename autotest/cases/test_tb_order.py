"""
===============***===============
Auther : Lee
Date   : 2022-11-24 - 19:21
File   : test_tb_order.py
===============***===============
"""
import os

import allure
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.ptrhon_xfj import login_token, get_yaml_data


@pytest.mark.T2
@allure.epic('第四天的测试')
@allure.feature('订单信息查询')
class Test_Tb_Order:
    tk = login_token()
    cases = get_yaml_data(os.path.join(DATA_DIR, 'tb_order.yaml'))
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_tb_order(self, case):
        if 'tkk&' in case['case_data'].values():
            case['case_data']['token'] = self.tk
        response = requests.post(url=case['url'], data=case['case_data'])
        res = response.json()
        allure.dynamic.title(case['case_title'])
        assert case['expect'] in res['msg']


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
