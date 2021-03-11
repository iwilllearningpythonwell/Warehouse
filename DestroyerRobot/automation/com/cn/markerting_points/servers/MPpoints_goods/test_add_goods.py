#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/4
# @Author  : vivid-XIEMENG
# @FileName: test_add_goods.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.util.ExcelUtil2 import DoExcel
from DestroyerRobot.automation.util.RandomUtil import  TestRamdom
from DestroyerRobot.automation.util.ExcelUtil import xlsxoper
import traceback
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPpoints_goods.add_goods import Add_goods
import time
class test_add_goods:
    def __init__(self,driver):
        """
        实现数据后，定位页面信息操作
        登录页面，操作数据
        """
        self.driver = driver


    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("markerting_points_configs")
        return confFile

    def childConfigXlsx(self,sheet,dictData):
        # "获取子配置文件中信息",Excel文件内容
        confFile = self.rootChildConfigPath()

        config1= Config("XlsxFilePath",confFile)

        goodsObjectXlsx = config1.get_path_config("goods_object")
        goodsObjectXlsx = SystemOs().sys_path(goodsObjectXlsx)

        excelUtil = DoExcel(goodsObjectXlsx, sheet).do_excel(**dictData)
        return excelUtil


    def childConfigXML(self,Pageskeyword,UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("uiaddgoods")
        filepath = SystemOs().sys_path(filepath)
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls

    def childConfigImgPath(self):
        """
        获取图片路径，并新建以日期为基础的文件目录名 例如： img/2019-01-01/
        :return:
        """
        confFile = self.rootChildConfigPath()
        config3 = Config("ImgPath",confFile)
        img_path = config3.get_path_config("error_img")
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(img_path,data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

    def childConfigPublicImg(self):
        """
        获取公共上传图片地址
        :return:
        """
        confFile = self.rootChildConfigPath()
        config4 = Config("PublicImg", confFile)
        public_img = config4.get_path_config("goodsImg")
        return public_img

    def childCofigLeading_inEcxel(self):
        """
        导入虚拟文件模板
        :return:
        """
        confFile = self.rootChildConfigPath()
        config5 = Config("XlsxFilePath", confFile)
        Leading_inEcxel = config5.get_path_config("redeem_code_template")
        return Leading_inEcxel


    def set_goodsObject(self):
        """
        添加实物商品
        :return:
        """
        # "获取子配置文件中信息",loginXlsx
        dictData = {"goodsName": 3, "goodsImg": 7, "goodsInfo": 8, "goodsReject": 9}
        excel = self.childConfigXlsx("sheet1", dictData)
        # 获取XML中相关信息
        bys_companyApp, values_companyApp = self.childConfigXML("新建商品页面", "集团小程序")
        bys_houseApp, values_houseApp = self.childConfigXML("新建商品页面", "好房APP")
        bys_goodsType, values_goodsType = self.childConfigXML("新建商品页面", "商品类型")
        bys_goodsTypeObject, values_goodsTypeObject = self.childConfigXML("新建商品页面", "商品类型实物")
        bys_goodsName, values_goodsName = self.childConfigXML("新建商品页面", "商品名称")
        bys_goodsPrice, values_goodsPrice = self.childConfigXML("新建商品页面", "商品单价")
        bys_goodsSKU, values_goodsSKU = self.childConfigXML("新建商品页面", "商品库存数量")
        bys_goodsPoints, values_goodsPoints = self.childConfigXML("新建商品页面", "消耗积分")
        bys_goodsTimes,values_goodsTimes = self.childConfigXML("新建商品页面", "上架时间")
        bys_beginday,values_beginday = self.childConfigXML("新建商品页面", "开始日期")
        bys_begintimes,values_begintimes = self.childConfigXML("新建商品页面", "开始时间")
        bys_endday,values_endday = self.childConfigXML("新建商品页面", "结束日期")
        bys_endTimes,values_endTimes = self.childConfigXML("新建商品页面", "结束时间")
        bys_trueTimes,values_trueTimes = self.childConfigXML("新建商品页面", "日期确定")
        bys_goodsImg, values_goodsImg = self.childConfigXML("新建商品页面", "上传图片")
        bys_goodsInfo, values_goodsInfo = self.childConfigXML("新建商品页面", "商品介绍")
        bys_goodsReject, values_goodsReject = self.childConfigXML("新建商品页面", "退货须知")
        bys_goodstrue, values_goodstrue = self.childConfigXML("新建商品页面", "创建并上架")
        bys_goodstrue1, values_goodstrue1 = self.childConfigXML("新建商品页面", "确定上架")
        beginDay,beginTimes=str(TestDateTime().chioce_time(300)).split(" ")
        endDay,endTimes = str(TestDateTime().chioce_time(60*60*24*30)).split(" ")
        add_goods = Add_goods(self.driver)
        try:
            num = TestRamdom().RandomShang(3)
            if num == 0:
                """集团版小程序"""
                add_goods.companyApp(bys_companyApp, values_companyApp)
            elif num == 1:
                """好房APP小程序"""
                add_goods.houseApp(bys_houseApp, values_houseApp)
            else:
                """集团版小程序&好房APP小程序"""
                add_goods.houseApp(bys_houseApp,values_houseApp)
                add_goods.companyApp(bys_companyApp,values_companyApp)
            add_goods.goodsType(bys_goodsType,values_goodsType)
            add_goods.goodsTypeObject(bys_goodsTypeObject,values_goodsTypeObject)
            #时间戳类型商品名称
            goodsName=excel[0]["goodsName"]+str(int(TestDateTime().time_stamp()))
            add_goods.goodsName(goodsName,bys_goodsName,values_goodsName)
            #商品价格100以内的浮点数
            goodsPrices = TestRamdom().RandomTestFloat(100)
            add_goods.goodsPrices(str(goodsPrices),bys_goodsPrice,values_goodsPrice)
            #商品数量
            goodsPrices = TestRamdom().RandomTestInt(10)
            add_goods.goodsSku(str(goodsPrices),bys_goodsSKU,values_goodsSKU)
            #消耗积分
            goodsPoints = TestRamdom().RandomTestInt(10)
            add_goods.goodsPoints(str(goodsPoints),bys_goodsPoints,values_goodsPoints)
            #点击上架时间
            add_goods.goodsTime(bys_goodsTimes,values_goodsTimes)
            add_goods.beginDay_Clear(bys_beginday,values_beginday)
            add_goods.beginDay(beginDay,bys_beginday,values_beginday)
            add_goods.beginDayClick(bys_begintimes,values_begintimes)
            add_goods.beginBack(beginTimes,bys_begintimes,values_begintimes)
            add_goods.beginTimes(beginTimes,bys_begintimes,values_begintimes)
            add_goods.endDayBack(endDay,bys_endday,values_endday)
            add_goods.endDay(endDay,bys_endday,values_endday)
            add_goods.endTimesBack(endTimes,bys_endTimes,values_endTimes)
            add_goods.endTimes(endTimes,bys_endTimes,values_endTimes)
            add_goods.trueTime(bys_trueTimes,values_trueTimes)
            #商品图片
            goodsImg = SystemOs().sys_path(self.childConfigPublicImg(),excel[0]["goodsImg"])
            add_goods.goodsImg(goodsImg,bys_goodsImg,values_goodsImg)
            #商品介绍
            jsGoodsInfo=values_goodsInfo %(excel[0]["goodsInfo"]+str(TestDateTime().local_time()))
            add_goods.goodsInfo(jsGoodsInfo)
            #退货须知
            jsGoodsReject = values_goodsReject %(excel[0]["goodsReject"]+str(TestDateTime().local_time()))
            add_goods.goodsRejected(jsGoodsReject)
            #创建并上架
            add_goods.goodsTrue(bys_goodstrue,values_goodstrue)
            add_goods.goodsTure1(bys_goodstrue1,values_goodstrue1)
            #返回驱动
            driver = add_goods.base.get_driver()
            return driver
        except Exception :
            img_path = self.childConfigImgPath()
            add_goods.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def set_goodsVR(self):
        """
        添加虚拟商品
        :return:
        """
        # "获取子配置文件中信息",loginXlsx
        dictData = {"goodsName": 3, "goodsImg": 7, "goodsInfo": 8, "goodsReject": 9}
        excel = self.childConfigXlsx("sheet1", dictData)
        # 获取XML中相关信息
        bys_companyApp, values_companyApp = self.childConfigXML("新建商品页面", "集团小程序")
        bys_houseApp, values_houseApp = self.childConfigXML("新建商品页面", "好房APP")
        bys_goodsType, values_goodsType = self.childConfigXML("新建商品页面", "商品类型")
        bys_goodsTypeObject, values_goodsTypeObject = self.childConfigXML("新建商品页面", "商品类型虚拟")
        bys_goodsName, values_goodsName = self.childConfigXML("新建商品页面", "商品名称")
        bys_goodsPrice, values_goodsPrice = self.childConfigXML("新建商品页面", "商品单价")
        bys_goodsExcel, values_goodsExcel = self.childConfigXML("新建商品页面", "导入模板")
        bys_goodsPoints, values_goodsPoints = self.childConfigXML("新建商品页面", "消耗积分")
        bys_goodsTimes, values_goodsTimes = self.childConfigXML("新建商品页面", "上架时间")
        bys_beginday, values_beginday = self.childConfigXML("新建商品页面", "开始日期")
        bys_begintimes, values_begintimes = self.childConfigXML("新建商品页面", "开始时间")
        bys_endday, values_endday = self.childConfigXML("新建商品页面", "结束日期")
        bys_endTimes, values_endTimes = self.childConfigXML("新建商品页面", "结束时间")
        bys_trueTimes, values_trueTimes = self.childConfigXML("新建商品页面", "日期确定")
        bys_goodsImg, values_goodsImg = self.childConfigXML("新建商品页面", "上传图片")
        bys_goodsInfo, values_goodsInfo = self.childConfigXML("新建商品页面", "商品介绍")
        bys_goodsReject, values_goodsReject = self.childConfigXML("新建商品页面", "退货须知")
        bys_goodstrue, values_goodstrue = self.childConfigXML("新建商品页面", "创建并上架")
        bys_goodstrue1, values_goodstrue1 = self.childConfigXML("新建商品页面", "确定上架")
        beginDay, beginTimes = str(TestDateTime().chioce_time(300)).split(" ")
        endDay, endTimes = str(TestDateTime().chioce_time(60 * 60 * 24 * 30)).split(" ")
        add_goods = Add_goods(self.driver)
        try:
            num = TestRamdom().RandomShang(3)
            if num == 0:
                """集团版小程序"""
                add_goods.companyApp(bys_companyApp, values_companyApp)
            elif num == 1:
                """好房APP小程序"""
                add_goods.houseApp(bys_houseApp, values_houseApp)
            else:
                """集团版小程序&好房APP小程序"""
                add_goods.houseApp(bys_houseApp, values_houseApp)
                add_goods.companyApp(bys_companyApp, values_companyApp)
            add_goods.goodsType(bys_goodsType, values_goodsType)
            add_goods.goodsTypeObject(bys_goodsTypeObject, values_goodsTypeObject)
            # 时间戳类型商品名称
            goodsName = excel[1]["goodsName"] + str(int(TestDateTime().time_stamp()))
            add_goods.goodsName(goodsName, bys_goodsName, values_goodsName)
            # 商品价格100以内的浮点数
            goodsPrices = TestRamdom().RandomTestFloat(100)
            add_goods.goodsPrices(str(goodsPrices), bys_goodsPrice, values_goodsPrice)
            # 商品导入数量
            # goodsLeading_in = SystemOs().sys_path(self.childCofigLeading_inEcxel())
            # print("goodsLeading_in",goodsLeading_in)
            # xls=xlsxoper(goodsLeading_in)
            # p =xls.readerXLS()
            # xls.writeXLS(p[0])
            # add_goods.goodstemplate(goodsLeading_in,bys_goodsExcel,values_goodsExcel)
            # 消耗积分
            goodsPoints = TestRamdom().RandomTestInt(10)
            add_goods.goodsPoints(str(goodsPoints), bys_goodsPoints, values_goodsPoints)
            # 点击上架时间
            add_goods.goodsTime(bys_goodsTimes, values_goodsTimes)
            add_goods.beginDay_Clear(bys_beginday, values_beginday)
            add_goods.beginDay(beginDay, bys_beginday, values_beginday)
            add_goods.beginDayClick(bys_begintimes, values_begintimes)
            add_goods.beginBack(beginTimes, bys_begintimes, values_begintimes)
            add_goods.beginTimes(beginTimes, bys_begintimes, values_begintimes)
            add_goods.endDayBack(endDay, bys_endday, values_endday)
            add_goods.endDay(endDay, bys_endday, values_endday)
            add_goods.endTimesBack(endTimes, bys_endTimes, values_endTimes)
            add_goods.endTimes(endTimes, bys_endTimes, values_endTimes)
            add_goods.trueTime(bys_trueTimes, values_trueTimes)
            # 商品图片
            goodsImg = SystemOs().sys_path(self.childConfigPublicImg(), excel[1]["goodsImg"])
            add_goods.goodsImg(goodsImg, bys_goodsImg, values_goodsImg)
            # 商品介绍
            jsGoodsInfo = values_goodsInfo % (excel[1]["goodsInfo"] + str(TestDateTime().local_time()))
            add_goods.goodsInfo(jsGoodsInfo)
            # 退货须知
            jsGoodsReject = values_goodsReject % (excel[1]["goodsReject"] + str(TestDateTime().local_time()))
            add_goods.goodsRejected(jsGoodsReject)
            # 创建并上架
            add_goods.goodsTrue(bys_goodstrue, values_goodstrue)
            add_goods.goodsTure1(bys_goodstrue1, values_goodstrue1)
            # 返回驱动
            driver = add_goods.base.get_driver()
            return driver
        except Exception:
            img_path = self.childConfigImgPath()
            add_goods.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())