
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
class MPTree:
    def __init__(self,driver):
        """
        获取驱动
        """
        self.base = BasePage(driver)

    def config_center(self,bys,values):
        """
        配置中心
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Standard_control(self,bys,values):
        """
        标准管控
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Contract_Center(self,bys,values):
        """
        合约中心
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Content_center(self,bys,values):
        """
        内容中心
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Trading_Center(self,bys,values):
        """
        交易中心
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Financial_settlement(self,bys,values):
        """
        财务结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Employee_settlement(self,bys,values):
        """
        员工结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Data_center(self,bys,values):
        """
        数据中心
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Personnel_Center(self,bys,values):
        """
        人力中心
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 配置中心-->二级菜单

    def Basic_data(self,bys,values):
        """
        基础数据
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Transaction_node(self,bys,values):
        """
        成交节点
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Interface_managers(self,bys,values):
        """
        接口配置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def kingdee_butt_joint(self,bys,values):
        """
        金蝶对接
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Reject_settings(self,bys,values):
        """
        驳回设置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

     # 标准管控--子菜单

    def Standard_management(self,bys,values):
        """
        标准管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Cost_Settlement(self,bys,values):
        """
        费用结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    #  合约中心--- 子菜单

    def contract_parties_Manage(self,bys,values):
        """
        签约方管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def contract_management(self,bys,values):
        """
        合同管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def investment_Rule(self,bys,values):
        """
        跟投规则
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Follow_up_management(self,bys,values):
        """
        跟投管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 内容中心 - 二级菜单

    def Content_configuration(self,bys,values):
        """
        内容配置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Information_feedback(self,bys,values):
        """
        资讯反馈
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 交易中心 -- 二级菜单

    def customer_management(self,bys,values):
        """
        客户管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def user_management(self, bys, values):
        """
        用户管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)


    # 财务结算-- 二级菜单

    def Payment_plate(self, bys, values):
        """
        支付板块
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def Performance_management(self, bys, values):
        """
        业绩管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def Commission_audit(self, bys, values):
        """
        佣金审核
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def Reward_management(self, bys, values):
        """
        奖励管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)

    def Restitution_expenditure(self, bys, values):
        """
        返还支出
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys, values)
        self.base.click(ele)


    def Group_award_settlement(self,bys,values):
        """
        团奖结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Settlement_payment(self,bys,values):
        """
        结算支付
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 员工结算 -- 二级菜单

    def Sub_Commission(self,bys,values):
        """
        分佣设置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Staff_management(self,bys,values):
        """
        员工管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Settlement_standard(self,bys,values):
        """
        结算标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Reference_standard(self,bys,values):
        """
        计提标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Performance_settlement(self,bys,values):
        """
        业绩结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Internal_incentive(self,bys,values):
        """
        内部激励
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Report_query(self,bys,values):
        """
        报表查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 数据中心 -- 二级菜单

    def Data_aggregation(self,bys,values):
        """
        数据汇总
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 人力中心 -- 二级菜单

    def Attendance_management(self,bys,values):
        """
        考勤管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

