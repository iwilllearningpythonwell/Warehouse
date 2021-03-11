#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 16:00
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : login.py

from DestroyerRobot.automation.app.cn.base.baseapp import BaseApp
class Login:
    def __init__(self, driver):
        self.base = BaseApp(driver)

    def click_tvPassLogin(self,bys,values):
        """
        点击【账号密码登录】
        :param bys:
        :param value:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        if ele:
            self.base.click(ele)

    def input_tvPhoneNum(self,bys,values,iphonenum):
        ele = self.base.getElementByElements(bys, values)
        if ele:
            self.base.sendkeys(ele, iphonenum)

    def input_tvPassword(self, bys, values, password):
        ele = self.base.getElementByElements(bys, values)
        if ele:
            self.base.sendkeys(ele, password)