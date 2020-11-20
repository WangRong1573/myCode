#!/usr/bin/env python
# -*- coding:utf-8 -*-

# list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
# len()函数可以获得list元素的个数

# 索引从0开始
print(classmates[0])
# 索引越界 IndexError: list index out of range
# print(classmates[3])

# 最后一个元素
classmates[-1]

# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Tom')
print(classmates)

# 把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素，用pop()
classmates.pop()

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(2)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = '孙悟空'


# tuple 不可变序列
t = (1,2)
t2 = (1,)
t3 = ()

# 查找
print(t[0])
