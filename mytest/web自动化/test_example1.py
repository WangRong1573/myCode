#!/usr/bin/env python
# -*- coding:utf-8 -*-

# pytest 环境搭建 pip install pytest
# pip install pytest-xdist

# pytest组成
#     1.测试模块：满足以test_*.py或者*_test.py格式（py脚本）
#     2.在测试模块中以Test开头，并且不能带有__init__方法（用例集合）
#     3.测试函数，以test_开头


class Test_Comm:
    """
    测试模块
    """

    def login(self):
        """
        这不是一个合规的测试用例/函数，执行时不会被执行
        :return:
        """
        print('这不是一个测试模块')

    def test_login(self):
        """
        这是一个合规的测试用例
        :return:
        """
        print('这是面向对象的封装')
        print('这是一个合规的测试用例')
