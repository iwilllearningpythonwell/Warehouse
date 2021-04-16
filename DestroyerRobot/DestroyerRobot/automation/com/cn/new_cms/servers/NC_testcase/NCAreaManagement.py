#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/10/28
# @Author  : hopsonxw
# @FileName: NCAreaManagement.py
# @Software: PyCharm
# @email    ：190135@lifeat.cn
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_Tree.test_nc_tree import test_nctree_master
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_TreeKids.test_nctree_kids import test_nctree_kids
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.NCLogin import NCLoing
from DestroyerRobot.automation.util.RandomUtil import TestRamdom
from DestroyerRobot.automation.util.MySqlDBUtil import MysqlDB
import traceback
import time

class NC_AreaManagement:
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
        confFile = conf2.get_configPath("new_cms_configs")
        return confFile

    def childConfigXML(self, Pageskeyword, UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("area_management")
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
        config3 = Config("ImgPath",confFile)
        img_path = config3.get_path_config("error_img")
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(img_path,data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

    def add_area(self):
        add_btn_bys,add_btn_values = self.childConfigXML('片区管理','新增')
        input_area_bys,input_area_values = self.childConfigXML('片区管理','输入片区名称')
        input_part_bys, input_part_values = self.childConfigXML('片区管理', '选择归属区域')
        select_part_bys, select_part_values = self.childConfigXML('片区管理', '归属区域下拉选项')
        select_province_bys, select_province_values = self.childConfigXML('片区管理', '关联省份')
        select_city_bys, select_city_values = self.childConfigXML('片区管理', '关联城市')
        select_county_bys, select_county_values = self.childConfigXML('片区管理', '关联区县')
        save_btn_bys,save_btn_values = self.childConfigXML('片区管理','保存')
        nc = NCLoing(self.driver)
        try:
            test_nctree_master(self.driver).get_link_config_center()  # 点击配置中心
            test_nctree_master(self.driver).get_link_Basic_data()     # 点击基础数据
            test_nctree_kids(self.driver).get_link_Area_management()    # 点击片区管理
            nc.input_click(add_btn_bys,add_btn_values)  # 点击新增片区
            radom_num = TestRamdom().RandomTestInt(500,0)
            area_name = 'xw_AutoTest_片区'+ str(radom_num)

            nc.Input_z(area_name,input_area_bys,input_area_values)    # 输入片区名称
            nc.input_click(input_part_bys,input_part_values)    # 点击展开归属区域下拉选项
            nc.input_click(select_part_bys,select_part_values)   # 选择归属区域
            time.sleep(6)
            nc.input_click_z(select_province_bys, select_province_values)  # 选择省份
            time.sleep(2)
            nc.input_click_o(select_city_bys, select_city_values)   # 选择城市
            nc.input_click_t(select_county_bys, select_county_values)  # 选择区县
            time.sleep(2)
            nc.input_click(save_btn_bys,save_btn_values)  # 保存
            time.sleep(2)

            return area_name

            # # 连接测试数据库，获取最新创建的部门名称(获取的名称没有按顺序排列，放弃此方法)
            # my = MysqlDB()
            # my.getCursor(sqltable="easylife_commallot")
            # sql = "SELECT department_name FROM commallot_staff_department"
            # department = my.queryOperation(sql)
            # print(department)
            # return department

        except Exception:
            img_path = self.childConfigImgPath()
            BasePage(self.driver).save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())
