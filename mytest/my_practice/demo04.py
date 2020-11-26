#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/26 21:12 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : demo04.py 
# @desc :   字典的操作

# 下面的字典里面记录了一个游戏系统中用户的信息。 其中key 是用户的ID， value 是另外一个字典，记录了用户名，用户等级和金币数量。
#
from pprint import pprint

members = {
    1: {'name': '白月黑羽', 'level': 3, 'coins': 300},
    2: {'name': '短笛魔王', 'level': 5, 'coins': 330},
    3: {'name': '紫气一元', 'level': 6, 'coins': 340},
    4: {'name': '拜月主', 'level': 3, 'coins': 32200},
    5: {'name': '诸法空', 'level': 4, 'coins': 330},
    6: {'name': '暗光城主', 'level': 3, 'coins': 320},
    7: {'name': '心魔尊', 'level': 3, 'coins': 2300},
    8: {'name': '日月童子', 'level': 8, 'coins': 3450},
    9: {'name': '不死尸王', 'level': 3, 'coins': 324},
    10: {'name': '天池剑尊', 'level': 9, 'coins': 13100},
}


# 要求大家写一个程序，运行的时候先显示如下主菜单
#
# 请选择操作选项：
#    1 查看用户账号信息
#    2 添加用户
#    3 删除用户
#    4 列出所有用户信息
#    0 退出
# 如果用户选择 1 选项， 再次提示用户输入账号名， 用户输入账号后，显示该用户的 ID, 等级和 金币数量。
#
# 如果用户选择 2 选项， 提示用户输入账号名、等级、金币数量。 用户输入后，要检查该账号名是否已经存在，如果已经存在，则提示用户重新输入。如果用户输入的账号不存在，则添加该信息到字典中。
#
# 如果用户选择 3 选项， 提示用户输入账号名。 用户输入后，要检查该账号名是否已经存在，如果不存在，则提示用户重新输入。如果用户输入的账号存在，在用户字典中删除该账号。
#
# 如果用户选择 4 选项，则打印出当前用户表里所有用户的信息
#
# 如果用户选择 0 选项， 则退出程序。
#
# 只要不是选择退出，用户操作完后，再次进入主菜单，让用户再次选择。如此循环，直到用户选择0 退出。
def menu():
    print('\t\t\t请选择操作选项：')
    print('\t\t\t1 查看用户账号信息')
    print('\t\t\t2 添加用户')
    print('\t\t\t3 删除用户')
    print('\t\t\t4 列出所有用户信息')
    print('\t\t\t0 退出')


def start():
    while True:
        menu()
        choice = int(input('请输入序号使用功能\n'))
        if not isinstance(choice, int):
            raise ValueError('input must be integer')

        if choice in [0, 1, 2, 3, 4]:
            if choice == 0:
                answer = input('是否退出程序y/n')
                if answer == 'y':
                    break
            elif choice == 1:
                search()
            elif choice == 2:
                add()
            elif choice == 3:
                delete()
            elif choice == 4:
                show()
        else:
            print('input must between 0 ~ 4')


def search():
    while True:
        no = int(input('请输入要查询的ID：\n'))
        if no not in members:
            print(f'对不起，未找到ID为{no}的角色信息')
            return
        else:
            msg = members[no]
            print('角色信息查询成功：')
            print('角色ID：{}, 角色名称：{}, 角色等级：{}， 金币数：{}'.format(no, msg['name'], msg['level'], msg['coins']))
        answer = input('是否继续查询？y/n')
        if answer == 'y':
            continue
        else:
            break


def add():
    while True:
        try:
            no = int(input('请输入角色ID\n'))
            name = input('请输入角色姓名\n')
            level = input('请输入角色级别\n')
            coins = input('请输入角色持有金币数\n')
        except:
            print('输入非法')
        else:
            print('角色信息添加成功')
            members[no] = {'name': name, 'level': level, 'coins': coins}

        answer = input('是否继续添加？y/n')
        if answer == 'y':
            continue
        else:
            break
    pprint(members, width=80)


def delete():
    while True:
        no = int(input('请输入要删除的角色ID\n'))
        if no not in members:
            print(f'未找到ID为{no}的角色信息')
        else:
            print(f'ID为{no}的角色信息删除成功')
            members.pop(no)

        answer = input('是否继续删除？y/n')
        if answer == 'y':
            continue
        else:
            break
    pprint(members, width=80)


def show():
    for k, v in members.items():
        print('角色ID：{}, 角色名称：{}, 角色等级：{}， 金币数：{}'.format(k, v['name'], v['level'], v['coins']))


if __name__ == '__main__':
    start()
