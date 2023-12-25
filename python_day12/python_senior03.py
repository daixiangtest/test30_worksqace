"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 13:42
File   : python_senior03.py
===============***===============
"""
"""
知识点：python操作MySQL数据库，进行批量增删改
"""

# 第一步：导入第三块模块，pymysql是一个第三方的库，我们需要先安装，再引包，然后通过pymysql库操作mysql数据库
import pymysql

# 第二步：获取连接对象（我们需要对象名，ip地址，端口号，用户名，密码，库名）
# localhost和127.0.0.1 代表本地的真实存在的ip地址（闭环地址）
# mysql默认端口号3306  Oracle默认端口号1521 http默认端口号80  https默认端口号443
# db是database的缩写数据库的意思
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)  # <pymysql.connections.Connection object at 0x0000019604277390>

# 第三步：获取一个游标对象，游标：用来执行sql和储存结果集的
cursor = conn.cursor()  # 通过连接对象新建游标对象

# 第四步：批量增删改操作，executemany(sql,params) 占位符数据用列表，列表中有几个成员sql就执行几次
# 新增
# count = cursor.executemany("insert into account(name,age,nickName) values(%s,%s,%s)",
#                            [('大花', 25, '女'), ('老徐', 28, '猛男'), ('班花', 20, '女')])
# 删除
count = cursor.executemany("delete from account where name=%s", ['老徐','班花'])

# 修改
# count = cursor.executemany("update account set name=%s where name=%s", [('huahua', '班花'), ('黑黑', '老徐')])
print(count)
# 第五步：增删改都需要提交，不能忘记，否则数据库的数据不变:
conn.commit()

# 第六步：关闭游标:
cursor.close()

# 第七步：关闭连接：
conn.close()


