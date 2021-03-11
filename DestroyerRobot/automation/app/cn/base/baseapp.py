#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/4 16:17
# @Author  : vivid
# @FileName: baseapp.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
from DestroyerRobot.automation.util.LoggerUtil import Log
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import time

class BaseApp:
    logger = Log().logger()
    def __init__(self,driver):
        self.driver = driver
        self.TouchAction = TouchAction(driver) #滑动操作


    def implicitly_wait(self):
        time.sleep(2)
        self.driver.implicitly_wait(10)

    def getElementByElement(self, page_keyword, ui_keyword):
        """
        返回定位的单个元素
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        try:
            self.logger.info("查找【%s】的【%s】元素", page_keyword, ui_keyword)
            self.implicitly_wait()
            element =self.driver.find_element(page_keyword, ui_keyword)
        except NoSuchElementException:
            self.logger.info('页面元素不存在')
        else:
            return element

    def getElementByElements(self, page_keyword, ui_keyword):
        """
        返回定位的单个元素
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        try:
            self.logger.info("查找【%s】的【%s】元素", page_keyword, ui_keyword)
            self.implicitly_wait()
            elements = self.driver.find_elements(page_keyword, ui_keyword)
        except NoSuchElementException:
            self.logger.info('页面元素不存在')
        else:
            return elements

    def click(self, driver_ele):
        """
        判断页面元素是否存在，存在点击
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        driver_ele.click()

    def sendkeys(self,elements,ele_value):
        """
        判断页面元素是否存在，如果存在输入信息
        :param elements:
        :param ele_value:
        :return:
        """
        self.clear(elements)
        self.implicitly_wait()
        elements.send_keys(ele_value)
    def clear(self,driver_ele):
        """
        清除缓存信息
        :param driver_ele:
        :return:
        """
        driver_ele.clear()
    def save_img(self,img_path,time_stamp):
        """
        截图
        :img_path :图片路径
        :time_stamp: 获取时间格式
        :return:
        """
        self.implicitly_wait()
        self.driver.get_screenshot_as_file("%s/error%s.png" %(img_path,time_stamp))

    def get_text(self,driver_ele):
        """
        获取文本内容
        :param driver_ele:  driver_ele = self.driver.find_elements(page_keyword, ui_keyword)
        :return:
        """
        self.logger.info("获取文本内容【%s】", driver_ele.text)
        self.implicitly_wait()
        return driver_ele.text

    def get_size(self):
        """
        获取手机屏幕尺寸
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    #修改刘建培新增内容
    def swipes(self,x1,y1,x2,y2,times):
        """
        输入滑动信息
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param times:
        :return:
        """
        self.implicitly_wait()
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向左滑动屏幕 刘建培新增
    def swipe_Left(self,  t=1000, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)


    def swipLeft(self):
        """
        左滑
        :return:
        """
        self.implicitly_wait()
        appsize = self.get_size()
        x1 = int(appsize[0]*0.9)
        y1 = int(appsize[1]*0.5)
        x2 = int(appsize[0]*0.1)
        self.driver.swipe(x1,y1,x2,y1,1000)

    # 向上滑动屏幕 刘建培新增
    def swipe_Up(self, t=1000, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.75  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


    def swipeUp(self):
        """
        上滑
        :return:
        """
        self.implicitly_wait()
        appsize = self.get_size()
        x1 = int(appsize[0] * 0.5)
        y1 = int(appsize[1] * 0.9)
        y2 = int(appsize[1] * 0.35)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 向下滑动屏幕 刘建培新增
    def swipe_Down(self,  t=1000, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driver.swipe(x1, y1, x1, y2, t)


    def swipeDown(self):
        """
        下滑
        :return:
        """
        self.implicitly_wait()
        appsize = self.get_size()
        x1 = int(appsize[0] * 0.5)
        y1 = int(appsize[1] * 0.35)
        y2 = int(appsize[1] * 0.85)
        self.driver.swipe(x1, y1, x1, y2, 1000)

    # 向右滑动屏幕 刘建培新增
    def swip_Right(self,  t=1000, n=1):
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driver.swipe(x1, y1, x2, y1, t)


    def swipeRight(self):
        """
        右滑
        :return:
        """
        self.implicitly_wait()
        appsize = self.get_size()
        y1 = int(appsize[1] * 0.5)
        x1 = int(appsize[0] * 0.25)
        x2 = int(appsize[0] * 0.9)
        self.driver.swipe(x1, y1, x2, y1, 1000)


    def get_driver(self):
        """
        返回当前驱动
        :return:
        """
        self.logger.info("返回当前驱动")
        self.implicitly_wait()
        return self.driver

    def press_keycode(self,nums):
        """
        调用键盘操作
        :param num:
        :return:
        """
        self.driver.press_keycode(nums)

    def page_source(self):
        """
        获取页面源码
        :return:
        """
        return self.driver.page_source

    def isElementExist(self, By, value):
        flag = True
        if By == 'xpath':
            try:
                self.driver.find_element_by_xpath(value)
            except:
                flag = False
        elif By == "id":
            try:
                self.driver.find_element_by_id(value)
            except:
                flag = False
        return flag

    def back(self):
        self.driver.back()

    def getattribut(self,driver_ele, value):
        """
        获取元素中属性
        #ele = self.driver.find_element(page_keyword, ui_keyword)
        #ele = self.driver.find_elements(page_keyword, ui_keyword)
        #ele[0].get_attribute(value)
        :return:
        """
        self.implicitly_wait()
        self.logger.info("获取元素中属性【%s】", driver_ele.get_attribute(value))
        return self.driver_ele.get_attribute(value)

    def current_activity(self):
        """
        获取当前activity
        :return:
        """
        current_activity = self.driver.current_activity
        return current_activity

    def MultiAction_add(self,action1,action2):
        """
        MultiAction多点触控操作，需要获取self.TouchAction属性方法
        :param action1: action1=TouchAction(driver) | action1.press(x=x*0.2,y=y*0.2).wait(1000).move_to(x=x*0.4,y=y*0.4).wait(1000).release()
        :param action2:
        :return:
        """
        self.multiaction = MultiAction(self.driver)
        self.multiaction.add(action1,action2)
        self.multiaction.perform()