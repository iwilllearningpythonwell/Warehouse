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

class NC_RejectCategoryManagement:
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
        filepath = config2.get_path_config("reject_category_management")
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

     # 新增驳回分类
    def add_reject_category(self):
        add_btn_bys,add_btn_values = self.childConfigXML('驳回类目管理_增','新增')
        input_rjmdl_bys,input_rjmdl_values = self.childConfigXML('驳回类目管理_增','驳回模块选择')
        select_rjmdl_bys, select_rjmdl_values = self.childConfigXML('驳回类目管理_增', '驳回模块下拉选项')
        input_rjctgr_bys, input_rjctgr_values = self.childConfigXML('驳回类目管理_增', '输入驳回分类')
        save_btn_bys, save_btn_values = self.childConfigXML('驳回类目管理_增', '保存')
        confirm_btn_bys,confirm_btn_values = self.childConfigXML('驳回类目管理_增', '保存成功确认弹窗')

        nc = NCLoing(self.driver)
        try:
            test_nctree_master(self.driver).get_link_config_center()  # 点击配置中心
            test_nctree_master(self.driver).get_link_Reject_settings()     # 点击驳回设置
            test_nctree_kids(self.driver).get_link_Reject_Category_Management()    # 点击驳回类目管理
            nc.input_click(add_btn_bys,add_btn_values)  # 点击新增驳回分类
            radom_num = TestRamdom().RandomTestInt(500,0)
            reject_category_name = 'xw_AutoTest_驳回分类'+ str(radom_num)

            nc.input_click_t(input_rjmdl_bys,input_rjmdl_values)    # 点击展开驳回模块下拉选项
            nc.input_click(select_rjmdl_bys,select_rjmdl_values)   # 选择驳回模块
            nc.Input(reject_category_name,input_rjctgr_bys,input_rjctgr_values)    # 输入驳回分类名称
            nc.input_click(save_btn_bys,save_btn_values)  # 保存
            time.sleep(2)
            nc.input_click_o(confirm_btn_bys,confirm_btn_values)    # 关闭保存成功弹窗
            time.sleep(3)

            return reject_category_name

        except Exception:
            img_path = self.childConfigImgPath()
            BasePage(self.driver).save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

     # 查询分类
    def search_reject_category(self):
            input_condition_bys, input_condition_values = self.childConfigXML('驳回类目管理_查', '查询条件')
            select_condition_bys, select_condition_values = self.childConfigXML('驳回类目管理_查', '选择查询条件')
            search_btn_bys, search_btn_values = self.childConfigXML('驳回类目管理_查', '查询')
            nc = NCLoing(self.driver)
            try:
                # test_nctree_master(self.driver).get_link_config_center()  # 点击配置中心
                # test_nctree_master(self.driver).get_link_Reject_settings()  # 点击驳回设置
                # test_nctree_kids(self.driver).get_link_Reject_Category_Management()  # 点击驳回类目管理
                # nc.input_click(add_btn_bys, add_btn_values)  # 点击新增驳回分类
                # radom_num = TestRamdom().RandomTestInt(500, 0)
                # reject_category_name = 'xw_AutoTest_驳回分类' + str(radom_num)

                nc.input_click(input_condition_bys, input_condition_values)  # 点击展开查询条件下拉选项
                nc.input_click_six(select_condition_bys, select_condition_values)  # 选择查询条件
                time.sleep(2)
                nc.input_click(search_btn_bys, search_btn_values)  # 点击查询
                time.sleep(5)

                return

            except Exception:
                img_path = self.childConfigImgPath()
                BasePage(self.driver).save_img(img_path, str(int(TestDateTime().time_stamp())))
                print(traceback.format_exc())

