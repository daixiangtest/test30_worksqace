"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 15:57
File   : python_senior07.py
===============***===============
"""
import pymysql

"""
数据库封装
"""


class DBUtils:
    count = -1  # （定义一个默认属性）

    # 封装连接对象和游标对象
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='businessdb')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库工具连接出现异常，请检查DBUtils类中的__init__方法", e)

    # 封装关闭游标对象和连接对象
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 封装增删改
    # 如果execute()括号内只传入一个参数，我们运行execute（sql）
    # 如果execute()括号中传入两个参数，如果是元组占位符参数我们运行execute(sql,params),如果是列表则执行executemany(sql,params)
    def cud(self, sql, params=None):
        try:
            if params is None:  # 判断传了几个参数，如果只传了一个参数，那么就执行execute（sql）
                self.count = self.cursor.execute(sql)
            if isinstance(params, tuple):  # 判断传入的参数是不是元组，是元组类型执行execute(sql,params)
                self.count = self.cursor.execute(sql, params)
            if isinstance(params, list):
                self.count = self.cursor.executemany(sql, params)
            self.conn.commit()
            return self.count  # 返回sql影响的条目数
        except Exception as e:
            print('增删改失败', e)


if __name__ == '__main__':
    db = DBUtils()
    count=db.cud('delete from account where name = %s',['哈哈','小李'])
    # count = db.cud("insert into account(name,age,nickName) values(%s,%s,%s)",
    #                [('小花', 18, '花花'), ('小马', 20, '欢乐马'), ('小刘', 20, '牛牛')])


