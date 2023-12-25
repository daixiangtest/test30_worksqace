"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 18:47
File   : python_senior04.py
===============***===============
"""
"""
迭代器:  只能从前往后遍历,每次会记住你遍历的位置,下次还从这个位置开始给你,如果遍历完就指向None,不占用系统资源
可以使用iter()把可迭代对象编程 迭代器对象,通过next()遍历
生成器: 生成器是一个包含yield关键字的函数,调用生成器函数返回一个迭代器对象

"""
"""
知识点: python操作mysql数据库,查询(查询单条、查询多条、查询所有)
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
count = cursor.execute("select * from account")
print(count)

# 第五步: 获取结果集中的数据
# 1.获取第一条数据
# data = cursor.fetchone()  # 返回一条数据,并且打包成元组格式
# 2.获取多条数据
# data = cursor.fetchmany(2)  # 返回多条数据,并且打包成元组格式
# 3.获取所有数据
data = cursor.fetchall()
print(data)

# 第六步: 关闭游标
cursor.close()

# 第七步: 关闭连接
conn.close()
