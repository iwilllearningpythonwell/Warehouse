#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 16:37
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : test_firstpage.py

from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
import traceback
from DestroyerRobot.automation.app.cn.Customer.servers.firstpage.firstpage import FirstPage
class test_firstpage:
    def __init__(self,driver):
        """
        获取驱动
        :param driver:
        """
        self.driver = driver

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件yaml信息
        Capp = Config("ConfigApp").get_configPath("C_app")
        Capp_path = SystemOs().sys_path(Capp)
        data = yamlUtil(Capp_path).get_yalm()
        return data


    def firstpage_path_info(self):
        """
        通过yaml配置文件获取到data.yaml配置信息，data是文件存放路径
        :return: firstpage 返回的是字典形式信息，excel & xml
        """
        datas = self.rootChildConfigPath()
        data_yaml = SystemOs().sys_path(datas["data"])
        firstpage_path = yamlUtil(data_yaml).get_yalm()
        return firstpage_path


    def read_xml(self,Pageskeyword,UIElementkeyword):
        """
        获取data.yaml "firstpage"信息-->指向xml,读取xml中相关的配置信息
        :param Pageskeyword: 如：首页
        :param UIElementkeyword: 如： 客户管理
        :return:
        """
        firstpage_path = self.firstpage_path_info()
        filepath = SystemOs().sys_path(firstpage_path["firstpage"]["xml"]) #获取xml绝对路径
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls


    # def read_excel(self):
    #     """
    #     数据集放到test方法中可以使用 @ddt,放到此处使用for循环，也可以将整个数据集做出全局变量，但不能引用unittest无法使用assert
    #     获取data.yaml "firstpage"信息-->指向excel,读取excel中相关的数据
    #     :return: 返回内容包含:数据和首行信息
    #     """
    #     firstpage_path = self.firstpage_path_info()
    #     filepath = SystemOs().sys_path(firstpage_path["indexpage"]["excel"]) #获取excel绝对路径
    #     excel = xlsxoper(filepath).readerXLS_dict("Sheet1") #默认Sheet1可以不写入
    #     return excel



    def firstpage_img(self):
        """
        通过yaml配置文件获取到Cuscomfig.yaml配置信息,img是图片存放地址
        :return:
        """
        datas = self.rootChildConfigPath()
        firstpage_img = SystemOs().sys_path(datas["img"])
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(firstpage_img, data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

    def mypage_info(self):
        """
        首页点击【我的】，进入我的页面
        :return: 返回当前驱动
        """
        my_info , my_use = self.read_xml("首页","我的") #获取xml中【我的】信息
        myinfo =  FirstPage(self.driver)
        try:
            myinfo.my_info(my_info, my_use) #点击首页中【我的】页面元素
            return myinfo.base.get_driver() #返回驱动
        except Exception:
            img_path = self.firstpage_img()
            myinfo.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def lookHousepage_info(self):
        """
        首页点击【看房】，
        :return:
        """
        lh_info, lh_use = self.read_xml("首页","看房")
        lhinfo = FirstPage(self.driver)
        try:
            lhinfo.lh_info(lh_info, lh_use) #点击首页中【我的】页面元素
            return lhinfo.base.get_driver() #返回驱动
        except Exception:
            img_path = self.firstpage_img()
            lhinfo.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

