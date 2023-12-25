"""
===============***===============
Auther : Lee
Date   : 2022-11-28 - 8:16
File   : test_goods_promote.py
===============***===============
"""
import os

import allure
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.dbutils import DBUtils
from autotest_03.comms.ptrhon_xfj import login_token, get_yaml_data

@pytest.mark.T2
@allure.epic('第七天的测试')
@allure.feature('商品促销设置接口')
class Test_Good_promote:
    tk = login_token()
    cases = get_yaml_data(os.path.join(DATA_DIR, 'goods_promote.yaml'))
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_tb_order(self, case):
        if 'tkk&' in case['case_data'].values():
            case['case_data']['token'] = self.tk
        response = requests.post(url=case['url'], data=case['case_data'])
        allure.dynamic.title(case['case_title'])
        res = response.json()
        if '促销开启设置成功' == res['msg'] and case['expect'] in res['msg']:
            db = DBUtils()
            stt = db.find_one('select ispromote from tb_goods where goodsid=%s',
                              (case['case_data']['goodsId']))
            assert 0 in stt
            db.cud('update tb_goods set ispromote=%s where goodsid=%s',('1',case['case_data']['goodsId']))
            db.close()
        else:
            assert case['expect'] in res['msg']


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
