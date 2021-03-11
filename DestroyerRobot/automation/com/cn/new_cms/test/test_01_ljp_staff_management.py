#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/15
# @Author  : vivid-XIEMENG
# @FileName: TestBaidu.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from selenium import webdriver
from BeautifulReport import BeautifulReport
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.test_nclogin import nclogin_test
#from DestroyerRobot.automation.com.cn.new_cms.servers.NC_Tree.test_mptree import test_mptree
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.test_NCLogin import Test_NCLogin
#from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.test_NCTransferAudit import test_NCTransferAudit
#from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.test_followDistributeRule import TestFollowDistributeRules
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.test_staff_Management import test_NC_StaffManagement
import unittest
import time
class test_login(unittest.TestCase):
    """
    实现unittest操作，到 run目录运行对应脚本操作
    BeautifulReport记录操作失败截图报告
    """
    def setUp(self):
        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.quit()
    '''
    # @BeautifulReport.add_test_img('test_01_mplogin')#失败后会有报告截图
    # def test_01_mplogin(self):
    #     """
    #     用户登录
    #     :return:
    #     """
    #     mplogin = mplogin_test(self.driver)
    #     mplogin.test_login()

    @BeautifulReport.add_test_img('test_02_mptree')  # 失败后会有报告截图
    def test_02_mptree(self):
        """
        用户登录点击积分商城
        :return:
        """
        mplogin = mplogin_test(self.driver)
        login_drivers = mplogin.test_login()
        mptree = test_mptree(login_drivers)
        mptree.get_link_points_shopping()
    

    @BeautifulReport.add_test_img('test_03_ncmslogin')  # 失败后会有报告截图
    def test_03_ncmslogin(self):
        """
              用户登录新运营后台
        """
        mplogin =Test_NCLogin(self.driver)
        mplogin.test_login()

    @BeautifulReport.add_test_img('test_04_ncmslogin')  # 失败后会有报告截图
    def test_04_ncmsTransferAudit(self):
        """
              银行转账审核
        """
        mplogin = Test_NCLogin(self.driver)
        login_driver=mplogin.test_login()
        test_NCTransferAudit(login_driver).operation()
        # test_NCTransferAudit(login_driver).mouse_op()
        # test_NCTransferAudit(login_driver).execute_script("document.querySelector('.bscroll-indicator').scrollTop=10000")
        time.sleep(3)
        print("拖动滚动条成功")
        test_NCTransferAudit(login_driver).get_parent_transfer_audit()

    def test_05_ncmsFollowDistributeRules(self):
        
        跟投分配规则
        :return:
        
        mplogin = Test_NCLogin(self.driver)
        login_driver = mplogin.test_login()
        test_NCTransferAudit(login_driver).operation()
        TestFollowDistributeRules(login_driver).newRule()
    '''

    def test_06_ncms_staff_management(self):
        '''
        员工管理
        :return:selenium
        '''
        mplogin = Test_NCLogin(self.driver)
        login_driver = mplogin.test_login()
        test_NC_StaffManagement(login_driver).add_Department()
        test_NC_StaffManagement(login_driver).add_Business_line()
        test_NC_StaffManagement(login_driver).add_staff_station()


if __name__=='__main__':
    unittest.main()
