#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/25 22:52 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : 发送邮件.py 
# @desc : 纯文本邮件

# 注意到构造MIMEText对象时，
# 第一个参数就是邮件正文，
# 第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，
# 最后一定要用utf-8编码保证多语言兼容性
from email.mime.text import MIMEText
msg = MIMEText('hello,send by python..','plain','utf-8')

# 通过SMTP发出去
# 输入email地址和口令
from_addr = input('from:')
password = input('password:')

# 输入收件人地址：
to_addr = input('To:')
# 输入SMIP服务器地址
smtp_server = input('SMTP server:')

import smtplib
server = smtplib.SMTP(smtp_server,25) # 默认端口是25
# set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信
server.set_debuglevel(1)
# login()方法用来登录SMTP服务器
server.login(from_addr,password)
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list,邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()