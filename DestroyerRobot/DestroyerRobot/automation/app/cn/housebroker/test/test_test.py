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
#from DestroyerRobot.automation.app.cn.base.capability_android import Capability
from DestroyerRobot.automation.app.cn.base.capability import Capability

from DestroyerRobot.automation.app.cn.housebroker.test.test_ljp import test_Estate

@ddt
class test_B(unittest.TestCase):

    """
    修改原型在测试类中的数据操作，
    通过配置文件获取数据集，
    """
    global datas,excel_title
    capp = Config("ConfigApp").get_configPath("B_Android")
    #capp = Config("ConfigApp").get_configPath("B_app")
    datas = yamlUtil(SystemOs().sys_path(capp)).get_yalm()




    def setUp(self):
        """
        获取驱动
        :return:
        """
        self.driver = Capability(datas).app_driver()


    def tearDown(self):
        self.driver.quit()


    def test_01(self):
        te =test_Estate(self.driver)
        te.test_dev_List()







if __name__=='__main__':
    unittest.main()