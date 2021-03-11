#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 11:08
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : test_myinfo.py
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
import traceback
from DestroyerRobot.automation.app.cn.Customer.servers.myinfo.myinfo import MyInfo
class test_myinfo:
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


    def myinfo_path_info(self):
        """
        通过yaml配置文件获取到data.yaml配置信息，data是文件存放路径
        :return: myinfo 返回的是字典形式信息，excel & xml
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
        myinfo_path = self.myinfo_path_info()
        filepath = SystemOs().sys_path(myinfo_path["myinfo"]["xml"]) #获取xml绝对路径
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls


    def myinfo_img(self):
        """
        通过yaml配置文件获取到Cuscomfig.yaml配置信息,img是图片存放地址
        :return:
        """
        datas = self.rootChildConfigPath()
        myinfo_img = SystemOs().sys_path(datas["img"])
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(myinfo_img, data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

    def logsing_info(self):
        """
        首页点击【注册|登录】，进入登录页面
        :return: 返回当前驱动
        """
        lg_info , lg_use = self.read_xml("我的","注册登录") #获取xml中【注册登录】信息
        lginfo =  MyInfo(self.driver)
        try:
            lginfo.click_loginsing(lg_info, lg_use) #点击首页中【我的】页面元素
            return lginfo.base.get_driver() #返回驱动
        except Exception:
            img_path = self.myinfo_img()
            lginfo.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

