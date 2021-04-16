#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/22
# @Author  : vivid-XIEMENG
# @FileName: MPTreeKids.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
class MPTreeKids:
    def __init__(self,driver):
        """
            获取驱动
        """
        self.base = BasePage(driver)

################# 积分管理 start ###############
    def points_rule(self,bys,values):
        """
        积分规则
        :param bys:
        :param values:
        :return:
        """
        ele=self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def points_rule_small_routine(self,bys,values):
        """
        积分规则小程序,
        :param bys: xpath
        :param values: //*[contains(text(),XXXX)]
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def points_change(self,bys,values):
        """
        调整积分
        :param bys: xpath
        :param values: //*[contains(text(),XXXX)]
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def points_change_small_routine(self,bys,values):
        """
        调整积分小程序
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

################# 积分管理 end ###############

################# 营销管理 start #############

    def  markering_actions(self,bys,values):
        """
        营销活动管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def markering_prices(self,bys,values):
        """
        奖品管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)


################# 营销管理 end ###############

################# 积分商城 start ###############

    def points_goods(self,bys,values):
        """
        积分商品
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def points_order(self, bys, values):
        """
        积分订单
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)
        
################# 积分商城 end ###############