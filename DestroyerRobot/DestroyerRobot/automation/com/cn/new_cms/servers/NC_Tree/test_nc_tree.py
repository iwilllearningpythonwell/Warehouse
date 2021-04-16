
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_Tree.nc_Tree import MPTree
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from selenium import webdriver
import traceback
class test_nctree_master:
    def __init__(self,driver):
        """
        实现数据后，定位页面信息操作
        登录页面，操作数据
        """
        self.driver = driver

    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("new_cms_configs")
        return confFile

    def childConfigXML(self,Pageskeyword,UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("basic_tree")
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


    def get_link_config_center(self):
        """
        配置中心
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "配置中心")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.config_center(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Standard_control(self):
        """
        标准管控
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "标准管控")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Standard_control(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Contract_Center(self):
        """
        合约中心
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "合约中心")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Contract_Center(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Content_center(self):
        """
        内容中心
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "内容中心")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Content_center(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Trading_Center(self):
        """
        交易中心
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("交易中心", "交易中心")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Trading_Center(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Financial_settlement(self):
        """
        财务结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "财务结算")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Financial_settlement(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Employee_settlement(self):
        """
        员工结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工结算")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Employee_settlement(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Data_center(self):
        """
        数据中心
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "数据中心")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Data_center(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Personnel_Center(self):
        """
        人力中心
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("人力中心", "人力中心")
        mptree = MPTree(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Personnel_Center(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 配置中心-->二级菜单

    def get_link_Basic_data(self):
        """
        基础数据
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "基础数据")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Basic_data(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Transaction_node(self):
        """
        成交节点
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "成交节点")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Transaction_node(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Interface_managers(self):
        """
        接口配置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "接口配置")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Interface_managers(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_kingdee_butt_joint(self):
        """
        金蝶对接
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "金蝶对接")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.kingdee_butt_joint(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Reject_settings(self):
        """
        驳回设置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "驳回设置")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Reject_settings(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 标准管控---二级菜单


    def get_link_Standard_management(self):
        """
        标准管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "标准管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Standard_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Cost_Settlement(self):
        """
        费用结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "费用结算")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Cost_Settlement(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    #  合约中心 -- 二级菜单

    def get_link_contract_parties_Manage(self):
        """
        签约方管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "签约方管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.contract_parties_Manage(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_contract_management(self):
        """
        合同管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "合同管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.contract_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_investment_Rule(self):
        """
        跟投规则
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "跟投规则")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.investment_Rule(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Follow_up_management(self):
        """
        跟投管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "跟投管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Follow_up_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 内容中心-二级菜单

    def get_link_Content_configuration(self):
        """
        内容配置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "内容配置")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Content_configuration(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Information_feedback(self):
        """
        资讯反馈
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "资讯反馈")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Information_feedback(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 交易中心 -- 二级菜单

    def get_link_customer_management(self):
        """
        客户管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("交易中心", "客户管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.customer_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_user_management(self):
        """
        用户管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("交易中心", "用户管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.user_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 财务结算-- 二级菜单

    def get_link_Payment_plate(self):
        """
        支付板块
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "支付板块")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Payment_plate(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Performance_management(self):
        """
        业绩管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "业绩管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Performance_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Commission_audit(self):
        """
        佣金审核
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "佣金审核")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Commission_audit(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Reward_management(self):
        """
        奖励管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "奖励管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Reward_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Restitution_expenditure(self):
        """
        返还支出
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "返还支出")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Restitution_expenditure(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Group_award_settlement(self):
        """
        团奖结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "团奖结算")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Group_award_settlement(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Settlement_payment(self):
        """
        结算支付
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "结算支付")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Settlement_payment(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 员工结算 -- 二级菜单

    def get_link_Sub_Commission(self):
        """
        分佣设置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "分佣设置")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Sub_Commission(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Staff_management(self):
        """
        员工管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Staff_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Settlement_standard(self):
        """
        结算标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "结算标准")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Settlement_standard(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Reference_standard(self):
        """
        计提标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "计提标准")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Reference_standard(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Performance_settlement(self):
        """
        业绩结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "业绩结算")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Performance_settlement(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Internal_incentive(self):
        """
        内部激励
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "内部激励")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Internal_incentive(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Report_query(self):
        """
        报表查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "报表查询")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Report_query(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 数据中心 -- 二级菜单

    def get_link_Data_aggregation(self):
        """
        数据汇总
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "数据汇总")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Data_aggregation(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 人力中心 -- 二级菜单

    def get_link_Attendance_management(self):
        """
        考勤管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("人力中心", "考勤管理")
        mptree = MPTree(self.driver)
        try :
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Attendance_management(bys_points,values_points)
            mpdriver =mptree.base.get_driver()
            return mpdriver
        except Exception :
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())
