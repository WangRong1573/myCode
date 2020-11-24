#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/24 20:28 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : test_parameters.py 
# @desc : 参数化
import pytest


def my_sum(x, y):
    return x + y


def login(username, password):
    if username == 'admin' and password == '123456':
        return 1


class Test_Para:
    @pytest.mark.parametrize('username,password',
                             [('admin', '123456'),
                              ('localhost', '123'),
                              ('jack', '000000')])
    def test_login(self, username, password):
        print(f'测试数据为：{username}，{password}')
        assert login(username, password) == 1

    @pytest.mark.parametrize('x,y,z',[
        (1,2,3),
        (1,2,2),
        (1,3,4),
        (1,3,5)
    ])
    def test_my_sum(self,x,y,z):
        print(f'测试场景为：{x}+{y}={z}')
        assert x + y == z
