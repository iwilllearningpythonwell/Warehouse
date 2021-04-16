#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/29
# @Author  : hopsonxw
# @FileName: test_01_xw_area_management.py
# @Software: PyCharm
# @email    ：190135@lifeat.cn
from selenium import webdriver
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.test_NCLogin import Test_NCLogin
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.NCAreaManagement import NC_AreaManagement
import unittest

class test_area_management(unittest.TestCase):
    """
     片区管理实现
    """

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #
    # def tearDown(self):
    #     self.driver.quit()

    def test_01_ncms_area_management(self):

        """
        片区管理新增片区
        :return:selenium
        """

        self.driver = webdriver.Chrome()
        ncmslogin = Test_NCLogin(self.driver)
        login_driver = ncmslogin.test_login_2()
        NC_AreaManagement(login_driver).add_area()

if __name__ == '__main__':
    unittest.main()
