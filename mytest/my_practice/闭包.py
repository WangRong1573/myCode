#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/28 12:45 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : 闭包.py 
# @desc :概念：如果一个函数的内部函数引用了外部函数的局部变量，成为闭包
def fun1(x):
    def fun2(y):
        return x * y

    return fun2


# 调用fun1返回的是一个function对象 fun2
print(fun1(5))

print(fun1(5)(8))


def funx():
    x = 5
    def funy():
        nonlocal x
        x *= x
        return x
    return funy


print(funx()())