"""
===============***===============
Auther : Lee
Date   : 2022-11-14 - 13:42
File   : python_senior02.py
===============***===============
"""

"""
知识点：python操作mysql数据库，进行增删改
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

# 第四步：通过游标对象执行sql语句，执行sql后返回影响的条目数
"""
通过execute（）方法提供的另外一种方式，占位符方式执行sql，execute（sql,params)
把活得数据通过%s进行占位，再通过元组进行赋值，好处：
        1.增加SQL代码的可读性
        2.占位符可以预先编译，提高执行的效率
        3.防止SQL注入
        4.用占位符的目的是绑定变量，这样可以减少数据SQL的硬解析，所以执行效率会提高不少
"""

# 新增
# count = cursor.execute("insert into account(name,age,nickName)values(%s,%s,%s)", ('xiaomei', 20, '美美'))
# 删除
count = cursor.execute("delete from account where name =%s", ('xiaohei',))
# 修改
count = cursor.execute("update account set name=%s where name=%s", ('小李', 'xiaomei'))
print(count)  # 数据受影响的行数

# 第五步：增删改都需要提交，不能忘记，否则数据库的数据不变:
conn.commit()

# 第六步：关闭游标:
cursor.close()

# 第七步：关闭连接：
conn.close()
