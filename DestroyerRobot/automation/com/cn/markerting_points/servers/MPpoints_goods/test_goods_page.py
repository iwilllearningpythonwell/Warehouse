#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/9/2
# @Author  : vivid-XIEMENG
# @FileName: test_goods_page.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.markerting_points.servers.MPpoints_goods.Goods_page import Goods_page
import traceback
class test_goods_page():
    def __init__(self,driver):
        """
        实现数据后，定位页面信息操作
        登录页面，操作数据
        """
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
        filepath = config2.get_path_config("uigoods")
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

    def get_link_points_managers(self):
        """
        积分管理
        :return:
        """
        # 获取XML中相关信息

        bys_points, values_points = self.childConfigXML("商品页面", "新建商品")
        print(bys_points,values_points)
        goods_page = Goods_page(self.driver)
        try:
            goods_page.add_goods(bys_points, values_points)
            mpdriver = goods_page.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            goods_page.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())