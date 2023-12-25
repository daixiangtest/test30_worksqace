"""
===============***===============
Auther : Lee
Date   : 2022-11-15 - 17:36
File   : python_senior10.py
===============***===============
"""
"""
注册接口
1.只允许post请求
2.用户信息必须有用户名、密码、确认密码、手机号、邮箱
3.密码和确认密码必须一致
4.用户名和手机号、邮箱不能重复
5.用户名和密码6-8位
6.手机号(11位的纯数字)和邮箱(判断是否带有@和.com)格式校验
"""
import flask
import json
import autotest_01.comms.dbutils as db

app = flask.Flask(__name__)


@app.route('/tianmao', methods=['post','get'])
def tianmao():
    data = flask.request.values.to_dict()
    if "username" not in data:
        return json.dumps({"code": 1001, "msg": "用户名键值不能为空!"}, ensure_ascii=False)
    if "psw" not in data:
        return json.dumps({"code": 1002, "msg": "密码键值不能为空!"}, ensure_ascii=False)
    if "re_psw" not in data:
        return json.dumps({"code": 1003, "msg": "确认密码键值不能为空!"}, ensure_ascii=False)
    if "phone" not in data:
        return json.dumps({"code": 1004, "msg": "手机号键值不能为空!"}, ensure_ascii=False)
    if "email" not in data:
        return json.dumps({"code": 1005, "msg": "邮箱键值不能为空!"}, ensure_ascii=False)
    else:
        username = data['username']
        psw = data['psw']
        re_psw = data['re_psw']
        phone = data['phone']
        email = data['email']

        if len(username) == 0:
            return json.dumps({"code": 1006, "msg": "用户名输入不能为空!"}, ensure_ascii=False)
        if len(psw) == 0:
            return json.dumps({"code": 1007, "msg": "密码不能为空!"}, ensure_ascii=False)
        if len(phone) == 0:
            return json.dumps({"code": 1008, "msg": "手机号不能为空!"}, ensure_ascii=False)
        if len(phone) != 11 or not phone.isnumeric():
            return json.dumps({"code": 1009, "msg": "手机号格式错误!"}, ensure_ascii=False)
        if len(email) == 0:
            return json.dumps({"code": 1010, "msg": "邮箱格式输入不能为空!"}, ensure_ascii=False)
        if psw != re_psw:
            return json.dumps({"code": 1011, "msg": "两次密码不一致!"}, ensure_ascii=False)
        if "@" not in email and ".com" not in email:
            return json.dumps({"code": 1012, "msg": "邮箱格式不正确!"}, ensure_ascii=False)
        else:
            db1 = db.DBUtils()
            count1 = db1.find_count("select * from tb_user where name=%s", (username,))
            count2 = db1.find_count("select * from tb_user where email=%s", (email,))
            count3 = db1.find_count("select * from tb_user where phone=%s", (phone,))

            if count1 >= 1:
                db1.close()
                return json.dumps({"code": 1013, "msg": "用户名已经注册!"}, ensure_ascii=False)
            if count2 >= 1:
                db1.close()
                return json.dumps({"code": 1014, "msg": "邮箱已经使用!"}, ensure_ascii=False)
            if count3 >= 1:
                db1.close()
                return json.dumps({"code": 1015, "msg": "手机号已经注册!"}, ensure_ascii=False)
            else:
                count4 = db1.cud("insert into tb_user(name,passwd,email,phone) values(%s,%s,%s,%s)",
                                        (username, psw, email, phone))
                db1.close()
                if count4 == 1:
                    return json.dumps({"code": 1016, "msg": "登录成功!"}, ensure_ascii=False)
                else:
                    return json.dumps({"code": 1017, "msg": "系统异常!"}, ensure_ascii=False)


if __name__ == '__main__':
    app.run(port=5589,debug=True)
