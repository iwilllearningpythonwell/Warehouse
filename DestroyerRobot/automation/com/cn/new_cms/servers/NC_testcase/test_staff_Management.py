from DestroyerRobot.automation.util.XmlUtil import XmlUtil
from DestroyerRobot.automation.util.ConfigUtil import Config
from DestroyerRobot.automation.util.DateTimeUtil import TestDateTime
from DestroyerRobot.automation.com.cn.base.BasePage import BasePage
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_Tree.test_nc_tree import test_nctree_master
from DestroyerRobot.automation.com.cn.new_cms.servers.NC_TreeKids.test_nctree_kids import test_nctree_kids
from DestroyerRobot.automation.com.cn.new_cms.servers.NCLoing.NCLogin import NCLoing
from DestroyerRobot.automation.util.RandomUtil import TestRamdom
from DestroyerRobot.automation.util.MySqlDBUtil import MysqlDB
import traceback
import time

class test_NC_StaffManagement:

    business_line = ''
    department_name = ''
    station_name = ''

    def __init__(self,driver):
        """
        实现数据后，定位页面信息操作
        登录页面，操作数据
        """
        self.driver = driver
    # test_mptree(self.driver).rootChildConfigPath()
    def rootChildConfigPath(self):
        # 从主配置文件中获取子配置文件路径
        conf2 = Config("ConfigKIDs")
        # 获取子文件路径
        confFile = conf2.get_configPath("new_cms_configs")
        return confFile

    def childConfigXML(self, Pageskeyword, UIElementkeyword):
        confFile = self.rootChildConfigPath()
        config2 = Config("XMLFilePath", confFile)
        filepath = config2.get_path_config("staff_management")
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

    # 新增部门
    def add_Department(self):
        add_btn_bys,add_btn_values = self.childConfigXML('部门管理','新建部门')
        input_box_bys,input_box_values = self.childConfigXML('部门管理','输入部门名称')
        save_btn_bys,save_btn_values = self.childConfigXML('部门管理','保存')
        popup_bys,popup_values = self.childConfigXML('部门管理','新建部门弹窗')
        nc = NCLoing(self.driver)
        try:
            test_nctree_master(self.driver).get_link_Employee_settlement()  # 点击员工结算
            test_nctree_master(self.driver).get_link_Staff_management()     # 点击员工管理
            test_nctree_kids(self.driver).get_link_Departmental_management()    # 点击部门管理
            nc.input_click(add_btn_bys,add_btn_values)  # 点击新建部门
            radom_num = TestRamdom().RandomTestInt(999,0)
            global department_name
            department_name = 'autotest_部门'+ str(radom_num)
