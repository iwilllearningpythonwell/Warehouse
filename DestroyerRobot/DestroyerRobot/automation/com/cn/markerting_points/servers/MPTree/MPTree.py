#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/29
# @Author  : vivid-XIEMENG
# @FileName: MPTree.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
class MPTree:
    def __init__(self,driver):
        """
        获取驱动
        """
        self.base = BasePage(driver)


    def points_managers(self,bys,values):
        """
        积分管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def points_marking(self,bys,values):
        """
        营销管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def points_shopping(self,bys,values):
        """
        积分商城
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)