#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 11:07
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : myinfo.py

from DestroyerRobot.automation.app.cn.base.baseapp import BaseApp
class MyInfo:
    def __init__(self,driver):
        """
        进入【我的】页面
        :param driver:
        """
        self.base = BaseApp(driver)

    def click_loginsing(self,bys,values):
        """
        点击【注册|登录】
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        if ele:
            self.base.click(ele)

    def choose_house(self,bys,values):
        """
        点击【在线选房】
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        if ele:
            self.base.click(ele)

    def mypoint(self,bys,values):
        """
        点击【我的积分】
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        if ele:
            self.base.click(ele)

    def seckill_order(self,bys,values):
        """
        点击【闪购订单】
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        if ele:
            self.base.click(ele)

