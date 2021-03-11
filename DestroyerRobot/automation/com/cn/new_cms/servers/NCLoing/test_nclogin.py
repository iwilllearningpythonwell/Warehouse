#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/27
# @Author  : vivid-XIEMENG
# @FileName: test_nclogin.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ExcelUtil2 import DoExcel
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.NCLogin import NCLoing
import traceback
class nclogin_test:
    def __init__(self,driver):
        """
        实现数据后，定位页面信息操作
        登录页面，操作数据
        """
        self.driver = driver


    def rootConfigURL(self):
        # 从主配置文件Config中获取URL
        conf1 = Config("URL")
        url = conf1.get_url_config("cms_new")
        return url

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("new_cms_configs")
        return confFile

    def childConfigXlsx(self,sheet,dictData):
        # "获取子配置文件中信息",loginXlsx
        confFile = self.rootChildConfigPath()
        config1= Config("XlsxFilePath",confFile)
        loginXlsx = config1.get_path_config("user_login")
        loginXlsx = SystemOs().sys_path(loginXlsx)
        #dictData = {"userName": 3, "password": 4, "expected": 6}
        excelUtil = DoExcel(loginXlsx, sheet).do_excel(**dictData)
        return excelUtil


    def childConfigXML(self,Pageskeyword,UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("uilogin")
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

    def test_login(self):
        url = self.rootConfigURL()
        # "获取子配置文件中信息",loginXlsx
        dictData = {"userName": 3, "password": 4, "expected": 6}
        excel = self.childConfigXlsx("sheet1", dictData)

        # 获取XML中相关信息
        bys_moblie, values_mobile = self.childConfigXML("登录页面", "用户")
        bys_password, values_password = self.childConfigXML("登录页面", "密码")
        # print(bys_password , values_password)
        bys_login, values_login = self.childConfigXML("登录页面", "登录按钮")

        nc_login = NCLoing(self.driver)
        try:
            nc_login.base.get_url(url)
            nc_login.base.maximize_window()
            nc_login.input_mobile(excel[0]["userName"],bys_moblie,values_mobile)
            nc_login.input_password(excel[0]["password"],bys_password,values_password)

            nc_login.input_click(bys_login,values_login)
            driver = nc_login.base.get_driver()
            return  driver
        except Exception :
            img_path =self.childConfigImgPath()
            nc_login.base.save_img(img_path,str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())