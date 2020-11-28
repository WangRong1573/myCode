#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/28 11:00 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : 全局变量和局部变量.py
# @desc :
def discount(price, rate):
    final_price = price * rate
    # 此处不会修改全局变量的值，而是新建了一个与全局变量同名的局部变量
    # old_price = 50
    # print('试图修改全局变量的值，输出查看：', old_price)
    global old_price
    old_price = 200
    print('试图修改全局变量的值，输出查看：', old_price)
    return final_price


old_price = int(input('请输入价格'))
rate = float(input('请输入折扣'))
discount(old_price, rate)
print('old_price的值为：', old_price)
print('打折后的价格为：', discount(old_price, rate))
