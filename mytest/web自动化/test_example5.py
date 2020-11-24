#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/24 20:16 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : test_example5.py 
# @desc :allure 测试报告

# 环境搭建
# 下载allure commandine 压缩包
# 解压，进入到bin目录，将bin目录路径添加到环境变量path中去
# pip install allure-pytest
# 安装pip install allure-pytest
# runner 中配置pytest.main(['--alluredir','./temp'])
# 执行命令 allure generate ./temp -o ./report --clean 生成测试报告(如果在terminal内无法执行
# 就在cmd中，切换到项目所在目录，执行此命令)
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