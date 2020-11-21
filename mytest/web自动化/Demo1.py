#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
selenium 学习
"""

from selenium import webdriver

# webDriver对象，声明操作的浏览器
driver = webdriver.Chrome()

# 设置全局等待时间
driver.implicitly_wait(30)

# 窗口最大化
driver.maximize_window()

# 打开指定页面
driver.get('http://testingedu.com.cn:8000/index.php/Home/user/login.html')


# 定位元素,执行操作
driver.find_element_by_id('username').send_keys('13800138006')

driver.find_element_by_id('password').send_keys('123456')

driver.find_element_by_id('verify_code').send_keys('1111')

driver.find_element_by_class_name('J-login-submit').click()
