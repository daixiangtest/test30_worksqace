"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 18:47
File   : python_senior05.py
===============***===============
"""
"""
知识点: python操作mysql数据库,参数化查询(查询单条、查询多条、查询所有)
"""

# 第一步: 导入第三方模块,pymysql是一个第三方的库,我们需要先安装,再引包,然后通过pymysql库操作mysql数据库
import pymysql

# 第二步: 获取连接对象(我们需要对象名、ip地址、端口号、用户名、密码、库名)
# localhost和 127.0.0.1 代表本地的真实ip地址(闭环地址)
# mysql默认端口号3306  oracle默认端口号1521  http默认端口号80  https默认端口号443
# db 是database的缩写
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='businessdb')
print(conn)  # <pymysql.connections.Connection object at 0x0000020DE73A97B8>

# 第三步: 获取一个游标对象,游标: 用来执行sql和存储结果集的
cursor = conn.cursor()  # 通过连接对象新建游标对象

# 第四步: 通过游标对象执行sql语句,执行sql后返回影响的条目数
count = cursor.execute("select * from account where age = %s", (18,))
print(count)

# 第五步: 获取结果集中的数据
# 1.获取第一条数据
# data = cursor.fetchone()  # 返回一条数据,并且打包成元组格式
# 2.获取多条数据
# data = cursor.fetchmany(3)  # 返回多条数据,并且打包成元组格式
# 3.获取所有数据,游标对象是一个迭代器
data = cursor.fetchall()
print(data)

# 第六步: 关闭游标
cursor.close()

# 第七步: 关闭连接
conn.close()

