#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/26 15:03
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : test_cms.py

import unittest
import time
from ddt import ddt,data,unpack
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.YamlUtil import yamlUtil
from DestroyerRobot.automation.util.ExcelUtil import xlsxoper
from DestroyerRobot.automation.util.LoggerUtil import Log
from DestroyerRobot.automation.util.HttpClient import HttpClient
from DestroyerRobot.automation.api.action.check_result import CheckResult
from DestroyerRobot.automation.api.action.store_token import stort_token
@ddt
class TestCase(unittest.TestCase):
    """
    全局变量中将excel中首行标题提取:testdata2 , yaml数据返回结果:datainfo
    新脚本中配置新的excel需要改写内容如下 ：对应新的配置文件信息
    global:全局变量
     file_path = SystemOs().sys_path(datainfo['file_path2'])
    testdata = xlsxoper(file_path).readerXLS_dict(datainfo['SheetName2'])[0]  # 数据用于ddt使用
    testdata2 = xlsxoper(file_path).readerXLS_dict(datainfo['SheetName2'])[1]  # 首行标题

    def:
    执行脚本对应的excel写入sheet
    xls = xlsxoper(file_path).writeXLS_dict(datas['caseNo'],column,str(responseData),datainfo['SheetName2'])

    """
    global  log , file_path,datainfo,testdata2
    log = Log().logger()
    conf = Config("ConfigApi")
    keys = conf.parsing_config("public_data")
    public_data = SystemOs().sys_path(keys) #通过主配置文件config获取主yaml配置文件路径-
    datainfo = yamlUtil(public_data).get_yalm()
    file_path = SystemOs().sys_path(datainfo['file_path2'])
    testdata = xlsxoper(file_path).readerXLS_dict(datainfo['SheetName2'])[0]  # 数据用于ddt使用
    testdata2 = xlsxoper(file_path).readerXLS_dict(datainfo['SheetName2'])[1]  # 首行标题


    #*testdata 只获取数据
    @data(*testdata)
    def test_01_demo(self, datas):
        """
        接口测试
        :param datas: 从yaml文件中获取excel路径，读取数据集，通过ddt形式
        """

        isSkip = datas['isSkip'] #获取excle中isSkip
        if isSkip == 'y':
            log.info("当isSkip==y跳过此条用例")
        else:
            #print("datas:",datas)
            webapp = datas['setApp']
            setApp=datainfo[webapp]      #获取excel中设备类型setApp是网页还是手机
            log.info('setApp: %s ',setApp)
            setpath = SystemOs().sys_path(setApp) #获取yaml子配置文件路径信息如：C:/Users/vivid/PycharmProjects/untitled/DestroyerRobot/yaml_file/header_cms.yaml
            header = yamlUtil(setpath).get_yalm() #获取header信息
            url = datainfo[datas['domain']]+datas['requestUrl']
            #"请求方式= %s",datas['method'],"请求参数= %s",datas['param'] "请求格式= %s",datas['paramType'],"请求头部信息= %s",header
            log.info("请求地址= %s ",url)
            # log.info("请求方式= %s",datas['method'])
            # log.info("请求格式= %s",datas['paramType'])
            # log.info("请求头部信息= %s",header)
            responseData = HttpClient().request(datas['method'],url,datas['paramType'],datas['param'],header) #实际结果
            log.info("实际响应结果：%s",responseData)
            responseResult = CheckResult.check(responseData, datas["exceptResponse"])
            log.info("判断预期结果与实际结果是否一致：0 为 False 1 为 True = %s ",responseResult)
            # 判断是否将token写入yaml对应的文件中
            stort_token(responseData,webapp,setpath,responseResult,datas['istoken'],datainfo['token'],datainfo['Authorization']).token()
            #查找CASE_trueResponse中value值对应excel的列位置
            column = testdata2.index(datainfo['CASE_trueResponse'])
            # 写入excel中
            log.info("将实际响应结果集数据写入excel中对应列" )
            #写入excel数据必须是字符串，不能是dict
            xls = xlsxoper(file_path).writeXLS_dict(datas['caseNo'],column,str(responseData),datainfo['SheetName2'])
            time.sleep(1)




if __name__ == '__main__':
    unittest.main()
