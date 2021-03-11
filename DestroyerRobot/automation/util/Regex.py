#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:15
# @Author  : vivid
# @FileName: Regex.py
# @Software: PyCharm
# @email    ：331597811@QQ.com

import re


class Reg:
    # 正则表达式匹配标记
    iRegexFlag = re.S | re.I | re.M

    # 设置 [使.匹配包括换行在内的所有字符]
    def SetDotAll(bVal):
        global iRegexFlag
        iRegexFlag = (iRegexFlag | re.S) if bVal else (iRegexFlag & ~re.S)

    # 设置 [使匹配对大小写不敏感]
    def SetIgnoreCase(bVal):
        global iRegexFlag
        iRegexFlag = (iRegexFlag | re.I) if bVal else (iRegexFlag & ~re.I)

    # 设置 [做本地化识别（locale-aware)匹配]
    def SetLocale(bVal):
        global iRegexFlag
        iRegexFlag = (iRegexFlag | re.L) if bVal else (iRegexFlag & ~re.L)

    # 设置 [多行匹配，影响^和$]
    def SetMutexLine(bVal):
        global iRegexFlag
        iRegexFlag = (iRegexFlag | re.M) if bVal else (iRegexFlag & ~re.M)

    # 设置 [更灵活的格式以便将正则表达式写得更易于理解]
    def SetVerbose(bVal):
        global iRegexFlag
        iRegexFlag = (iRegexFlag | re.X) if bVal else (iRegexFlag & ~re.X)

    # 设置 [根据Unicode字符集解析字符，这个标志影响\w,\W,\b,\B]
    def SetUnicode(bVal):
        global iRegexFlag
        iRegexFlag = (iRegexFlag | re.U) if bVal else (iRegexFlag & ~re.U)



    # 正则表达式测试
    def Test(sText, sPattern):
        objPattern = re.compile(sPattern)
        objMatcher = re.search(objPattern, sText)
        if objMatcher == None:
            return False
        else:
            return True

    # 正则表达式查找
    def FindStr(sText, sPattern, iGroup = 0):
        try:
            objPattern = re.compile(sPattern, iRegexFlag)
            objMatcher = re.search(objPattern, sText)
            if objMatcher == None:
                return ""
            else:
                return objMatcher.group(iGroup)
        except:
            return ""

    # 正则表达式查找，返回找到的字符串和所有子串
    def Find(sText, sPattern):
        #try:
            objPattern = re.compile(sPattern, iRegexFlag)
            objMatcher = re.search(objPattern, sText)
            if objMatcher == None:
                return []
            else:
                arrRet = []
                arrRet.append(objMatcher.group(0))
                for s in objMatcher.groups():
                    arrRet.append(s)
                return arrRet
        #except:
            #return []

    # 正则表达式查找全部
    def FindAll(sText, sPattern):
        try:
            objPattern = re.compile(sPattern, iRegexFlag)
            return re.findall(objPattern, sText)
        except:
            return []

    # locust 关联
    def fetchStringByBoundary(self,data,LB=None,RB=None):
        rule =LB + r"(.*?)" + RB
        slotList = re.findall(rule,data)
        return slotList






# 测试代码
if __name__ == '__main__':
    # print("Test [成功] :", Reg().Test("我的手机号码是 : 13111111111，记住了吗？", "[0-9]+"))
    # print("Test [失败] :", Reg().Test("这是一段字符串", "找不到地"))
    # print("FindStr [全串] :", Reg().Test("我的手机号码是 : 13111111111，记住了吗？", "是 : ([0-9]+)"))
    # print("FindStr [子串] :", Reg().Test("我的手机号码是 : 13111111111，记住了吗？", "是 : ([0-9]+)", 1))
    # print("Find :", Reg().Find("我的手机号码是 : 13111111111，记住了吗？", "是 : ([0-9]+)"))
    # print("FindAll :",Reg().FindAll("我的手机号码是 : 13111111111，记住了吗？是 : 13222222222，这次记住了吗？是 : 13333333333，对了！", "(是 :) ([0-9]+)"))
    ss = "CREATE TABLE `easylife_broker_performance_confirmation_detail` (\
  `id` int(11) NOT NULL AUTO_INCREMENT,\
  `confirmation_id` int(11) NOT NULL,\
  `commission_id` int(11) NOT NULL COMMENT '佣金信息ID',\
  `commission_type` int(2) NOT NULL COMMENT '佣金类型（0老套餐 1新套餐）',\
  `commission_amount` decimal(20,2) NOT NULL COMMENT '佣金金额',\
  PRIMARY KEY (`id`)\
) ENGINE=InnoDB AUTO_INCREMENT=670 DEFAULT CHARSET=utf8mb4 "
    print(Reg().fetchStringByBoundary(ss,LB="COMMENT='",RB="'"))
