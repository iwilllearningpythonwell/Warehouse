#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/27
# @Author  : vivid-XIEMENG
# @FileName: add_goods.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
class Goods_page():
    """
    新建商品
    """
    def __init__(self,driver):
        self.base = BasePage(driver)

    def add_goods(self,bys,values):
        """
        新增商品
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def find_goods(self,bys,values):
        """
        查询页面
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)




