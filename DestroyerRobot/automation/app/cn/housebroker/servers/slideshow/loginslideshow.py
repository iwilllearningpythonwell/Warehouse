#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/10
# @Author  : vivid-XIEMENG
# @FileName: test_hive.py
# @Software: PyCharm
# @email   : 331597811@QQ.com

from DestroyerRobot.automation.app.cn.base.baseapp import  BaseApp

class LoginSideShow:

    def __init__(self,driver):
        self.driver = BaseApp(driver)

    def get_swipLeft(self):
        for i in range(3):
            self.driver.swipLeft()
