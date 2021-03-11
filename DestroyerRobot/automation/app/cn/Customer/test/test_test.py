#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/19 11:40
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : test_test.py
import unittest
from ddt import  ddt,data,unpack
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.ExcelUtil import xlsxoper
from DestroyerRobot.automation.app.cn.base.capability import Capability
from DestroyerRobot.automation.app.cn.Customer.servers.indexpage.test_indexpage import test_indexpage
from DestroyerRobot.automation.app.cn.Customer.servers.firstpage.test_firstpage import test_firstpage
@ddt
class test_C(unittest.TestCase):

    """
    修改原型在测试类中的数据操作，
    通过配置文件获取数据集，
    """
    global datas,excel_title
    capp = Config("ConfigApp").get_configPath("C_app")
    datas = yamlUtil(SystemOs().sys_path(capp)).get_yalm()
    data_yaml = SystemOs().sys_path(datas["data"])
    login_path = yamlUtil(data_yaml).get_yalm()

    filepath = SystemOs().sys_path(login_path["login"]["excel"])
    excel_datas = xlsxoper(filepath).readerXLS_dict("Sheet1")[0] #读取login.xlxs中的数据信息
    excel_title = xlsxoper(filepath).readerXLS_dict("Sheet1")[1] #读取login.xlxs中的头部信息



    def setUp(self):
        """
        获取驱动
        :return:
        """
        self.driver = Capability(datas).app_driver()


    # def tearDown(self):
    #     self.driver.quit()

    def test_01_indexpage(self):
        """
        用户进入首页
        :return:
        """
        index_p = test_indexpage(self.driver)
        index_p.indexpage_index() #进入首页获取驱动

    def test_02_firstpage(self):
        index_p = test_indexpage(self.driver)
        index_driver = index_p.indexpage_index()  # 进入首页获取驱动
        first_p = test_firstpage(index_driver)
        first_p.mypage_info() #进入【我的】页面,返回驱动





if __name__=='__main__':
    unittest.main()
