"""
===============***===============
Auther : Lee
Date   : 2022-11-15 - 20:04
File   : homwork.py
===============***===============
"""
"""
作业登录工具
"""
"""
登录接口
1.只允许post请求
2.用户入参必须有用户名(username)和密码(password)
3.用户名和密码不能为空
4.用户名和密码必须在数据库中存在,提示登录成功,反之提示用户名或密码错误
"""
import flask  # 引入一个flask框架的模板
import json  # 映入json 格式的模板
import autotest.comms.dbutils as db  # 引入数据库连接的模板

app = flask.Flask(__name__)  # 创建一个对象把当前模块当成一个服务


@app.route('/sign', methods=["post", "get"])  # 定义一个虚拟的路径，传送方法为post方法
def sign():  # 定义一个登录的方法
    data = flask.request.values.to_dict()  # 定义请求数据的格式为字典格式
    if 'username' not in data:  # key键的username不能为空
        return json.dumps({"code": 1001, "msg": "用户名不能为空!"}, ensure_ascii=False)
    if 'password' not in data:  # key键的password不能为空
        return json.dumps({"code": 1002, "msg": "密码不能为空!"}, ensure_ascii=False)
    else:
        db1 = db.DBUtils()  # 创建一个操作数据库的实例对象
        name = data['username']  # 输入的用户名赋值给name
        password = data['password']  # 输入的密码赋值给password
        count1 = db1.find_count("select * from businessdb.tb_user where name=%s", (name,))
        count2 = db1.find_count("select * from businessdb.tb_user where passwd=%s", (password,))
        count3 = db1.find_count("select * from businessdb.tb_user where name=%s and passwd=%s", (name, password))
        if len(name) == 0:
            return json.dumps({"code": 1003, "msg": "用户名输入不能为空!"}, ensure_ascii=False)
        if len(password) == 0:
            return json.dumps({"code": 1004, "msg": "密码输入不能为空!"}, ensure_ascii=False)
        if count1 == 0:
            db1.close()
            return json.dumps({"code": 1005, "msg": "用户名不存在!"}, ensure_ascii=False)
        if count2 == 0:
            db1.close()
            return json.dumps({"code": 1006, "msg": "密码错误!"}, ensure_ascii=False)
        if count3 >= 1:
            db1.close()
            return json.dumps({"code": 1007, "msg": "登录成功!"}, ensure_ascii=False)
        else:
            return json.dumps({"code": 1008, "msg": "用户名和密码不匹配!"}, ensure_ascii=False)


if __name__ == '__main__':
    app.run()  # 开启调试功能
