#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/14
# @Author  : vivid-XIEMENG
# @FileName: MPLogin.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import time

from DestroyerRobot.automation.com.cn.base.BasePage import BasePage

class MPLoing():
    """
    实现定位操作
    积分营销后台，登录页面定位内容
    """
    def __init__(self,driver):
        self.base = BasePage(driver)

    def input_mobile(self,username,bys,values):
        ele = self.base.getElementByElements(bys,values)
        self.base.sendkeys(ele[0],username)

    def input_password(self,password,bys,values):
        ele = self.base.getElementByElements(bys,values)
        self.base.sendkeys(ele[1],password)

    def input_click(self,bys,values):
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    # def get_current_url(self):
    #     print(self.base.get_current_url())


if __name__ == '__main__':
    mp = MPLoing()
    mp.base.get_url("https://tcms.lifeat.cn:45788/#/login")
    mp.base.maximize_window()
    mptitle = mp.base.title()
    print(mptitle)
    mp.input_mobile()
    mp.input_password()
    mp.input_click()
    mp.get_current_url()



