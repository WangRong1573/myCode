#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, request

# 新建应用
app = Flask(__name__)


# 路由，用来处理浏览器发送的请求
# @app.route('/')
# def index():
#     return 'hello  world'
#
#
# @app.route('/demo')
# def demo():
#     return render_template('demo.html')
#
#
# @app.route('/hello')
# def hello():
#     return render_template('hello.html', name='赛利亚')

@app.route('/')
def index():
    return render_template('login.html')

# 当写成post时会有一个请求405提示，百度查询结果是改为get，但原因尚不明确
@app.route("/login",methods=['get'])
def login():
    # 接收用户名和密码
    username = request.form.get('username')
    password = request.form.get('pwd')

    if username=='admin' and password=='123':
        return '登录成功'
    else:
        return '登陆失败'


# @app.route('/mylist')
# def mylist():
#     heros = ['神思者', '百花缭乱', '赛利亚', '阿修罗', '不动明王']
#     return render_template('testlist.html', heros=heros)


if __name__ == '__main__':
    # 启动应用
    app.run()
