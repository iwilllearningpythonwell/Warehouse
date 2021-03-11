from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_Tree.MPTree import MPTree
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
import traceback
import os
import time

class NCTransferAudit:
    def __init__(self,driver):
        self.page = BasePage(driver)

    # def oper(self,bys,values):
    #     NC_Tree(self.page).points_managers(bys,values)
    def points_managers(self,bys,values):
        """
        积分管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.page.getElementByElement(bys,values)
        self.page.click(ele)

    def get_elements(self,bys,values):
        ele = self.page.getElementByElements(bys, values)
        self.page.click(ele[7])

    def input_banknum(self,bys,values):
        ele = self.page.getElementByElements(bys, values)
        self.page.sendkeys(ele[2], "4")

    def input_customer_name(self,bys,values):
        ele = self.page.getElementByElements(bys, values)
        self.page.sendkeys(ele[0], "123")

    def opera(self,js1):
        self.page.get_js(js1)
        self.page.implicitly_wait()

    def upload_pic(self,bys,values):
        ele = self.page.getElementByElement(bys, values)
        self.page.sendkeys(ele, "C:\\Users\lyg\Pictures\Saved Pictures\pic.jpg")



    # def audit(self,bys,values):
    #     ele = self.page.getElementByElements(bys, values)
    #     for i in range(len(ele)):
    #         self.page.click(ele[i])
    #         time.sleep(2)
    #         test_NCTransferAudit().uploadPic()
    #         print("hjj")
    #
    #         test_NCTransferAudit.auditPass()
    #         time.sleep(2)
    #         test_NCTransferAudit.search()
    #         # self.page.refresh()

    '''
    单条数据的审核
    def audit(self,bys,values):
        ele = self.page.getElementByElement(bys, values)
        # for i in range(len(ele)):
        self.page.click(ele)
    '''
