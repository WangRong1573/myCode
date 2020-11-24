#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/24 21:42 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : test_example6.py 
# @desc : 关键字驱动，web自动化代码封装
import time

import webkeys


class Test_web:
    """
    电商PO封装
    """

    def setup_class(self):
        self.web = webkeys.WebKey()
        self.web.open_browser()

    def test_login(self):
        """
        登录成功用例
        :return: None
        """
        self.web.get_url('http://testingedu.com.cn:8000/index.php/Home/user/login.html')
        self.web.input('//*[@id="username"]', '13800138006')
        self.web.input('//*[@id="password"]', '123456')
        self.web.input("/html//input[@id='verify_code']", '1111')
        self.web.click("//form[@id='loginform']/div[@class='layel2']//a[@name='sbtbutton']")

    def teardown_class(self):
        """
        退出浏览器
        :return:
        """
        time.sleep(3)
        self.web.quit()
