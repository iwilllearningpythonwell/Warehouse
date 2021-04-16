#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/9 15:45
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : interface_auto.test.py
import unittest
from BeautifulReport import  BeautifulReport
from DestroyerRobot.automation.util.LoggerUtil import  Log
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime


class testFileReport:
    def apis_yaml(self):
        conf = Config("ConfigApi")
        api_path = conf.get_configPath("public_data")
        api_yaml = SystemOs().sys_path(api_path)
        report = yamlUtil(api_yaml).get_yalm()
        report_path = SystemOs().sys_path(report['report'])
        test_path = SystemOs().sys_path(report['test_path'])
        # 0 报告地址 ， 1 测试数据集地址
        return report_path,test_path








if __name__ == '__main__':
    tf = testFileReport().apis_yaml()
    report_dir = SystemOs().sys_path(tf[0],TestDateTime().local_day())
    SystemOs().mkdirs_file(report_dir) #按照日期创建测试报告目录
    discover = unittest.defaultTestLoader.discover(tf[1], 'test_*.py', None)
    filename = '测试报告'+str(TestDateTime().report_file())
    BeautifulReport(discover).report(description='测试', filename=filename, report_dir=report_dir)