#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/6 11:26
# @Author  : vivid
# @FileName: capability.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from appium import webdriver
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
class Capability:
    def __init__(self,dataYaml):
        self.dataYaml = dataYaml

    def getCapability(self):
        desired_caps = {}
        desired_caps['platformName'] = str(self.dataYaml['platformName'])
        desired_caps['platformVersion'] = str(self.dataYaml['platformVersion'])
        desired_caps['udid'] = self.dataYaml['udid']
        #app地址需要修改，将app相关的apk包放到应用程序中
        desired_caps['app'] = SystemOs().sys_path(self.dataYaml['app'])
        desired_caps['appPackage'] = self.dataYaml['appPackage']
        desired_caps['appActivity'] = self.dataYaml['appActivity']
        desired_caps['noReset'] = self.dataYaml['noReset']
        # send_keys()传入中文时需要在capability中配置如下内容：
        desired_caps['unicodeKeyboard'] = self.dataYaml['unicodeKeyboard']
        # 隐藏键盘
        desired_caps['resetKeyboard'] = self.dataYaml['resetKeyboard']
        # 支持toast操作
        desired_caps['automationName'] = self.dataYaml['automationName']


        return desired_caps

    def app_driver(self):
        desired_cap = self.getCapability()
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        return driver

if __name__ == '__main__':
    file = "D:\\AutoTestTeamm\\DestroyerRobot\\DestroyerRobot\\automation\\app\\cn\\housebroker\\config\\borkerconfig.yaml"
    datayaml = yamlUtil(file).get_yalm()
    Capability(datayaml).app_driver()