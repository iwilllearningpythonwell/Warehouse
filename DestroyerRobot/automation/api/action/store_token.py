#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 10:22
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : store_token.py
from DestroyerRobot.automation.util.LoggerUtil import Log
from DestroyerRobot.automation.util.YamlUtil import yamlUtil

class stort_token:
    """
    stort_token只是为了满足权限系统而作
    """

    def __init__(self,responseData,setApp,setpath,responseResult,istoken,token_value,Authorization):
        self.responseData = responseData
        self.istoken = istoken
        self.setpath = setpath
        self.setApp = setApp
        self.responseResult = responseResult
        self.tokenvalue =token_value
        self.Authorization = Authorization
        self.log = Log().logger()

    def token(self):
        #print(self.responseData,"\n\t",self.istoken ,"\n\t",self.setpath ,"\n\t", self.setApp ,"\n\t" ,self.responseResult ,"\n\t",self.tokenvalue ,"\n\t",self.Authorization )
        if self.istoken :
            if self.responseResult :
                if "data" in self.responseData.keys():
                    if self.responseData["data"] == None:
                        self.log.info("data层为null")
                    else:
                        if self.tokenvalue  in self.responseData['data'].keys():
                            reToken = self.responseData["data"][self.tokenvalue]
                            #在权限系统中生成"Bearer "+applicationToken 对应Authorization
                            reAuthorization = "Bearer "+self.responseData["data"]["applicationToken"]
                            self.log.info("reToken:%s" % reToken)
                            if self.setApp == 1 :
                                data = yamlUtil(self.setpath).get_yalm()
                                if self.tokenvalue in data.keys():
                                    yamlUtil(self.setpath).update_yaml(self.tokenvalue,reToken)
                                else:
                                    Token = {self.tokenvalue: reToken}
                                    yamlUtil(self.setpath).write_yaml(Token)
                                if self.Authorization in data.keys():
                                    yamlUtil(self.setpath).update_yaml(self.Authorization,reAuthorization)
                                else:
                                    Authorization = {self.Authorization: reAuthorization}
                                    yamlUtil(self.setpath).write_yaml(Authorization)
                            elif self.setApp == 2 :
                                data = yamlUtil(self.setpath).get_yalm()
                                if self.tokenvalue in data.keys():
                                    yamlUtil(self.setpath).update_yaml(self.tokenvalue,reToken)
                                else:
                                    reToken = {self.tokenvalue :  reToken}
                                    yamlUtil(self.setpath).write_yaml(reToken)
                        else:
                            self.log.info("登录没有返回token")
                else:
                    self.log.info("response没有data层")
            else:
                self.log.info("登录失败" )
        else:
            self.log.info("不是登录")

if __name__ == '__main__':
    responseData= {'code': 200, 'msg': '成功', 'data': {'token': 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiMTg3MTg3NTA0MDQiLCJpYXQiOjE2MTAwODUwOTUsImV4cCI6MTYxMDA5MjI5NSwibmJmIjoxNjEwMDg1MDk1fQ.2FU0jEfnCaMlVisqTF0KmrM-KbpUPtaxMvuccWQNHlg', 'applicationToken': 'eyJhbGciOiJIUzI1NiJ9.eyJ0ZW5hbnRfaWQiOiIyOCIsInVzZXJfaWQiOiIyMTUyIiwicGxhdGZvcm1faWQiOiIzIiwiaWF0IjoxNjEwMDg1MDk1LCJleHAiOjE2MTAwOTIyOTUsIm5iZiI6MTYxMDA4NTA5NX0.sbt8vqNlK308yNC_l2DZD8dJgPA-o86dty_QS3ESZYc', 'isDirectLogin': True, 'tenants': None, 'apps': [{'id': 3, 'appName': '新运营端管理系统', 'appIcon': '', 'appUrl': 'http://localhost:8089/,https://ndcms.lifeat.cn:45788/cms/,https://ntcms.lifeat.cn:45788/cms/,https://nhcms.lifeat.cn:45788/cms/,https://hb-ncms.lifeat.cn/cms/'}, {'id': 0, 'appName': '权限系统', 'appIcon': 'https://kf-pms-cdn.hopsontong.com/1585129410411-10947/cms/permission-system-logo-258x86.png', 'appUrl': 'https://uat-pms-tenant.hopsontong.com:11013/#/login'}]}, 'success': True}
    istoken= 1
    setpath = "C:/Users/vivid/PycharmProjects/untitled/DestroyerRobot/automation/api/config/header_cms.yaml "
    setApp = 1
    responseResult = 1
    tokenvalue = "token"
    Authorization = "Authorization"
    #responseData,setApp,setpath,responseResult,istoken,token_value,Authorization
    st = stort_token(responseData,istoken,setpath,setApp,responseResult,tokenvalue,Authorization)
    st.token()
