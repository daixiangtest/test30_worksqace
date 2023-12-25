"""
===============***===============
Auther : Lee
Date   : 2022-11-28 - 15:46
File   : test_session_login.py
===============***===============
"""
import os
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.ptrhon_xfj import get_yaml_data


class Test_Session_Login:
    cases = get_yaml_data(os.path.join(DATA_DIR, 'session_login.yaml'))
    ids = [case['case_title'] for case in cases]

    @pytest.mark.parametrize("case", cases, ids=ids)
    def test_session_login(self, case):
        session = requests.session()
        response = requests.post(url=case['url'],data=case['case_data'])
        res = response.json()
        assert res == case['expect']
        return session


if __name__ == '__main__':
    pytest.main([__file__])
