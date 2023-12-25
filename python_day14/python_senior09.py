"""
===============***===============
Auther : Lee
Date   : 2022-11-15 - 15:10
File   : python_senior09.py
===============***===============
"""
import flask

# 第二部：创建应用对象，__name__代表当前文件，把当前的python模块当作一个服务
app = flask.Flask(__name__)


# 第三步：我们将接口发布成服务，route是路由的意思
@app.route('/add', methods=['get', 'post'])
def add():
    data = flask.request.values.to_dict()
    a = data['params1']
    b = data['params2']
    return str(eval(a) + eval(b))


if __name__ == '__main__':
    app.run(debug=True)
