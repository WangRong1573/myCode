#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/28 10:03 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : 字符串内置方法.py 
# @desc : 字符串练习

# 声明
str1 = 'i am a man'
# 切片
print(str1[:8:2])

# 拼接
str2 = 'YOU'
str3 = str2 + ' ' + str1
print(str3)

# 把字符串的第一个字母变成大写
print(str3.capitalize())

#所有变成小写
print(str3.casefold())

# 居中
print(str3.center(40))

# 字符串出现的次数
print(str3.count('a', 0, len(str3)))

print(str3.endswith('n'))

# 找不到返回-1，找到返回元素第一次出现的位置
print(str3.find('x'))

# 向原字符串中添加分隔符
print(str3.join('----'))
# -YOU i am a man-YOU i am a man-YOU i am a man-

# partition(sub)找到子字符串，把字符串分成一个3元组，(pre_sub,sub,fol_sub),如果字符串中不包含sub，返回('原字符串','','')
str4 = 'my_demo.tex'
print(str4.partition('.'))
# print(str4.partition('-'))

# replace(old,new,[,count]) 把字符串中的old字符串替换成new字符串，count可指定替换次数
str5 = 'i am a student i like play game but i have to work hard'
print(str5.replace(' ', '-', 3))

# split(sep=None)默认是以空格来切分，可传入参数指定切分格式
print(str5.split())
print(str5.split(' '))

str6 = 'i-im-a-student'
print(str6.split('-'))

# strip([chars]) 删除字符串前后所有的空格，chars可指定删除的字符
str7 = '            ggggssssaasdfsdfggdgdg   '
print(str7.strip())
str8 = 'ggggssssaasdfsdfggdgdg'
print(str7.strip('g'))