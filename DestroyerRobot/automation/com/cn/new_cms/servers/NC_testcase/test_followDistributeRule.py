from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_testcase.NCTransferAudit import  NCTransferAudit
import traceback
import time

class TestFollowDistributeRules:
    def __init__(self,driver):
        self.driver=driver

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("new_cms_configs")
        return confFile

    def childConfigXML(self, Pageskeyword, UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("ncmsTree")
        filepath = SystemOs().sys_path(filepath)
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls

    # test_mptree().childConfigImgPath()
    def childConfigImgPath(self):
        """
        获取图片路径，并新建以日期为基础的文件目录名 例如： img/2019-01-01/
        :return:
        """
        confFile = self.rootChildConfigPath()
        config3 = Config("ImgPath",confFile)
        img_path = config3.get_path_config("error_img")
        data_path = TestDateTime().local_day()
        img_path = SystemOs().sys_path(img_path,data_path)
        SystemOs().mkdirs_file(img_path)
        return img_path

    def operation(self):
        js2="document.getElementsByClassName('el-menu-vertical-demo el-menu')[0].style='transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1); transition-duration: 0ms; transform: translate(0px, -557px) scale(1) translateZ(0px);'"
        print(type(js2))
        NCTransferAudit(self.driver).opera(js2)

    def newRule(self):

        dis=NCTransferAudit(self.driver)
        bys_pAudit1, values_pAudit1 = self.childConfigXML("跟投管理菜单", "跟投管理")
        bys_pAudit2, values_pAudit2 = self.childConfigXML("跟投管理菜单", "跟投规则管理")
        bys_pAudit3, values_pAudit3 = self.childConfigXML("跟投管理菜单", "跟投分配规则")

        try:
            dis.points_managers(bys_pAudit1,values_pAudit1)
            time.sleep(2)
            dis.points_managers(bys_pAudit2,values_pAudit2)
            time.sleep(2)
            dis.points_managers(bys_pAudit3,values_pAudit3)
            time.sleep(2)

        except Exception:
            print(traceback.format_exc())
