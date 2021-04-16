#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 15:29
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : fristpge.py
from DestroyerRobot.automation.app.cn.base.baseapp import BaseApp

class IndexPage:

    def __init__(self,driver):
        self.base = BaseApp(driver)

    def personal_info_index(self,bys,values):
        """
        进入引导页 个人信息保护指引-->点击
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        if ele:
            self.base.click(ele)

    def judge_element(self,bys,values):
        """
        引导页循环
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        return ele

    def come_in_page(self, ele):
        """
        进入引导页 循环页面4次，点击页面信息进入首页
        :param bys:
        :param values:
        :return:
        """
        if ele:
            self.base.click(ele)


