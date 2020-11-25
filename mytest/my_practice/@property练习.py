#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/25 22:36 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : @property练习.py 
# @desc :练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Computer(object):

    def __init__(self):
        self._height = None
        self._width = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width


# 测试:
s = Computer()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
