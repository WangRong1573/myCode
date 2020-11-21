#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
PO模式学习
"""
import time

from selenium import webdriver


class Comm:
    """
    电商项目PO封装
    """

    def __init__(self):
        """
        构造函数，创建对象时候执行
        初始化浏览器
        """
        self.driver = webdriver.Chrome()

        # 设置全局等待时间
        self.driver.implicitly_wait(30)

        # 窗口最大化
        self.driver.maximize_window()

    def login(self):
        """
        登录用例
        :return:
        """
        self.driver.get('http://testingedu.com.cn:8000/index.php/Home/user/login.html')

        self.driver.find_element_by_id('username').send_keys('13800138006')

        self.driver.find_element_by_id('password').send_keys('123456')

        self.driver.find_element_by_id('verify_code').send_keys('1111')

        self.driver.find_element_by_class_name('J-login-submit').click()

    def info(self):
        """
        需要登录成功
        :return:
        """
        # self.driver.get('http://testingedu.com.cn:8000/index.php/Home/User/info.html')

        self.driver.find_element_by_css_selector('ul:nth-of-type(4) > li:nth-of-type(2) > a').click()

        # 点击头像
        self.driver.find_element_by_css_selector('img#preview').click()

        # 进入iframe
        self.driver.switch_to.frame(0)

        self.driver.find_element_by_name("file") \
            .send_keys('G:\myCode\mytest\images\demo.png')

        time.sleep(2)

        self.driver.find_element_by_class_name('saveBtn').click()


if __name__ == '__main__':
    comm = Comm()
    comm.login()

    # 上传头像
    comm.info()
