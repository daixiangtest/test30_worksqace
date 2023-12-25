"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 18:45
File   : python_senior06.py
===============***===============
"""
import pymysql

"""
数据库封装
"""


class DBUtils:
    # 封装连接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库工具类连接出现异常,请检查DBUtils类中的__init__方法!")
            print(e)

    # 封装关闭游标对象和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = DBUtils()
    print(db.conn, db.cursor)
    db.close()
