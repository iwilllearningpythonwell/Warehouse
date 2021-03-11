#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/15
# @Author  : vivid-XIEMENG
# @FileName: TestBaidu.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from selenium import webdriver
from BeautifulReport import BeautifulReport
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPLoing.test_mplogin import mplogin_test
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTree.test_mptree import test_mptree
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTreeKids.test_mptreekids import test_mptreekids
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPpoints_goods.test_goods_page import test_goods_page
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPpoints_goods.test_add_goods import test_add_goods
import unittest


class test_login(unittest.TestCase):
    """
    实现unittest操作，到 run目录运行对应脚本操作
    BeautifulReport记录操作失败截图报告
    """
    def setUp(self):

        self.driver = webdriver.Chrome()


    def tearDown(self):
        self.driver.quit()


    @BeautifulReport.add_test_img('test_01_mplogin')#失败后会有报告截图
    def test_01_mplogin(self):
        """
        用户登录
        :return:
        """
        mplogin = mplogin_test(self.driver)
        mplogin.test_login()

    # @BeautifulReport.add_test_img('test_02_mptree')  # 失败后会有报告截图
    # def test_02_mptree(self):
    #     """
    #     用户登录点击积分商城
    #     :return:
    #     """
    #     mplogin = mplogin_test(self.driver)
    #     login_drivers = mplogin.test_login()
    #     mptree = test_mptree(login_drivers)
    #     mptree.get_link_points_shopping()

    # @BeautifulReport.add_test_img('test_03_mpaddgoods')
    # def test_03_mpaddgoods(self):
    #     """
    #     创建积分商品(实物)
    #     :return:
    #     """
    #     mplogin = mplogin_test(self.driver)
    #     login_drivers = mplogin.test_login()
    #     mptree = test_mptree(login_drivers)
    #     mptree_driver =mptree.get_link_points_shopping()
    #     points_goods=test_mptreekids(mptree_driver)
    #     points_goods_driver=points_goods.get_points_goods()
    #     addGoods=test_goods_page(points_goods_driver)
    #     addGoods_driver=addGoods.get_link_points_managers()
    #     test_add_goods(addGoods_driver).set_goodsObject()

    # @BeautifulReport.add_test_img('test_04_mpaddgoods')
    # def test_04_mpaddgoods(self):
    #     """
    #     创建积分商品(虚拟)
    #     :return:
    #     """
    #     mplogin = mplogin_test(self.driver)
    #     login_drivers = mplogin.test_login()
    #     mptree = test_mptree(login_drivers)
    #     mptree_driver = mptree.get_link_points_shopping()
    #     points_goods = test_mptreekids(mptree_driver)
    #     points_goods_driver = points_goods.get_points_goods()
    #     addGoods = test_goods_page(points_goods_driver)
    #     addGoods_driver = addGoods.get_link_points_managers()
    #     test_add_goods(addGoods_driver).set_goodsVR()





if __name__=='__main__':
    unittest.main()
