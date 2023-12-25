"""
===============***===============
Auther : Lee
Date   : 2022-11-28 - 16:05
File   : test_session_goodsInfo.py
===============***===============
"""
import os
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.ptrhon_xfj import get_yaml_data


class Test_Session_Goods:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'session_goodsinfo.yaml'))
    ids = [case['case_title'] for case in cases]

    @pytest.mark.parametrize("case", cases, ids=ids)
    def test_session_login(self, case):
        session = requests.session()
        response = session.post(url='http://127.0.0.1:6666/business/session_login',
                                data={"username": "AutoTrue", "password": "AutoTrue", "typeId": "101"})
        if case['case_id'] == 2:
            response = requests.post(url=case['url'], data=case['case_data'])
            res = response.json()
            assert case['expect'] in res['msg']
        else:
            response = session.post(url=case['url'], data=case['case_data'])
            res = response.json()
            assert case['expect'] in res['msg']


if __name__ == '__main__':
    pytest.main([__file__])