#            self.department_name = 'autotest_部门'+ str(radom_num)
            nc.Input_o(department_name,input_box_bys,input_box_values)    # 输入部门名称
            nc.input_click(save_btn_bys,save_btn_values)

            for i in range(0,10):                     # 判断标题名称是否重复
                cont = self.driver.page_source
                if u'部门名称已存在'in cont:
                    nc.Clear_o(input_box_bys,input_box_values)
                    radom_num = TestRamdom().RandomTestInt(999, 0)
                    department_name = 'autotest_部门' + str(radom_num)
                    nc.Input_o(department_name, input_box_bys, input_box_values)  # 再次输入部门名称
                elif i == 9:
                    print('部门太多啦，新建不了啦')
                    break
                else:
                    break

            #
            # # 连接测试数据库，获取最新创建的部门名称
            # my = MysqlDB()
            # my.getCursor(sqltable="easylife_commallot")
            # sql = "SELECT department_name FROM commallot_staff_department "
            # department = my.queryOperation(sql)
            # print(department)
            # return department

        except Exception:
            img_path = self.childConfigImgPath()
            BasePage(self.driver).save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    # 新增业务线
    def add_Business_line(self):
        add_btn_bys, add_btn_values = self.childConfigXML('业务线管理', '新建业务线')
        input_box_bys, input_box_values = self.childConfigXML('业务线管理', '请输入业务线名称')
        save_btn_bys, save_btn_values = self.childConfigXML('业务线管理', '保存')
        popup_bys, popup_values = self.childConfigXML('业务线管理', '新建业务线弹窗')
        nc = NCLoing(self.driver)
        try:
            test_nctree_kids(self.driver).get_link_Business_Line_Management()    # 点击业务线管理
            nc.input_click(add_btn_bys,add_btn_values)  # 点击新建业务线
            radom_num = TestRamdom().RandomTestInt(999,0)

            global business_line
            business_line = 'autotest_业务线'+ str(radom_num)
            nc.Input_o(business_line,input_box_bys,input_box_values)    # 输入业务线名称
            nc.input_click(save_btn_bys,save_btn_values)

            for i in range(0,10):                     # 判断标题名称是否重复
                cont = self.driver.page_source
                if u'业务线名称已存在'in cont:
                    nc.Clear_o(input_box_bys,input_box_values)
                    radom_num = TestRamdom().RandomTestInt(999, 0)
                    business_line = 'autotest_业务线' + str(radom_num)
                    nc.Input_o(business_line, input_box_bys, input_box_values)  # 再次输入部门名称
                elif i == 9:
                    print('业务线太多啦，新建不了啦')
                    break
                else:
                    break


        except Exception:
            img_path = self.childConfigImgPath()
            BasePage(self.driver).save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())

    # 新增岗位
    def add_staff_station(self):
        add_btn_bys, add_btn_val = self.childConfigXML('岗位管理', '新建岗位')
        input_box_bys, input_box_val = self.childConfigXML('岗位管理', '输入岗位名称')

        bussiness_line_bys,bussiness_line_val = self.childConfigXML('岗位管理', '筛选业务线')
        click_line_bys,click_line_val = self.childConfigXML('岗位管理', '选中业务线')

        department_bys,department_val = self.childConfigXML('岗位管理', '选择所属部门')
        click_department_bys, click_department_val = self.childConfigXML('岗位管理', '点击所属部门')
        weight_off_line_bys,weight_off_line_val = self.childConfigXML('岗位管理', '岗位权重范围_off')
        weight_on_line_bys,weight_on_line_val = self.childConfigXML('岗位管理', '岗位权重范围_on')
        standard_weight_bys,standard_weight_val = self.childConfigXML('岗位管理', '岗位标准权重')
        compilation_quantity_bys,compilation_quantity_val = self.childConfigXML('岗位管理', '编制数量')
        role_bys,role_val = self.childConfigXML('岗位管理', '选择角色')
        role_click_bys,role_click_val = self.childConfigXML('岗位管理', '点击角色')
        save_btn_bys, save_btn_values = self.childConfigXML('岗位管理', '保存')

        nc = NCLoing(self.driver)
        try:
            test_nctree_kids(self.driver).get_link_Post_management()    # 点击岗位管理
            nc.input_click(add_btn_bys,add_btn_val)  # 点击新建岗位
            radom_num = TestRamdom().RandomTestInt(999,0)
            global station_name
            station_name = 'autotest_岗位'+ str(radom_num)
            nc.Input_z(station_name,input_box_bys,input_box_val)    # 输入岗位名称
            nc.Input_o(business_line,bussiness_line_bys,bussiness_line_val)    # 输入业务线
            click_line_val = click_line_val %(business_line)    # 获取add_Business_line方法里面的业务线名称，并取对应的xpath值
            nc.input_click(click_line_bys, click_line_val)      # 点击业务线
            nc.Input_t(department_name,department_bys,department_val)    # 输入部门
            click_department_val = click_department_val %(business_line)    # 获取部门名称对应的xpath值
            nc.input_click(click_department_bys, click_department_val)  # 点击所属部门
            nc.Input_z('1',weight_off_line_bys,weight_off_line_val)     # 输入权重范围-最小值
            nc.Input_o('10', weight_on_line_bys, weight_on_line_val)    # 输入权重范围-最大值
            nc.Input_t('5',standard_weight_bys,standard_weight_val)     # 输入标准权重
            nc.Input_z('10',compilation_quantity_bys,compilation_quantity_val)     # 输入编制数量
            nc.Input_th('业务人员',role_bys,role_val)    # 角色选择“业务人员”
            nc.input_click(role_click_bys,role_click_val)   # 点击业务人员
            nc.input_click(save_btn_bys,save_btn_values)


        except Exception:
            img_path = self.childConfigImgPath()
            BasePage(self.driver).save_img(img_path, str(int(TestDateTime().time_stamp())))
            print(traceback.format_exc())




    def add_Staff(self):
        pass
        

