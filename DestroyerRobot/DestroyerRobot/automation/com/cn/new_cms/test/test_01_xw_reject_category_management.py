#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/29
# @Author  : hopsonxw
# @FileName: test_01_xw_area_management.py
# @Software: PyCharm
# @email    ：190135@lifeat.cn
from selenium import webdriver
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.test_NCLogin import Test_NCLogin
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.NCRejectCategoryManagement import NC_RejectCategoryManagement
import unittest

class test_reject_category_management(unittest.TestCase):
    """
     驳回原因类目管理实现
    """

    def test_manage_reject_category(self):

        """
        驳回类目
        :return:selenium
        """
        self.driver = webdriver.Chrome()
        ncmslogin = Test_NCLogin(self.driver)
        login_driver = ncmslogin.test_login_2()
        NC_RejectCategoryManagement(login_driver).add_reject_category()
        NC_RejectCategoryManagement(login_driver).search_reject_category()

if __name__ == '__main__':
    unittest.main()
