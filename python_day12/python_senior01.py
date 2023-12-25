"""
===============***===============
Auther : Lee
Date   : 2022-11-13 - 19:04
File   : python_senior07.py
===============***===============
"""
"""
知识点：python操作mysql数据库，进行增删改
"""
"""
第三方库的下载方法
1.通过电脑端的cmd命令提示符 输入pip install 库名   下载该库名的文件
2.通过电脑端的cmd命令提示符 输入pip uninstall 库名  卸载该库名的文件
3.当有些库的文件过大且是从外网下载时可能会导致库名下载失败 这时可以输入pip install 库名-i IP地址  临时更改下载的IP地址
4.永久更改国外镜像首先在c:users\用户名文件中创建一个pip文件目录，然后在目录中创建一个pip.ini文件 打开该文件输入以下内容：
[global]
index-url=https://pypi.douban.com/simple (ip地址)
[install]
trusted-host=pypi.pypi.douban.com(ip地址的域名)
保存退出即可
通过pycharm这个ide来下载
1.直接输入import 库名 当库名标红的时候鼠标放在上面提示可以下载该库，直接点击下载即可
2.点击展示台最下面的terminal（Alt+F12）输入代码与上面的电脑端输入操作一样
3.点击左上角的File,点击seting,点击project:WorkSpace,点击Python Interpreter,点击加号输入框输入库名，删除则点击库名再点击减号就可以
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
# 新增
count = cursor.execute("insert into account (name,age,nickName) values('小马',19,'黑马')")
# 删除
# count=cursor.execute('delete from account where name="小花"')
# 修改
# count = cursor.execute("update account set name='小马' where name='大马'")
print(count)  # 数据受影响的行数

# 第五步：增删改都需要提交，不能忘记，否则数据库的数据不变:
conn.commit()

# 第六步：关闭游标:
cursor.close()

# 第七步：关闭连接：
conn.close()
