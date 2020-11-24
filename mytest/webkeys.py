#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Time : 2020/11/24 21:43 
# @Author : 好好学习吧，每天都有新打击！ 
# @File : webkeys.py 
# @desc : 关键字
from selenium import webdriver


class WebKey:
    def __init__(self):
        self.driver = None

    def open_browser(self, br='gc'):
        """
        打开浏览器，默认谷歌
        :param br: gc = 谷歌； ff=Firefox；ie=IE浏览器
        :return:
        """
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器在不支持')

        # 默认隐式等待
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get_url(self, url=None):
        """
        打开网站
        :param url:网站地址
        :return:
        """
        self.driver.get(url)

    def __find_ele(self, locator=''):
        """
        支持8中定位方式
        :param locator: xpath = //*[@id=''user]
        :return: 返回定位到的元素
        """
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_tag_name(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_link_text(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(
                locator[locator.find('=') + 1:]
            )
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_css_selector(
                locator[locator.find('=') + 1:]
            )
        else:
            ele = self.driver.find_element_by_xpath(locator)

        self.ele = ele
        return ele

    def click(self, locator=None):
        """
        找到并点击元素
        :param locator: 默认xpath
        :return:
        """
        ele = self.__find_ele(locator)
        ele.click()

    def input(self, locator=None, value=None):
        """
        找到元素并完成输入
        :param locator: 默认xpath
        :param value: 输入字符串
        :return:
        """
        ele = self.__find_ele(locator)
        ele.send_keys(str(value))

    def into_iframe(self,locator=None):
        """
        进入iframe
        :param locator: iframe定位器
        :return:
        """
        ele = self.__find_ele(locator)
        self.driver.switch_to.frame(ele)

    def quit(self):
        """
        退出浏览器
        :param locator:
        :return:
        """
        self.driver.quit()