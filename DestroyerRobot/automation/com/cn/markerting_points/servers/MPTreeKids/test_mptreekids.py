#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/8/27
# @Author  : vivid-XIEMENG
# @FileName: test_mptreekids.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPTreeKids.MPTreeKids import MPTreeKids
import traceback
class test_mptreekids:
    """
    子tree
    """
    def __init__(self,driver):
        self.driver = driver

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("markerting_points_configs")
        return confFile

    def childConfigXML(self, Pageskeyword, UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("uimptreekids")
        filepath = SystemOs().sys_path(filepath)
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls

    def childConfigImgPath(self):
        """
        获取图片路径，并新建以日期为基础的文件目录名 例如： img/2019-01-01/
        :return:
        """
        confFile = self.rootChildConfigPath()
        config3 = Config("ImgPath", confFile)
        img_path = config3.get_path_config("error_img")
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(img_path, data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

###############积分规则 start #############
    def get_points_rule(self):
        """
        积分规则
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "积分规则")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.points_rule(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_points_rule_small_routine(self):
        """
        积分规则(小程序)
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "积分规则(小程序)")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.points_rule_small_routine(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_points_change(self):
        """
        调整积分
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "调整积分")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.points_change(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_points_change_small_routine(self):
        """
        调整积分(小程序)
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "调整积分(小程序)")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.points_change_small_routine(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

##########积分规则 end############

##########营销管理 start #########
    def get_markering_actions(self):
        """
        营销活动管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "营销活动管理")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.markering_actions(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_markering_prices(self):
        """
        奖品管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "奖品管理")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.markering_prices(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())
##########营销管理 end ############

##########积分商城 start ##########

    def get_points_goods(self):
        """
        积分商品
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "积分商品")

        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.points_goods(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_points_order(self):
        """
        积分订单
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("积分子列表", "积分订单")
        mPTreeKids = MPTreeKids(self.driver)
        try:
            mPTreeKids.points_order(bys_points, values_points)
            mpdriver = mPTreeKids.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mPTreeKids.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())
##########积分商城 end ##########