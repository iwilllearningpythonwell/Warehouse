#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 16:37
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : firstpage.py
from DestroyerRobot.automation.app.cn.base.baseapp import BaseApp

class FirstPage:
    """
    页面操作
    """
    def __init__(self,driver):
        self.base = BaseApp(driver)

    def my_info(self,bys,values):
        """
        点击【我的】
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        if ele:
            self.base.click(ele)

    def lh_info(self,bys,values):
        """
        点击【看房】
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        if ele:
            self.base.click(ele)