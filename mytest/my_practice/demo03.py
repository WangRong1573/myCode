#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/26 20:45 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : demo03.py 
# @desc :
# 这个是一个数据文件，格式如下
#
# 薛蟠     4560 42
# 薛蝌     4460 25
# 薛宝钗   5776 43
# 薛宝琴   4346 42
# 王夫人   3360 25
# 王熙凤   4460 35
# 王子腾   5660 45
# 王仁     5034 65
# 尤二姐   5324 25
# 贾芹   5663 25
# 贾蓉     3446 15
# 贾兰     3443 35
# 贾芸     4522 25
# 尤三姐   5905 45
# 贾珍     4603 25
# 这里面有3列数据，分别 保存了 游戏系统的用户名， 用户积分 ， 年龄
#
# 现在要求大家写一个程序，计算出同一姓氏的人的积分总和。
#
# 输出结果格式如下：
#
# 薛 : 19142
# 王 : 18514
# 尤 : 11229
# 贾 : 21677

def read_demo():
    """
    练习文件读取和数据类型转换操作
    :return:
    """
    with open('0016_1.txt', 'r', encoding='utf8') as file:
        # 此时得到的是一个列表
        content = file.read()
        print(type(content))  # str

        l = content.splitlines()
        d = {}
        for i in l:
            it = i.split()
            print(it)
            name = it[0][0]
            score = int(it[1])
            if name not in d:
                d[name] = score
            else:
                d[name] += score
        print(d)


read_demo()
