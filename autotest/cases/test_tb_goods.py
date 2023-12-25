"""
===============***===============
Auther : Lee
Date   : 2022-11-24 - 20:54
File   : test_tb_goods.py
===============***===============
"""
import os

import allure
import pytest
import requests

from autotest_03.comms.constants import DATA_DIR
from autotest_03.comms.dbutils import DBUtils
from autotest_03.comms.log_utils import logger
from autotest_03.comms.ptrhon_xfj import login_token, get_yaml_data


@pytest.mark.T2
@allure.epic('第五天的测试')
@allure.feature('商品录入接口')
class Test_Tb_Goods:
    tk = login_token()
    cases = get_yaml_data(os.path.join(DATA_DIR, 'tb_goods.yaml'))
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_tb_order(self, case):
        if 'tkk&' in case['case_data'].values():
            case['case_data']['token'] = self.tk
        print(case, '**' * 20)
        response = requests.post(url=case['url'], data=case['case_data'])
        allure.dynamic.title(case['case_title'])
        res = response.json()

        if '商品录入成功' == res['msg'] and case['expect'] in res['msg']:
            db = DBUtils()
            count = db.find_count('select * from tb_goods where goodsTypeId=%s and goodsName=%s',
                                  (case['case_data']['goodsTypeId'], case['case_data']['goodsName']))
            assert count >= 1
            db.cud("delete from tb_goods where goodsTypeId=%s and goodsName=%s",
                   (case['case_data']['goodsTypeId'], case['case_data']['goodsName']))
        else:
            assert case['expect'] in res['msg']


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
