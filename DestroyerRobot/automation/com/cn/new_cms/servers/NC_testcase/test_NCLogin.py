from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.ExcelUtil2 import DoExcel
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.NCLogin import NCLoing
import traceback
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.test_nclogin import nclogin_test

class Test_NCLogin:
    def __init__(self,driver):
        self.driver=driver

    def rootConfigURL(self):
        config1=Config("URL")
        ncurl=config1.get_url_config("cms_new")
        return ncurl

    def rootChildConfigPath(self):
        config2=Config("ConfigKIDs")
        confFile = config2.get_configPath("new_cms_configs")
        return confFile

    def childConfigXlsx(self,sheet,dictData):
         configFile=self.rootChildConfigPath()
         config=Config("XlsxFilePath",configFile)  #
         loginXlsx = config.get_path_config("ncms_login")
         loginXlsx=SystemOs().sys_path(loginXlsx)
         excel=DoExcel(loginXlsx,sheet).do_excel(**dictData)
         return excel

    # mplogin_test().childConfigXML()
    # mplogin_test().childConfigImgPath()
    # mplogin_test().test_login()
    def childConfigXML(self,Pageskeyword,UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("uilogin")
        filepath = SystemOs().sys_path(filepath)
        xmlspath = XmlUtil(filepath)
        # 获取XML中相关信息
        xmls = xmlspath.xml_parsing(Pageskeyword, UIElementkeyword)
        return xmls

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

    def test_login(self):
        url = self.rootConfigURL()
        # "获取子配置文件中信息",loginXlsx
        dictData = {"userName": 3, "password": 4, "expected": 6}
        excel = self.childConfigXlsx("sheet1", dictData)

        # 获取XML中相关信息
        bys_moblie, values_mobile = self.childConfigXML("登录页面", "用户")
        bys_password, values_password = self.childConfigXML("登录页面", "密码")
        # print(bys_password , values_password)
        bys_login, values_login = self.childConfigXML("登录页面", "登录按钮")

        nc_login = NCLoing(self.driver)
        try:
            nc_login.base.get_url(url)
            nc_login.base.maximize_window()
            nc_login.input_mobile(excel[0]["userName"],bys_moblie,values_mobile)
            nc_login.input_password(excel[0]["password"],bys_password,values_password)
            nc_login.input_click(bys_login,values_login)

            driver = nc_login.base.get_driver()
            return  driver
        except Exception :
            img_path =self.childConfigImgPath()
            nc_login.base.save_img(img_path,str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def test_login(self):
        url = self.rootConfigURL()
        # "获取子配置文件中信息",loginXlsx
        dictData = {"userName": 3, "password": 4, "expected": 6}
        excel = self.childConfigXlsx("sheet1", dictData)

        # 获取XML中相关信息
        bys_moblie, values_mobile = self.childConfigXML("登录页面", "用户")
        bys_password, values_password = self.childConfigXML("登录页面", "密码")
        # print(bys_password , values_password)
        bys_login, values_login = self.childConfigXML("登录页面", "登录按钮")

        nc_login = NCLoing(self.driver)
        try:
            nc_login.base.get_url(url)
            nc_login.base.maximize_window()
            nc_login.input_mobile(excel[0]["userName"],bys_moblie,values_mobile)
            nc_login.input_password(excel[0]["password"],bys_password,values_password)
            nc_login.input_click(bys_login,values_login)

            driver = nc_login.base.get_driver()
            return  driver
        except Exception :
            img_path =self.childConfigImgPath()
            nc_login.base.save_img(img_path,str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def test_login_2(self):
        url = self.rootConfigURL()
        # "获取子配置文件中信息",loginXlsx
        dictData = {"userName": 3, "password": 4, "expected": 6}
        excel = self.childConfigXlsx("sheet1", dictData)

        # 获取XML中相关信息
        bys_moblie, values_mobile = self.childConfigXML("登录页面", "用户")
        bys_password, values_password = self.childConfigXML("登录页面", "密码")
        # print(bys_password , values_password)
        bys_login, values_login = self.childConfigXML("登录页面", "登录按钮")

        nc_login = NCLoing(self.driver)
        try:
            nc_login.base.get_url(url)
            nc_login.base.maximize_window()
            nc_login.input_mobile(excel[1]["userName"],bys_moblie,values_mobile)
            nc_login.input_password(excel[1]["password"],bys_password,values_password)
            nc_login.input_click(bys_login,values_login)

            driver = nc_login.base.get_driver()
            return  driver
        except Exception :
            img_path =self.childConfigImgPath()
            nc_login.base.save_img(img_path,str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

