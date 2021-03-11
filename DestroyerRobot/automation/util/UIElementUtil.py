# _*_ coding: utf-8 _*_

# @Time         : 2019-04-06 19:54
# @Author        : 路培强
# @Email         : 136024009@qq.com
# @File          :UIElementUtil.py
# @Software      :PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#automation/automation/com/cn/util/XmlUtil.py
from DestroyerRobot.automation.util.XmlUtil import  XmlUtil

from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
import os


class Config:

    xml_filepath = SystemOs().sys_path("automation/datas", "UILibrary.xml")



class UiElement:
    def __init__(self, driver, logger):
        self.driver = driver
        self.Xml = XmlUtil(Config().xml_filepath)
        self.logger = logger


    def getVisibleElement(self, by, value):
        """
        根据by和value进行定位
        :param by:
        :param value:
        :return:
        """
        wait = WebDriverWait(self.driver, 20, 0.5)
        locator = None
        if by == "id":
            locator = (By.ID, value)
        elif by == "name":
            locator = (By.NAME, value)
        elif by == "className":
            locator = (By.CLASS_NAME, value)
        elif by == "tagName":
            locator = (By.TAG_NAME, value)
        elif by == "linkText":
            locator = (By.LINK_TEXT, value)
        elif by == "partialLinkText":
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif by == "cssSelector":
            locator = (By.CSS_SELECTOR, value)
        elif by == "xpath":
            locator = (By.XPATH, value)
        else:
            print("定位元素不存在", by, value)
        web_element = wait.until(EC.visibility_of_element_located(locator))
        return web_element

    def getElementByKeyword(self, page_keyword, ui_keyword):
        """
        根据传入的page_keyword与ui_keyword 从 UILibrary.xml 里找对应的by跟value
        :param page_keyword:要定位的页面
        :param ui_keyword:要定位的元素
        :return:返回定位方式以及定位用的值
        """
        by, value = self.Xml.xml_parsing(page_keyword, ui_keyword)
        self.logger.info("通过【%s】方式，值是【%s】定位【%s】的【%s】", by, value, page_keyword, ui_keyword)
        web_element = self.getVisibleElement(by, value)
        return web_element

    # def getElementJavaScripts(self,jscritps):
    #     pass

if __name__ == '__main__':
    conf = UiElement()
