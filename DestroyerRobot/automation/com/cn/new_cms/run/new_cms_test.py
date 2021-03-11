#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/4
# @Author  : hopsonxw
# @FileName: new_cms_test.py
# @Software: PyCharm
# @email    ：190135@lifeat.cn
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ExcelUtil2 import DoExcel
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPLoing import test_mplogin
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPLoing.MPLogin import MPLoing
import traceback
import time
from selenium import webdriver
class paylist_test:

    def __init__(self, driver):
        """
        实现数据后，定位页面信息操作
        首页页面，操作元素
        """
        self.driver = driver

    def rootConfigURL(self):
        # 从主配置文件Config中获取URL
        conf1 = Config("URL")
        url = conf1.get_url_config('cms_new')
        return url

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("new_cms_config")
        return confFile

    def childConfigXlsx(self,sheet,dictData):
        # "获取子配置文件中信息",loginXlsx
        confFile = self.rootChildConfigPath()
        config1= Config("XlsxFilePath",confFile)
        loginXlsx = config1.get_path_config("user_login")
        loginXlsx = SystemOs().sys_path(loginXlsx)
        #dictData = {"userName": 3, "password": 4, "expected": 6}
        excelUtil = DoExcel(loginXlsx, sheet).do_excel(**dictData)
        return excelUtil


    def childConfigXML(self,Pageskeyword,UIElementkeyword):
        # "获取子配置文件中信息",loginXml
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("uilogin")
        filepath = SystemOs().sys_path(filepath)
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls

    def paylist(self):
        # 获取XML中相关信息
        bys_button0, values_button0 = test_mplogin.mplogin_test.childConfigXML("结算支付管理", "待支付清单")
        bys_button1, values_button1 = test_mplogin.mplogin_test.childConfigXML("待支付清单", "全部")
        bys_button2, values_button2 = test_mplogin.mplogin_test.childConfigXML("待支付清单", "已付款")
        bys_button3, values_button3 = test_mplogin.mplogin_test.childConfigXML("待支付清单", "未付款")
        bys_button4, values_button4 = test_mplogin.mplogin_test.childConfigXML("待支付清单", "推送失败")
        bys_button5, values_button5 = test_mplogin.mplogin_test.childConfigXML("待支付清单", "支付失败")

        check__button = MPLoing(self.driver)
        try:
            check__button.input_click(bys_button0, values_button0)
            time.sleep(3)
            check__button.input_click(bys_button1, values_button1)
            time.sleep(3)
            check__button.input_click(bys_button2, values_button2)
            time.sleep(3)
            check__button.input_click(bys_button3, values_button3)
            time.sleep(3)
            check__button.input_click(bys_button4, values_button4)
            time.sleep(3)
            check__button.input_click(bys_button5, values_button5)
            time.sleep(3)
            return check__button

        except Exception:
            img_path = self.childConfigImgPath()
            check__button.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


if __name__=='__main__':
    driver =webdriver.Chrome()
    # click_paylist_button = test_mplogin.mplogin_test(driver).test_login()

    paylist_test.paylist(driver)