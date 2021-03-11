# _*_ coding: utf-8 _*_

# @Time         : 2019-03-17 19:20
# @Author        : 路培强
# @Email         : 136024009@qq.com
# @File          :Base.py
# @Software      :PyCharm

from selenium import webdriver
from DestroyerRobot.automation.com.cn.util.UIElementUtil import UiElement
from DestroyerRobot.automation.com.cn.util.LoggerUtil import Log
from DestroyerRobot.automation.com.cn.util.SystemOsUtil import SystemOs
import unittest
import time


class TestBeforeAndAfter(unittest.TestCase):
    """
    测试前后处理
    """

    @classmethod
    def setUpClass(cls):
        """
        测试执行前执行
        classmethod是用来指定一个类的方法为类方法，没有此参数指定的类的方法为实例方法
        :return:
        """
        print("Start test!!!")

    #     print("Start test!!!")

    @classmethod
    def tearDownClass(cls):
        """
        所有测试执行完后执行
        :return:
        """
        print("Sleep 3S,stop test!!!")
        time.sleep(3)
        Base().quit()


class Driver:
    def __init__(self):

        pass
    def driver(self):
        driver = webdriver.Chrome()
        return driver


class Base(TestBeforeAndAfter):
    """
    集成一些常用方法
    """
    driver = Driver().driver()
    logger = Log().logger()
    #ui = UiElement(driver, logger)

    def save_img(self, img_name):
        """
        截图
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file("{}/{}.png".format(SystemOs().path("automation/run", "img"), img_name))

    def getElementByElement(self, page_keyword, ui_keyword):
        """
        返回定位的元素
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        self.logger.info("点击【%s】的【%s】元素", page_keyword, ui_keyword)
        return self.ui.getElementByKeyword(page_keyword, ui_keyword)

    def click(self, page_keyword, ui_keyword):
        """
        点击方法
        :param page_keyword:
        :param ui_keyword:
        :return:
        """
        self.logger.info("点击【%s】的【%s】元素", page_keyword, ui_keyword)
        self.ui.getElementByKeyword(page_keyword, ui_keyword).click()

    def sendkeys(self, page_keyword, ui_keyword, text):
        """
        输入方法
        :param page_keyword:
        :param ui_keyword:
        :param text:
        :return:
        """
        self.logger.info("对【%s】的【%s】元素输入【%s】", page_keyword, ui_keyword, text)
        self.ui.getElementByKeyword(page_keyword, ui_keyword).send_keys(text)

    def get_url(self, url):
        """
        打开url
        :param url:
        :return:
        """
        self.logger.info("打开url【%s】", url)
        self.driver.get(url)

    def quit(self):
        """
        关闭浏览器以及驱动
        :return:
        """
        self.driver.quit()

    def alert_accept(self):
        """
        操作alert弹窗
        :return:
        """
        alert = self.driver.switch_to_alert()
        alert.accept()

    def get_alert_text_and_accept(self):
        alert = self.driver.switch_to_alert()
        text = alert.text

        # alert.accept()
        return text

    def clearAndSendkeys(self, page_keyword, ui_keyword, text):
        """
        清空文本框值，然后输入新值
        :param page_keyword:
        :param ui_keyword:
        :param text:
        :return:
        """
        self.logger.info("清空【%s】的【%s】元素的值，然后输入【%s】", page_keyword, ui_keyword, text)
        element = self.ui.getElementByKeyword(page_keyword, ui_keyword)
        element.clear()
        element.send_keys(text)

    def sleep(self, s):
        """
        线程等待，偶尔会用到
        :param s:
        :return:
        """
        time.sleep(s)

    # def execute_script(self,page_keyword, ui_keyword, text):
    #     self.logger.info("使用js操作对【%s】的【%s】元素输入【%s】",page_keyword, ui_keyword, text )

if __name__=='__main__':
    driver = Driver()
    #driver.driver()