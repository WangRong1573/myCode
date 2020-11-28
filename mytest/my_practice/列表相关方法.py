#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/28 10:46 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : 列表相关方法.py 
# @desc :
# 同类型时可使用max，min函数来比较列表和元组的最大值和最小值
l1 = [1, 5, 3, 5, 5, 85, 84, 36]
print(max(l1))

print(min(l1))

t1 = (1, 34, 3454, 6, 7, 34)
print(max(t1))
print(min(t1))

# 报错
# l2 = ['a',2,4]
# print(max(l2))

print(sum(l1))

# 等同于l1.sort()
print(sorted(l1))

# reversed(l1)
print(list(reversed(l1)))

a = [1,3,5]
b = [3,6,8,9]
print(list(zip(a, b)))