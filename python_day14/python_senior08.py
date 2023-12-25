"""
===============***===============
Auther : Lee
Date   : 2022-11-15 - 13:47
File   : python_senior08.py
===============***===============
"""

"""
falsk框架：是一个从轻量级的容器框架，能把咱们写好代码发布成服务，通过http协议访问调用
"""

# 第一步：通过pip安装库
import flask

# 第二步：创建应用对象，__name__代表当前文件，把当前的python模块当作一个服务
app = flask.Flask(__name__)


# 第三步：我们将接口接口发布成服务，route是路由的意思
# @app.route('/index', methods=['get', 'post'])
# def test30():
#     return "这是我的第一个接口"

@app.route('/home',methods=['get','post'])
def home():
    return'这是第二个接口'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6868, debug=True)  # 启动服务 debug是可调式服务
