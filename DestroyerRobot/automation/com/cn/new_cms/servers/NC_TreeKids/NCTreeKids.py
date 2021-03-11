from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
class MPTreeKids:
    def __init__(self,driver):
        """
        获取驱动
        """
        self.base = BasePage(driver)


    # 配置中心 -> 基础数据


    def Area_management(self,bys,values):
        """
        片区管理
        :param bys:
        :param values:
        :return:
        """

        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Bank_Data_management(self,bys,values):
        """
        银行数据配置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    # 配置中心 -> 成交节点

    def Node_rule_settings(self,bys,values):
        """
        节点规则管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Settlement_Rules(self,bys,values):
        """
        结佣规则管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 配置中心 -> 接口配置


    def Customer_State_Mapping(self,bys,values):
        """
        客户状态映射
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Project_mapping(self,bys,values):
        """
        外部项目映射
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Interface_mapping(self,bys,values):
        """
        外部接口映射
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Kingdee_push_Management(self,bys,values):
        """
        金蝶推送管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Auxiliary_Account_Mapping(self,bys,values):
        """
        辅助账项目映射
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def dev_Organizational_Relations(self,bys,values):
        """
        楼盘映射组织关系
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Auxiliary_Accounts_Mapping(self,bys,values):
        """
        辅助账供应商映射
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Auxiliary_Account_Customer(self,bys,values):
        """
        辅助账客户映射
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    # 配置中心 -- 驳回设置

    def Reject_Category_Management(self,bys,values):
        """
        驳回类目管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    def Rejection_Cause_Management(self,bys,values):
        """
        驳回原因管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    # 标准管控 -- 标准管理


    def Project_Cooperation_Criteria(self,bys,values):
        """
        项目合作标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Award_criteria(self,bys,values):
        """
        团奖标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Commission_settlement_standard(self,bys,values):
        """
        佣金结算标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Cost_Control_Standard(self,bys,values):
        """
        费用管控标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def investment_Control_standard(self,bys,values):
        """
        跟投管控标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 标准管控 -- 费用结算


    def Expense_settlement_management (self,bys,values):
        """
        费用结算管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 合约中心 -- 签约方管理

    def legal_person_management (self,bys,values):
        """
        内部法人管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Channel_brokerage_management(self,bys,values):
        """
        渠道/经纪管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Developer_management (self,bys,values):
        """
        开发商管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 合约中心 -- 合同管理

    def Contract_signing_management(self,bys,values):
        """
        合同签订管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Termination_contract(self,bys,values):
        """
        合同终止
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Contract_enquiry(self,bys,values):
        """
        合同查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Contract_type_management(self,bys,values):
        """
        合同类型管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Model_management(self,bys,values):
        """
        范本管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 合约中心 -- 跟投规则

    def investment_Allocation_rule(self,bys,values):
        """
        跟投分配规则
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Dividend_settlement_rule(self,bys,values):
        """
        分红结算规则
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 合约中心 -- 跟投管理

    def investment_project_management(self,bys,values):
        """
        跟投项目管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def investment_Payment_management(self,bys,values):
        """
        跟投支付管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Transfer_remittance_examine(self,bys,values):
        """
        转账汇款审核
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Project_progress_view(self,bys,values):
        """
        项目进展查看
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Project_liquidation(self,bys,values):
        """
        项目清算管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def investment_Income_record(self,bys,values):
        """
        跟投收益记录
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 内容中心 -- 内容配置

    def Homepage_Bullet_Window(self,bys,values):
        """
        首页弹窗管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Poster_Configuration(self,bys,values):
        """
        海报配置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Live_Course_Management(self,bys,values):
        """
        直播课程管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Announcement_config(self,bys,values):
        """
        管家端公告配置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Flash_screen_advertising(self,bys,values):
        """
        闪屏广告
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 内容中心 -- 资讯反馈

    def Topic_Page_Management(self,bys,values):
        """
        专题页配置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 交易中心 -- 客户管理


    def Customer_List(self,bys,values):
        """
        客户列表
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 交易中心 -- 用户管理

    def User_List(self,bys,values):
        """
        用户列表
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 财务结算 -- 支付板块


    def Transfer_accounts_examine(self,bys,values):
        """
        转账审核
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 财务结算 -- 业绩管理


    def Transaction_commission(self,bys,values):
        """
        交易及佣金
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Payment_confirmation(self,bys,values):
        """
        回款确认
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 财务结算 -- 佣金审核


    def Broker_rewards(self,bys,values):
        """
        经纪人奖励
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Broker_Commission(self,bys,values):
        """
        经纪人结佣
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Broker_company_Commission(self,bys,values):
        """
        经纪公司结佣
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def network_pusher_Commission(self,bys,values):
        """
        网络推客结佣
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 财务结算 -- 奖励管理


    def shop_card_Commission(self,bys,values):
        """
        购物卡结佣
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def shop_card_category(self,bys,values):
        """
        购物卡类别
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def shop_card_Stock(self,bys,values):
        """
        购物卡库存
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def shop_card_query(self,bys,values):
        """
        购物卡查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def shop_card_send(self,bys,values):
        """
        购物卡发货
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)



    # 财务结算 -- 返还支出


    def Refund_inquiry(self,bys,values):
        """
        返还款查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Refund_payment(self,bys,values):
        """
        返还款支付
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 财务结算 -- 团奖结算

    def Group_award_statement(self,bys,values):
        """
        团奖结算表
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Group_award_application(self,bys,values):
        """
        团奖申请
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Group_award_Finance(self,bys,values):
        """
        团奖申请-财务
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 财务结算 -- 结算支付


    def List_pending_payments(self,bys,values):
        """
        待支付清单
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Payment_List_Query(self,bys,values):
        """
        支付清单查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Settlement_Inquiry(self,bys,values):
        """
        结算查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Payment_settings(self,bys,values):
        """
        支付设置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 分佣设置

    def Cooperative_Label_Management(self,bys,values):
        """
        合作标签管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Project_Commission_management(self,bys,values):
        """
        项目分佣管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Project_Level_Management(self,bys,values):
        """
        项目等级管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Project_Commission_Detail(self,bys,values):
        """
        项目分佣比例明细
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 员工管理


    def Departmental_management(self,bys,values):
        """
        部门管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Business_Line_Management(self,bys,values):
        """
        业务线管理
        :param bys:
        :param values:
        :return:
        """

        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Post_management(self,bys,values):
        """
        岗位管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Employee_management(self,bys,values):
        """
        员工管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 结算标准

    def Section_standard_setting(self,bys,values):
        """
        区间标准设置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Transaction_settlement_standard(self,bys,values):
        """
        成交结算标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Revenue_settlement_standard(self,bys,values):
        """
        营收结算标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Profit_settlement_standard(self,bys,values):
        """
        利润结算标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Profit_standard_setting(self,bys,values):
        """
        利润标准设置
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Market_settlement_standard(self,bys,values):
        """
        市场结算标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 计提标准

    def commission_standard(self,bys,values):
        """
        交易佣金标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Performance_incentive(self,bys,values):
        """
        业绩激励标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Profit_incentive(self,bys,values):
        """
        利润激励标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Market_Commission_Standard(self,bys,values):
        """
        市场佣金标准
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 业绩结算


    def Transaction_Settlement(self,bys,values):
        """
        成交结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Revenue_Settlement_Month(self,bys,values):
        """
        营收结算-月
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Revenue_Settlement_Year(self,bys,values):
        """
        营收结算-年
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Profit_Settlement(self,bys,values):
        """
        利润结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Market_Settlement(self,bys,values):
        """
        市场结算
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 内部激励


    def employee_Commission_Summary(self,bys,values):
        """
        员工佣金发放总表
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Market_Commission(self,bys,values):
        """
        市场佣金
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Trading_Commission(self,bys,values):
        """
        交易佣金
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Employee_motivation_Month(self,bys,values):
        """
        员工激励-月
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Employee_motivation_Year(self,bys,values):
        """
        员工激励-年
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Profit_incentive_Year(self,bys,values):
        """
        利润激励-年
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 员工结算 -- 报表查询

    def Employee_Commission_Report_Query(self,bys,values):
        """
        员工分佣报表查询
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    # 数据中心 -- 数据汇总


    def Channel_Commission(self,bys,values):
        """
        渠道佣金
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def easylife_Summary_commission(self,bys,values):
        """
        好生活结佣汇总
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def easylife_Pool_funds(self,bys,values):
        """
        好生活资金池
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Kpi_Index_management(self,bys,values):
        """
        kpi指标管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def easylife_kpi_check(self,bys,values):
        """
        好生活kpi考核
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    def Rejection_pool(self,bys,values):
        """
        驳回统计池
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)


    # 人力中心 -- 考勤管理

    def Personal_attendance_record(self,bys,values):
        """
        个人考勤记录
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Monthly_Attendance_Statistics(self,bys,values):
        """
        考勤月度统计
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)

    def Attendance_management(self,bys,values):
        """
        考勤人员管理
        :param bys:
        :param values:
        :return:
        """
        ele = self.base.getElementByElement(bys,values)
        self.base.click(ele)





