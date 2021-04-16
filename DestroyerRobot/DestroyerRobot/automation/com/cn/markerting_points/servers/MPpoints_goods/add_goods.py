#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/2
# @Author  : vivid-XIEMENG
# @FileName: add_goods.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from DestroyerRobot.automation.com.cn.base.BasePage import BasePage

class Add_goods():
    def __init__(self,driver):
        self.base = BasePage(driver)

    def houseApp(self,bys,values):
        """
        好房APP
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def companyApp(self,bys,values):
        """
        集团版小程序
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def goodsType(self,bys,values):
        """
        点击商品类型下拉列表
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def goodsTypeObject(self,bys,values):
        """
        实物商品
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def goodsTypeFictitious(self,bys,values):
        """
        虚拟商品
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def goodsName(self,goodsname,bys,values):
        """
        商品名称
        :param goodsname:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[1],goodsname)

    def goodsPrices(self,goodsprice,bys,values):
        """
        商品单价
        :param goodsprice:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[2],goodsprice)

    def goodsSku(self,goodssku,bys,values):
        """
        商品库存
        :param goodssku:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[3],goodssku)

    def goodsPoints(self,goodspoints,bys,values):
        """
        消耗商品积分
        :param goodspoints:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[4],goodspoints)

    def goodsTime(self,bys,values):
        """
        上架时间
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElements(bys,values)
        self.base.click(ele[5])
#########################################
    def beginDay_Clear(self,bys,values):
        ele = self.base.getElementByElement(bys,values)
        self.base.clear(ele)


    def beginDay(self,beginday,bys,values):
        """
        开始日期
        :param bys: 通过xpath录入
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.sendkeys(ele,beginday)

    def beginDayClick(self,bys,values):
        ele = self.base.getElementByElements(bys,values)
        self.base.click(ele[7])

    def beginBack(self,begintimes,bys,values):
        ele = self.base.getElementByElements(bys,values)
        for i in range(len(begintimes)):
            self.base.keys_back_space(ele[7])

    def beginTimes(self,begintimes,bys,values):
        """
        开始时间
        :param begintimes:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElements(bys,values)
        self.base.sendkeys(ele[7],begintimes)


    def endDayBack(self,endDay,bys,values):
        ele = self.base.getElementByElement(bys,values)
        for i in range(len(endDay)):
            self.base.keys_back_space(ele)
    def endDay(self,endDay,bys,values):
        ele = self.base.getElementByElement(bys,values)
        self.base.sendkeys(ele,endDay)

    def endTimesBack(self,endtimes,bys,values):
        ele = self.base.getElementByElements(bys,values)
        for i in range(len(endtimes)):
            self.base.keys_back_space(ele[9])
    def endTimes(self,endTimes,bys,values):
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[9], endTimes)



    def trueTime(self,bys,values):
        """
        日期确定
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)
#########################################

    def goodstemplate(self,template,bys,values):
        """
        导入模板
        :param template:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        print(bys,values)
        self.base.sendkeys(ele,template)

    def goodsImg(self,goodsImg,bys,values):
        """
        上传图片
        :param goodsImg:
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.sendkeys(ele,goodsImg)


    def goodsInfo(self,jsvalues):
        """
        商品介绍
        :return:
        """
        self.base.get_js(jsvalues)

    def  goodsRejected(self,jsvalues):
        """
        退货须知
        :param jsvalues:
        :return:
        """
        self.base.get_js(jsvalues)

    def goodsTrue(self,bys,values):
        """
        创建并上架
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def goodsTure1(self,bys,values):
        """
        确认
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)