#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/25 22:26 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : 使用@property.py 
# @desc :

# class Student(object):
#
#     def __init__(self):
#         self._score = None
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100')
#
#         self._score = value


# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作
class Student(object):

    _score: int

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
