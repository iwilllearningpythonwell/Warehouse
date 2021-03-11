#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/14
# @Author  : vivid-XIEMENG
# @FileName: NCLogin.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import time

from selenium.webdriver import ActionChains

from DestroyerRobot.automation.com.cn.base.BasePage import BasePage

class NCLoing():
    """
    实现定位操作
    新运营后台，登录页面定位内容
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
        self.base.move_to_ele(bys, values)  # 页面移到所选元素位置
        self.base.click(ele)

    def input_click_z(self,bys,values):   # 第0个 zero
        ele = self.base.getElementByElements(bys,values)
        self.base.click(ele[0])

    def input_click_o(self,bys,values):   # 第1个 one
        ele = self.base.getElementByElements(bys,values)
        self.base.click(ele[1])

    def input_click_t(self,bys,values):   # 第2个 two
        ele = self.base.getElementByElements(bys,values)
        self.base.click(ele[2])

    def input_click_six(self,bys,values):   # 第6个 six
        ele = self.base.getElementByElements(bys,values)
        self.base.click(ele[6])

    def Input(self,parm,bys,values):
        ele = self.base.getElementByElement(bys,values)
        self.base.sendkeys(ele,parm)


    def Input_z(self,parm,bys,values):  # 第0个 zero
        ele = self.base.getElementByElements(bys,values)
        self.base.sendkeys(ele[0],parm)

    def Input_o(self,parm,bys,values):  # 第1个 one
        ele = self.base.getElementByElements(bys,values)
        self.base.sendkeys(ele[1],parm)

    def Input_t(self,parm,bys,values):  # 第2个 two
        ele = self.base.getElementByElements(bys,values)
        self.base.sendkeys(ele[2],parm)

    def Input_th(self, parm, bys, values):  # 第3个 three
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[3], parm)

    def Input_f(self, parm, bys, values):  # 第4个 four
        ele = self.base.getElementByElements(bys, values)
        self.base.sendkeys(ele[4], parm)

    def Clear_o(self,bys,values):   # 第1个 one
        ele = self.base.getElementByElements(bys,values)
        self.base.clear(ele[1])

    def get_current_url(self):
        print(self.base.get_current_url())


if __name__ == '__main__':
    mp = NCLoing()
    mp.base.get_url("https://ntcms.lifeat.cn:45788/cms/#/login")
    mp.base.maximize_window()
    mptitle = mp.base.title()
    print(mptitle)
    mp.input_mobile()
    mp.input_password()
    mp.input_click()
    mp.get_current_url()



