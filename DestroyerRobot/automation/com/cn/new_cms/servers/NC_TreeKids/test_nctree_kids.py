from selenium.webdriver import ActionChains
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_TreeKids.NCTreeKids import MPTreeKids
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from selenium import webdriver
import traceback
class test_nctree_kids:
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

    # 配置中心 -> 基础数据

    def get_link_Area_management(self):
        """
        片区管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "片区管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Area_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Bank_Data_management(self):
        """
        银行数据配置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "银行数据配置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Bank_Data_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 配置中心 -> 成交节点

    def get_link_Node_rule_settings(self):
        """
        节点规则管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "节点规则管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Node_rule_settings(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Settlement_Rules(self):
        """
        结佣规则管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "结佣规则管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Settlement_Rules(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 配置中心 -> 接口配置

    def get_link_Customer_State_Mapping(self):
        """
        客户状态映射
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "客户状态映射")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Customer_State_Mapping(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Project_mapping(self):
        """
        外部项目映射
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "外部项目映射")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_mapping(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Interface_mapping(self):
        """
        外部接口映射
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "外部接口映射")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Interface_mapping(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Kingdee_push_Management(self):
        """
        金蝶推送管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "金蝶推送管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Kingdee_push_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Auxiliary_Account_Mapping(self):
        """
        辅助账项目映射
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "辅助账项目映射")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Auxiliary_Account_Mapping(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_dev_Organizational_Relations(self):
        """
        楼盘映射组织关系
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "楼盘映射组织关系")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.dev_Organizational_Relations(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Auxiliary_Accounts_Mapping(self):
        """
        辅助账供应商映射
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "辅助账供应商映射")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Auxiliary_Accounts_Mapping(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Auxiliary_Account_Customer(self):
        """
        辅助账客户映射
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "辅助账客户映射")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Auxiliary_Account_Customer(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    # 配置中心 -- 驳回设置

    def get_link_Reject_Category_Management(self):
        """
        驳回类目管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("配置中心", "驳回类目管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Reject_Category_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Rejection_Cause_Management(self):
        """
        驳回原因管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("左侧导航栏", "驳回原因管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Rejection_Cause_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 标准管控 -- 标准管理


    def get_link_Project_Cooperation_Criteria(self):
        """
        项目合作标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "项目合作标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_Cooperation_Criteria(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Award_criteria(self):
        """
        团奖标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "团奖标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Award_criteria(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Commission_settlement_standard(self):
        """
        佣金结算标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "佣金结算标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Commission_settlement_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Cost_Control_Standard(self):
        """
        费用管控标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "费用管控标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Cost_Control_Standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_investment_Control_standard(self):
        """
        跟投管控标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "跟投管控标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.investment_Control_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 标准管控 -- 费用结算


    def get_link_Expense_settlement_management(self):
        """
        费用结算管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("标准管控", "费用结算管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Expense_settlement_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 合约中心 -- 签约方管理

    def get_link_legal_person_management(self):
        """
        内部法人管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "内部法人管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.legal_person_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Channel_brokerage_management(self):
        """
        渠道/经纪管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "渠道/经纪管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Channel_brokerage_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Developer_management(self):
        """
        开发商管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "开发商管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Developer_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 合约中心 -- 合同管理



    def get_link_Contract_signing_management(self):
        """
        合同签订管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "合同签订管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Contract_signing_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Termination_contract(self):
        """
        合同终止
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "合同终止")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Termination_contract(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Contract_enquiry(self):
        """
        合同查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "合同查询")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Contract_enquiry(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Contract_type_management(self):
        """
        合同类型管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "合同类型管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Contract_type_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Model_management(self):
        """
        范本管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "范本管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Model_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 合约中心 -- 跟投规则

    def get_link_investment_Allocation_rule(self):
        """
        跟投分配规则
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "跟投分配规则")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.investment_Allocation_rule(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Dividend_settlement_rule(self):
        """
        分红结算规则
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "分红结算规则")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Dividend_settlement_rule(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 合约中心 -- 跟投管理

    def get_link_investment_project_management(self):
        """
        跟投项目管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "跟投项目管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.investment_project_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_investment_Payment_management(self):
        """
        跟投支付管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "跟投支付管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.investment_Payment_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Transfer_remittance_examine(self):
        """
        转账汇款审核
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "转账汇款审核")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Transfer_remittance_examine(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Project_progress_view(self):
        """
        项目进展查看
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "项目进展查看")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_progress_view(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Project_liquidation(self):
        """
        项目清算管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "项目清算管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_liquidation(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_investment_Income_record(self):
        """
        跟投收益记录
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("合约中心", "跟投收益记录")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.investment_Income_record(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 内容中心 -- 内容配置


    def get_link_Homepage_Bullet_Window(self):
        """
        首页弹窗管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "首页弹窗管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Homepage_Bullet_Window(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Poster_Configuration(self):
        """
        海报配置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "海报配置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Poster_Configuration(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Live_Course_Management(self):
        """
        直播课程管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "直播课程管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Live_Course_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Announcement_config(self):
        """
        管家端公告配置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "管家端公告配置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Announcement_config(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Flash_screen_advertising(self):
        """
        闪屏广告
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "闪屏广告")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Flash_screen_advertising(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 内容中心 -- 资讯反馈

    def get_link_Topic_Page_Management(self):
        """
        专题页配置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("内容中心", "专题页配置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Topic_Page_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 交易中心 -- 客户管理


    def get_link_Customer_List(self):
        """
        客户列表
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("交易中心", "客户列表")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Customer_List(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())




    # 交易中心 -- 用户管理

    def get_link_User_List(self):
        """
        用户列表
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("交易中心", "用户列表")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.User_List(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 财务结算 -- 支付板块

    def get_link_Transfer_accounts_examine(self):
        """
        转账审核
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "转账审核")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Transfer_accounts_examine(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 财务结算 -- 业绩管理



    def get_link_Transaction_commission(self):
        """
        交易及佣金
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "交易及佣金")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Transaction_commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Payment_confirmation(self):
        """
        回款确认
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "回款确认")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Payment_confirmation(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 财务结算 -- 佣金审核


    def get_link_Broker_rewards(self):
        """
        经纪人奖励
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "经纪人奖励")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Broker_rewards(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Broker_Commission(self):
        """
        经纪人结佣
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "经纪人结佣")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Broker_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Broker_company_Commission(self):
        """
        经纪公司结佣
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "经纪公司结佣")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Broker_company_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_network_pusher_Commission(self):
        """
        网络推客结佣
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "网络推客结佣")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.network_pusher_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 财务结算 -- 奖励管理

    def get_link_shop_card_Commission(self):
        """
        购物卡结佣
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "购物卡结佣")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.shop_card_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_shop_card_category(self):
        """
        购物卡类别
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "购物卡类别")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.shop_card_category(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_shop_card_Stock(self):
        """
        购物卡库存
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "购物卡库存")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.shop_card_Stock(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_shop_card_query(self):
        """
        购物卡查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "购物卡查询")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.shop_card_query(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_shop_card_send(self):
        """
        购物卡发货
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "购物卡发货")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.shop_card_send(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 财务结算 -- 返还支出


    def get_link_Refund_inquiry(self):
        """
        返还款查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "返还款查询")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Refund_inquiry(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Refund_payment(self):
        """
        返还款支付
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "返还款支付")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Refund_payment(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 财务结算 -- 团奖结算


    def get_link_Group_award_statement(self):
        """
        团奖结算表
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "团奖结算表")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Group_award_statement(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Group_award_application(self):
        """
        团奖申请
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "团奖申请")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Group_award_application(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Group_award_Finance(self):
        """
        团奖申请-财务
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "团奖申请-财务")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Group_award_Finance(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 财务结算 -- 结算支付

    def get_link_List_pending_payments(self):
        """
        待支付清单
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "待支付清单")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.List_pending_payments(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Payment_List_Query(self):
        """
        支付清单查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "支付清单查询")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Payment_List_Query(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Settlement_Inquiry(self):
        """
        结算查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "结算查询")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Settlement_Inquiry(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Payment_settings(self):
        """
        支付设置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("财务结算", "支付设置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Payment_settings(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 员工结算 -- 分佣设置

    def get_link_Cooperative_Label_Management(self):
        """
        合作标签管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "合作标签管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Cooperative_Label_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Project_Commission_management(self):
        """
        项目分佣管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "项目分佣管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_Commission_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Project_Level_Management(self):
        """
        项目等级管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "项目等级管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_Level_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Project_Commission_Detail(self):
        """
        项目分佣比例明细
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "项目分佣比例明细")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Project_Commission_Detail(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 员工结算 -- 员工管理

    def get_link_Departmental_management(self):
        """
        部门管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "部门管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Departmental_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Business_Line_Management(self):
        """
        业务线管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "业务线管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Business_Line_Management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Post_management(self):
        """
        岗位管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "岗位管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Post_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Employee_management(self):
        """
        员工管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Employee_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 员工结算 -- 结算标准


    def get_link_Section_standard_setting(self):
        """
        区间标准设置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "区间标准设置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Section_standard_setting(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Transaction_settlement_standard(self):
        """
        成交结算标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "成交结算标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Transaction_settlement_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Revenue_settlement_standard(self):
        """
        营收结算标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "营收结算标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Revenue_settlement_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Profit_settlement_standard(self):
        """
        利润结算标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "利润结算标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Profit_settlement_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Profit_standard_setting(self):
        """
        利润标准设置
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "利润标准设置")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Profit_standard_setting(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Market_settlement_standard(self):
        """
        市场结算标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "市场结算标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Market_settlement_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 员工结算 -- 计提标准

    def get_link_commission_standard(self):
        """
        交易佣金标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "交易佣金标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.commission_standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Performance_incentive(self):
        """
        业绩激励标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "业绩激励标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Performance_incentive(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Profit_incentive(self):
        """
        利润激励标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "利润激励标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Profit_incentive(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Market_Commission_Standard(self):
        """
        市场佣金标准
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "市场佣金标准")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Market_Commission_Standard(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 员工结算 -- 业绩结算


    def get_link_Transaction_Settlement(self):
        """
        成交结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "成交结算")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Transaction_Settlement(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Revenue_Settlement_Month(self):
        """
        营收结算-月
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "营收结算-月")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Revenue_Settlement_Month(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Revenue_Settlement_Year(self):
        """
        营收结算-年
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "营收结算-年")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Revenue_Settlement_Year(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Profit_Settlement(self):
        """
        利润结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "利润结算")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Profit_Settlement(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Market_Settlement(self):
        """
        市场结算
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "市场结算")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Market_Settlement(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    # 员工结算 -- 内部激励


    def get_link_employee_Commission_Summary(self):
        """
        员工佣金发放总表
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工佣金发放总表")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.employee_Commission_Summary(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Market_Commission(self):
        """
        市场佣金
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "市场佣金")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Market_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Trading_Commission(self):
        """
        交易佣金
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "交易佣金")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Trading_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Employee_motivation_Month(self):
        """
        员工激励-月
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工激励-月")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Employee_motivation_Month(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Employee_motivation_Year(self):
        """
        员工激励-年
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工激励-年")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Employee_motivation_Year(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Profit_incentive_Year(self):
        """
        利润激励-年
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "利润激励-年")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Profit_incentive_Year(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 员工结算 -- 报表查询

    def get_link_Employee_Commission_Report_Query(self):
        """
        员工分佣报表查询
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("员工结算", "员工分佣报表查询")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Employee_Commission_Report_Query(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    # 数据中心 -- 数据汇总


    def get_link_Channel_Commission(self):
        """
        渠道佣金
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "渠道佣金")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Channel_Commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_easylife_Summary_commission(self):
        """
        好生活结佣汇总
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "好生活结佣汇总")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.easylife_Summary_commission(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_easylife_Pool_funds(self):
        """
        好生活资金池
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "好生活资金池")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.easylife_Pool_funds(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_Kpi_Index_management(self):
        """
        kpi指标管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "kpi指标管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Kpi_Index_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    def get_link_easylife_kpi_check(self):
        """
        好生活kpi考核
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "好生活kpi考核")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.easylife_kpi_check(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Rejection_pool(self):
        """
        驳回统计池
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("数据中心", "驳回统计池")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Rejection_pool(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())



    # 人力中心 -- 考勤管理


    def get_link_Personal_attendance_record(self):
        """
        个人考勤记录
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("人力中心", "个人考勤记录")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Personal_attendance_record(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Monthly_Attendance_Statistics(self):
        """
        考勤月度统计
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("人力中心", "考勤月度统计")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Monthly_Attendance_Statistics(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


    def get_link_Attendance_management(self):
        """
        考勤人员管理
        :return:
        """
        # 获取XML中相关信息
        bys_points, values_points = self.childConfigXML("人力中心", "考勤人员管理")
        mptree = MPTreeKids(self.driver)
        try:
            BasePage(self.driver).move_to_ele(bys_points, values_points)
            mptree.Attendance_management(bys_points, values_points)
            mpdriver = mptree.base.get_driver()
            return mpdriver
        except Exception:
            img_path = self.childConfigImgPath()
            mptree.base.save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())


