#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/23 23:37 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : test_example4.py 
# @desc : setup/teardown
import pytest


def setup_class():
    """
    用例开始前执行一次（测试开始时执行一次）
    :return:
    """
    print('用例开始前执行一次')


def teardown_class():
    """
    用例执行结束后执行一次
    :return:
    """
    print('用例执行结束后执行一次')


def teardown():
    """
    测试函数每次执行结束都会执行
    :return:
    """
    print('用例执行结束')


def setup():
    """
    测试函数每次执行都会执行
    :return:
    """
    print('用例开始执行')


class Test_SetUp:

    @pytest.fixture()
    def mySetup(self):
        """
        fixture先于setup执行的
        :return:
        """
        print('开始')
        yield
        print('结束')

    def test_login(self):
        print('测试执行函数')

    def test_info(self):
        print('测试执行函数2')

    def test_1(self, mySetup):
        print('1执行了')

    def test_2(self):
        print('2执行了')

    def test_3(self):
        print('3执行了')

    def test_4(self,mySetup):
        print('4执行了')

