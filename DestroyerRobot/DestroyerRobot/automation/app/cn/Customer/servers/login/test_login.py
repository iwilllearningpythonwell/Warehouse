#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/26 16:00
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : test_login.py

from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ExcelUtil import xlsxoper
import traceback
from DestroyerRobot.automation.app.cn.Customer.servers.login.login import Login
class test_login:
    def __init__(self,driver,datas):
        """
        获取驱动
        :param driver:
        """
        self.driver = driver
        self.datas = datas

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件yaml信息
        Capp = Config("ConfigApp").get_configPath("C_app")
        Capp_path = SystemOs().sys_path(Capp)
        data = yamlUtil(Capp_path).get_yalm()
        return data


    def login_path_info(self):
        """
        通过yaml配置文件获取到data.yaml配置信息，data是文件存放路径
        :return: firstpage 返回的是字典形式信息，excel & xml
        """
        datas = self.rootChildConfigPath()
        data_yaml = SystemOs().sys_path(datas["data"])
        login_path = yamlUtil(data_yaml).get_yalm()
        return login_path


    def read_xml(self,Pageskeyword,UIElementkeyword):
        """
        获取data.yaml "firstpage"信息-->指向xml,读取xml中相关的配置信息
        :param Pageskeyword: 如：首页
        :param UIElementkeyword: 如： 客户管理
        :return:
        """
        login_path = self.login_path_info()
        filepath = SystemOs().sys_path(login_path["login"]["xml"]) #获取xml绝对路径
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
    #     login_path = self.login_path_info()
    #     filepath = SystemOs().sys_path(login_path["login"]["excel"]) #获取excel绝对路径
    #     excel = xlsxoper(filepath).readerXLS_dict("Sheet1") #默认Sheet1可以不写入
    #     return excel



    def login_img(self):
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
        login_click , login_use = self.read_xml("登录","账号密码登录") #获取xml中【账号密码登录】信息
        phone_info , phone_use = self.read_xml("登录","手机号") #获取xml中【手机号】信息
        pwd_info , pwd_use = self.read_xml("登录","密码") #获取xml中【密码】信息
        # login_excel = self.read_excel()
        logins =  Login(self.driver)
        try:
            logins.click_tvPassLogin(login_click, login_use) #点击首页中【我的】页面元素
            logins.input_tvPhoneNum(phone_info,phone_use,self.datas["iphonenum"])
            logins.input_tvPassword(pwd_info,pwd_use,self.datas["Password"])
            return logins.base.get_driver() #返回驱动
        except Exception:
            img_path = self.login_img()
            logins.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


if __name__ == '__main__':
    login =test_login(1)
    datas = login.read_excel()
    print(datas[0])