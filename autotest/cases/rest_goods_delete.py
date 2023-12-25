"""
===============***===============
Auther : Lee
Date   : 2022-11-28 - 13:55
File   : rest_goods_delete.py
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
@allure.epic('第八天的测试')
@allure.feature('商品促销设置接口')
class Test_Good_promote:
    tk = login_token()
    cases = get_yaml_data(os.path.join(DATA_DIR, 'goods_delete.yaml'))
    ids = ['测试{}'.format(case['case_title']) for case in cases]

    @pytest.mark.parametrize('case', cases, ids=ids)
    def test_tb_order(self, case):
        db = DBUtils()
        db.cud('insert into tb_goods (goodsId,goodsName,num,isonsale) values (100012,"自行车1",20000,1)')
        if 'tkk&' in case['case_data'].values():
            case['case_data']['token'] = self.tk
        response = requests.post(url=case['url'], data=case['case_data'])
        res = response.json()
        if '商品删除成功' == res['msg'] and case['expect'] in res['msg']:
            db = DBUtils()
            stt = db.find_count('select * from tb_goods where goodsid=%s',
                              (case['case_data']['goodsId']))
            db.close()
            assert stt ==0
        else:
            assert case['expect'] in res['msg']
            db=DBUtils()
            db.cud('delete from tb_goods where goodsid=100012')
            db.close()


if __name__ == '__main__':
    pytest.main([__file__, '-vs'])
