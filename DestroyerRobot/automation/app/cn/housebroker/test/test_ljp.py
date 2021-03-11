#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/10 10:34
# @Author  : vivid
# @Email   : 331597811@163.com
# @File    : test_ljp.py
from DestroyerRobot.automation.app.cn.base.baseapp import BaseApp
from DestroyerRobot.automation.util.LoggerUtil import Log
import re
import time
class test_Estate():
    def __init__(self,driver):
        self.driver = BaseApp(driver)
        self.log = Log().logger()


    def is_Home_page(self):
        """
            判断当前是否在首页，不在首页就重启进入首页，重启失败返回False
            :return:
        """
        flag =True
        locator = '//*[@text="我的应用"]'
        Home_page=self.driver.getElementByElement("xpath",locator)
        if Home_page:
            pass
        else:
            flag = False
        return flag

    def is_Login(self):
        """
        获取当前登录状态,未登录返回 0，登录返回 1，异常返回2
        :return:
        """
        flag = 0
        try:
            login = self.driver.isElementExist("xpath",'//*[@text="请登录/注册"]')
            if login == False:
                flag =1
        except:
            try:
                login = self.driver.isElementExist('xpath', '//*[@text="请登录/注册"]')
                if login == False:
                    flag = 1
            except:
                # 如果没有检测到“我的应用”字样，说明还是没有打开首页，程序异常
                flag = 2
        return flag


    def test_dev_List(self):
        """
        楼盘列表
        :return:
        """
        flag = True
        home_page = self.is_Home_page()
        if home_page:
            login_status = self.is_Login()
            self.driver.swipes(20, 500, 20, 100, 1000)
            element=self.driver.getElementByElement("id","com.easylife.house.broker:id/tvDataNewHouse") #com.easylife.house.broker.test:id/tvDataNewHouse
            self.driver.clear(element)
            time.sleep(2)
            dev_list_res = self.driver.page_source()
            if login_status:
                try:
                    assert '方案' in dev_list_res and '报备' in dev_list_res
                    self.log.info('PASS,楼盘列表数据加载正常')
                    element=self.driver.getElementByElement("xpath",'//*[@text="添加到店铺"]')
                    self.driver.click(element)
                    time.sleep(1)
                    res = self.driver.page_source()
                    if "成功添加至我的店铺" in res:
                        self.log.info('添加店铺成功')
                    else:
                        flag = False
                        self.log.error('楼盘列表添加至我的店铺失败')

                    element =self.driver.getElementByElement('xpath','//*[@text="报备"]')
                    self.driver.click(element)
                    time.sleep(1)
                    res = self.driver.page_source()
                    if '注册用户不能报备' in res or '客户姓名' in res:
                        self.log.info('楼盘列表，点击报备，成功跳转至报备页')
                    else:
                        flag = False
                        self.log.info('楼盘列表，点击报备，没有跳转到报备页')
                except:
                    self.log.error('楼盘列表，未检测到“报备按钮”和“佣金方案”数据')
            else:
                # 未登录状态下，点击楼盘列表里的”添加到店铺”和“报备”
                element = self.driver.getElementByElement('xpath','//*[@text="添加到店铺"]')
                self.driver.click(element)
                res = self.driver.page_source()
                if "您暂未登录，不可添加至店铺" in res:
                    self.log.info('PASS，未登录状态，不可添加至店铺')
                else:
                    flag = False
                    self.log.error('Failed,未登录状态，添加至店铺没有检测到toast提示')
                element = self.driver.getElementByElement('xpath','//*[@text="报备"]')
                self.driver.click(element)
                locator = 'com.easylife.house.broker:id/btnLogin'
                try:
                    #WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.ID, locator)))
                    time.sleep(5)
                    self.log.info('PASS,未登录状态下，点击新房列表里的【报备】按钮,跳转到登录页')
                    self.driver.back()
                except:
                    flag = False
                    self.log.error('Failed,未登录状态下，点击新房列表里的【报备】按钮，未跳转到登录页')
        else:
            flag = False
            self.log.error('程序未成功启动首页，楼盘列表用例未能正常执行')

        assert flag == True, 'test_dev_List 楼盘列表用例执行失败'

    def test_dev_info(self):
        home_page = self.is_Home_page()  #super()
        print('home_page:',home_page)
        flag1 = True
        flag2 = True
        flag3 = True
        flag4 = True
        flag5 = True
        try:
            assert home_page == True, '当前页面不在APP首页，楼盘详情无法正常执行'
            self.driver.swipe(20, 500, 20, 100, 1000)
            element = self.driver.getElementByElement('id','com.easylife.house.broker:id/tvDataNewHouse')
            self.driver.click(element)

            time.sleep(2)
            # 搜索出霄云路8号

            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edSearchDevNam')
            self.driver.click(element)
            time.sleep(1)

            element = self.driver.getElementByElement('xpath', '//*[@text="请输入楼盘名称"]')
            self.driver.sendkeys(element,'霄云路8号')
            self.driver.press_keycode(66)
            time.sleep(2)
            dev_name = self.driver.isElementExist('xpath', '//*[@text="朝阳区 | 住宅 | 建面 450-520㎡"]')
            dev_img = self.driver.isElementExist('id', 'com.easylife.house.broker:id/imgHouse')
            try:
                assert dev_name and dev_img, '楼盘列表搜索霄云路8号，搜索结果里 未检测到楼盘图片或霄云路8号字段'
                # 进入楼盘详情，查看详情数据
                #self.driver.find_element_by_id('com.easylife.house.broker:id/tvHouseName').click()
                element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvHouseName')
                self.driver.click(element)
                # 等待元素加载完成
                # WebDriverWait(self.driver,20,0.5).until_not(lambda x: x.find_element_by_id('com.easylife.house.broker:id/progressBar').is_displayed())
                locator = '//*[@text="朝阳区霄云路8号"]'
                #WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
                time.sleep(5)
                # 获取楼盘详情页数据，检查是否正确
                dev_info_page1 = (('合生霄云路8号', '120000.0元/㎡', '朝阳区霄云路8号'), ('楼盘数据', '订单数'))
                dev_info_page2 = (('带客规则', '报备规则', '带看规则', '报备间隔：30分钟'), ('主力户型(2)', '5居(1)'))
                dev_info_page3 = (('楼盘动态(4)', '合生·霄云路8号450-520㎡产品在售', '合生·霄云路8号项目大户型房源在售'),
                                  ('楼盘信息', '合生', '2009-10-01', '2011-10-08', '京房售证字（2011）182号'))

                # 先检查第一屏幕里的信息是否正确
                for info in dev_info_page1:

                    for i in info:
                        ele = self.driver.isElementExist('xpath', '//*[@text="' + i + '"]')
                        try:
                            assert ele
                        except:
                            flag1 = False
                            self.log.error('Failed，楼盘详情：' + info[0] + '里未检测到元素：' + i)

                if flag1 == True:
                    self.log.info('PASS，楼盘详情页地址价格及确客制度等数据检测正常')

                # 然后滑动到第二屏幕，检查信息
                self.driver.swipe_Up()
                for info in dev_info_page2:

                    for i in info:
                        ele = self.driver.isElementExist('xpath', '//*[@text="' + i + '"]')
                        try:
                            assert ele
                        except:
                            flag2 = False
                            self.log.error('Failed，楼盘详情：' + info[0] + '里未检测到元素：' + i)

                if flag2 == True:
                    self.log.info('PASS，楼盘详情页主力户型、楼盘动态数据检测正常')

                # 然后滑动到第三屏幕，检查信息
                self.driver.swipe_Up()
                for info in dev_info_page3:
                    for i in info:
                        ele =self.driver.isElementExist('xpath', '//*[@text="' + i + '"]')
                        try:
                            assert ele
                        except:
                            flag3 = False
                            self.log.error('Failed，楼盘详情：' + info[0] + '里未检测到元素：' + i)

                if flag3 == True:
                    self.log.info('PASS，楼盘详情页楼盘信息数据检测正常')

                # 进入楼盘信息详情页，检查是否数据正确
                #self.driver.find_element_by_id('com.easylife.house.broker:id/tvMoreHouseInfo').click()
                element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvMoreHouseInf')
                self.driver.click(element)
                time.sleep(2)
                dev_more_info = ['京房售证字（2011）182号', '康景物业', '精装修']
                for info in dev_more_info:
                    ele = self.driver.isElementExist('xpath', '//*[@text="' + info + '"]')
                    try:
                        assert ele
                    except:
                        flag4 = False
                        self.log.error('Failed，楼盘详情【更多信息】里未检测到元素：' + info)

                if flag4 == True:
                    self.log.info('PASS，楼盘详情页【更多信息页】数据检测正常')
                self.driver.back()

                # 楼盘动态页加载检查
                #self.driver.find_element_by_id('com.easylife.house.broker:id/tvMoreDynamic').click()
                element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvMoreDynamic')
                self.driver.click(element)
                time.sleep(2)
                text = self.driver.page_source()
                try:
                    assert '地处燕莎商圈' in text and '合生·霄云路8号450-520㎡产品在售' in text
                except:
                    flag5 = False
                    self.log.error('Failed,楼盘动态详情页，加载数据异常')
                self.driver.back()
            except:
                assert 1 == 2
                self.log.error('未检测到楼盘图片或霄云路8号字段')

        except:
            self.log.error('楼盘详情用例未执行')

        assert flag1 == True and flag2 == True and flag3 == True and flag4 == True and flag5 == True

    def dev_commision_login(self):
        """
        登录情况下，【缦合·北京】楼盘详情页佣金方案显示，及佣金查看详情
        :return:
        """
        #self.driver.find_element_by_id('com.easylife.house.broker:id/tvDataNewHouse').click()
        element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvDataNewHouse')
        self.driver.click(element)
        time.sleep(2)
        # self.driver.start_activity('com.easylife.house.broker', 'com.easylife.house.broker.ui.house.HouseListActivity')
        locator = 'com.easylife.house.broker:id/edSearchDevName'
        flag = True
        try:
            #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, locator)))
            time.sleep(5)
            #self.driver.find_element_by_id('com.easylife.house.broker:id/edSearchDevName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edSearchDevName')
            self.driver.click(element)
            time.sleep(1)
            #self.driver.find_element_by_id('com.easylife.house.broker:id/edSearchDevName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edSearchDevName')
            self.driver.click(element)
            time.sleep(1)
            #self.driver.find_element_by_xpath('//*[@text="请输入楼盘名称"]').send_keys('缦合·北京')
            element = self.driver.getElementByElement('xpath','//*[@text="请输入楼盘名称"]')
            self.driver.sendkeys(element,'缦合·北京')
            self.driver.press_keycode(66)
            time.sleep(2)
            #self.driver.find_element_by_id('com.easylife.house.broker:id/tvHouseName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvHouseName')
            self.driver.click(element)
            locator = '//*[@text="朝阳区霄云路8号"]'
            #WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            time.sleep(5)
            # 先检查是否有佣金激励模块
            page_res = self.driver.page_source()
            # exist_commision = BaseApp(self.driver).isElementExist('xpath', '//*[@text="佣金激励"]')
            if '佣金激励' in page_res:
                # 获取页面数据，检查是否有佣金数据
                commision_res = self.driver.page_source()
                assert '有效期' in commision_res and '套餐' in commision_res, '登录状态下，慢合北京楼盘详情，佣金激励模块未检测到佣金方案详细数据'
                # 查看佣金详情数据
                commision_info_btn = self.driver.isElementExist('id', 'com.easylife.house.broker:id/tvDetail')
                if commision_info_btn:
                    #self.driver.find_element_by_id('com.easylife.house.broker:id/tvMoreCommission').click()
                    element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvMoreCommission')
                    self.driver.click(element)
                    time.sleep(3)
                    comm_cont = self.driver.page_source()
                    try:
                        assert '展开详情' in comm_cont and '有效期' in comm_cont, '佣金激励列表，未检测出数据'
                        self.log.info('PASS，楼盘详情页，佣金激励方案，更多列表加载正确')
                    except:
                        flag = False
                else:
                    flag = False
                    self.log.error('慢合北京，楼盘详情页，佣金激励模块登录后，没有查看详情按钮')
            else:
                self.log.info('缦合·北京,楼盘详情页，未检测出佣金激励模块，请查看是否存在佣金数据')


        except:
            flag = False
            self.log.error('缦合·北京楼盘详情页，佣金方案异常')
        assert flag == True


    def dev_commission_not_login(self):
        """
        未登录状态下，楼盘详情页，佣金方案展示，及登录跳转
        :return:
        """
        #self.driver.find_element_by_id('com.easylife.house.broker:id/tvDataNewHouse').click()
        element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvDataNewHouse')
        self.driver.click(element)
        time.sleep(2)
        # self.driver.start_activity('com.easylife.house.broker', 'com.easylife.house.broker.ui.house.HouseListActivity')
        locator = 'com.easylife.house.broker:id/edSearchDevName'
        flag = True
        try:
            #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, locator)))
            time.sleep(3)
            #self.driver.find_element_by_id('com.easylife.house.broker:id/edSearchDevName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edSearchDevName')
            self.driver.click(element)
            time.sleep(1)
            #self.driver.find_element_by_xpath('//*[@text="请输入楼盘名称"]').send_keys('缦合·北京')
            element = self.driver.getElementByElement('xpath', '//*[@text="请输入楼盘名称"]')
            self.driver.sendkeys(element,'缦合·北京')
            self.driver.press_keycode(66)
            time.sleep(3)
            #self.driver.find_element_by_id('com.easylife.house.broker:id/tvHouseName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvHouseName')
            self.driver.click(element)
            locator = '//*[@text="朝阳区霄云路8号"]'
            #WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            time.sleep(3)

            # 先检查是否有佣金激励模块
            exist_commision = self.driver.isElementExist('xpath', '//*[@text="结佣规则"]')
            if exist_commision:
                login_tips = self.driver.isElementExist('xpath', '//*[@text="登录查看佣金激励，点击“立即登录”"]')
                assert login_tips, '未登录状态下，楼盘详情页，佣金激励模块，未检测到登录提示'
                self.log.info('PASS,未登录状态下，楼盘详情页，佣金激励模块显示去登录按钮')
                if login_tips:
                    # 去登录，然后检查登录后是否可以展示
                    #self.driver.find_element_by_xpath('//*[@text="登录查看佣金激励，点击“立即登录”"]').click()
                    element = self.driver.getElementByElement('xpath', '//*[@text="登录查看佣金激励，点击“立即登录”"]')
                    self.driver.click(element)
                    time.sleep(3)
                    try:
                        # 检查是否跳转到登录页面
                        login_btn = self.driver.isElementExist('id', 'com.easylife.house.broker:id/btnLogin')
                        time.sleep(4)
                        if login_btn:
                            # 输入用户名密码登录
                            #self.driver.find_element_by_xpath('//*[@text="密码登录"]').click()
                            element = self.driver.getElementByElement('xpath', '//*[@text="密码登录"]')
                            self.driver.click(element)
                            time.sleep(1)
                            #self.driver.find_element_by_id('com.easylife.house.broker:id/edphone').send_keys('18810223040')
                            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edphone')
                            self.driver.sendkeys(element,'18810223040')
                            #self.driver.find_element_by_id('com.easylife.house.broker:id/edPassword').send_keys('123456')
                            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edPassword')
                            self.driver.sendkeys(element, '18810223040')
                            # self.driver.find_element_by_id('com.easylife.house.broker:id/cbAgree').click() # 勾选用户服务协议，默认是勾选的，不用点击勾选了
                            #self.driver.find_element_by_id('com.easylife.house.broker:id/btnLogin').click()
                            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/btnLogin')
                            self.driver.click(element)
                            time.sleep(1)
                            # self.driver.refresh()
                            # 由于返回的时候没有刷新页面，所以需要重新进入楼盘详情页
                            self.log.info('楼盘详情页登录成功')
                            self.driver.back()
                            #self.driver.find_element_by_id('com.easylife.house.broker:id/tvHouseName').click()
                            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvHouseName')
                            self.driver.click(element)
                            # WebDriverWait(self.driver, 20, 0.5).until(
                            #     EC.visibility_of_element_located((By.XPATH, locator)))
                            time.sleep(5)
                            # 获取页面数据，检查是否有佣金数据
                            commision_res = self.driver.page_source()
                            assert '有效期' in commision_res and '套餐' in commision_res, '登录后，慢合北京楼盘详情，佣金激励模块未检测到佣金方案详细数据'
                            # 查看佣金详情数据
                            commision_info_btn = self.driver.isElementExist('id','com.easylife.house.broker:id/tvDetail')
                            if commision_info_btn:
                                #self.driver.find_element_by_id('com.easylife.house.broker:id/tvMoreCommission').click()
                                element = self.driver.getElementByElement('id',
                                                                          'com.easylife.house.broker:id/tvMoreCommission')
                                self.driver.click(element)
                                time.sleep(3)
                                comm_cont = self.driver.page_source()
                                try:
                                    assert '展开详情' in comm_cont and '有效期' in comm_cont, '佣金激励列表，未检测出数据'
                                except:
                                    flag = False
                            else:
                                flag = False
                                self.log.error('慢合北京，楼盘详情页，佣金激励模块登录后，没有查看详情按钮')
                        else:
                            flag = False
                            self.log.error('慢合北京，楼盘详情页，未登录状态下，佣金激励模块未检测到登录提示')

                    except:
                        flag = False
                        self.log.error('慢合北京，楼盘详情页，通过佣金激励模块登录功能异常')

            else:
                self.log.info('缦合·北京楼盘详情页，未检测到佣金激励模块，请检查是否有佣金政策')

        except:
            flag = False
            self.log.error('缦合·北京楼盘详情页，佣金方案异常')

        assert flag == True


    def test_dev_house_info(self):
        """
        霄云路8号，户型详情
        :return:
        """
        home_page = self.is_Home_Page()
        try:
            assert home_page, '未能成功进入首页，户型详情执行失败'
            # self.driver.swipe(20, 500, 20, 100, 1000)
            # 点击新房列表
            #self.driver.find_element_by_id('com.easylife.house.broker:id/tvDataNewHouse').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvDataNewHouse')
            self.driver.click(element)
            time.sleep(3)
            # 搜索出霄云路8号，回车
            #self.driver.find_element_by_id('com.easylife.house.broker:id/edSearchDevName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edSearchDevName')
            self.driver.click(element)
            time.sleep(1)
            #self.driver.find_element_by_id('com.easylife.house.broker:id/edSearchDevName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edSearchDevName')
            self.driver.click(element)
            time.sleep(1)
            #self.driver.find_element_by_xpath('//*[@text="请输入楼盘名称"]').send_keys('霄云路8号')
            element = self.driver.getElementByElement('xpath', '//*[@text="请输入楼盘名称"]')
            self.driver.sendkeys(element,'霄云路8号')
            self.driver.press_keycode(66)
            time.sleep(2)
            # 进入楼盘详情，查看详情数据
            #self.driver.find_element_by_id('com.easylife.house.broker:id/tvHouseName').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/tvHouseName')
            self.driver.click(element)
            # 等待元素加载完成
            locator = '//*[@text="朝阳区霄云路8号"]'
            #WebDriverWait(self.driver, 20, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            time.sleep(5)
            self.driver.swipe_Up()
            time.sleep(1)
            #self.driver.find_element_by_xpath('//*[@text="5室3厅5卫2厨"]').click()
            element = self.driver.getElementByElement('xpath', '//*[@text="5室3厅5卫2厨"]')
            self.driver.click(element)
            time.sleep(5)
            house_page_info = self.driver.page_source()
            self.driver.swipe_Up()
            house_page_info = self.driver.page_source() + house_page_info
            page_info = ['住宅', '520㎡', '户型简介', '会客厅开间8.6米 2、进门双玄关处都更为宽大', '所属楼盘', '合生霄云路8号',
                         '朝阳区 | 住宅 | 建面450.0-520.0㎡', '本楼盘其他户型', '4室3厅5卫1厨']
            flag = True
            for i in page_info:
                try:
                    assert i in house_page_info
                except:
                    flag = False
                    self.log.error('Failed，楼盘动态详情页，未检测到数据：' + i)

            assert flag == True, 'Failed,户型详情页数据加载异常'
            self.log.info('PASS，楼盘-户型详情，数据加载正确')

        except:
            assert 1 == 2
            self.log.error('户型详情用例执行失败')


    def test_dev_commission(self):
        login_state = self.is_Login()
        if login_state == 0:
            self.dev_commission_not_login()
        elif login_state == 1:
            self.dev_commision_login()
        else:
            # 如果登录状态为2，说明程序异常
            self.log.error('程序异常，未能测试楼盘详情佣金数据')
        assert login_state != 2, ('程序异常，未能测试楼盘详情佣金数据')


    def test_broker_store(self):
        '''
        经纪人我的店铺-移除楼盘
        :return:
        '''
        home_page = self.is_Home_Page()
        assert home_page == True, 'Faied，未能成功启动首页'
        time.sleep(3)
        #self.driver.find_element_by_xpath('//*[@text="我的店铺"]').click()
        element = self.driver.getElementByElement('xpath', '//*[@text="我的店铺"]')
        self.driver.click(element)
        time.sleep(1)
        # 判断是否跳转到登录页，跳转的话就进行登录，否则直接进行后续流程
        is_login = self.driver.isElementExist('xpath', '//*[@text="验证码登录"]')
        if is_login:
            # 输入用户名密码登录
            #self.driver.find_element_by_xpath('//*[@text="密码登录"]').click()
            element = self.driver.getElementByElement('xpath', '//*[@text="密码登录"]')
            self.driver.click(element)
            time.sleep(1)
            # self.driver.find_element_by_id('com.easylife.house.broker:id/edphone').send_keys(
            #     '18810223040')
            element=self.driver.getElementByElement('id','com.easylife.house.broker:id/edphone')
            self.driver.sendkeys(element,"18810223040")
            # self.driver.find_element_by_id('com.easylife.house.broker:id/edPassword').send_keys(
            #     '123456')
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/edPassword')
            self.driver.sendkeys(element, "123456")
            # self.driver.find_element_by_id('com.easylife.house.broker:id/cbAgree').click() # 勾选用户服务协议，默认是勾选的，不用点击勾选了
            #self.driver.find_element_by_id('com.easylife.house.broker:id/btnLogin').click()
            element = self.driver.getElementByElement('id', 'com.easylife.house.broker:id/btnLogin')
            self.driver.click(element)
            time.sleep(1)
            #self.driver.find_element_by_xpath('//*[@text="我的店铺"]').click()
            element = self.driver.getElementByElement('xpath', '//*[@text="我的店铺"]')
            self.driver.click(element)
            time.sleep(2)

        # 移除所有店铺
        #res_text = self.driver.find_element_by_id('com.easylife.house.broker:id/tvMyDev').get_attribute('text')
        element =self.driver.getElementByElement('id','com.easylife.house.broker:id/tvMyDev')
        res_text = self.driver.getattribut(element,'text')

        num = re.sub(r'\D', '', res_text)
        if num == '':
            self.log.info('PASS，我的店铺里没有收藏的店铺')
        else:
            for i in range(0, int(num)):
                #self.driver.find_element_by_xpath('//*[@text="移除店铺"]').click()
                element = self.driver.getElementByElement('xpath', '//*[@text="移除店铺"]')
                self.driver.click(element)
                time.sleep(2)
                #self.driver.find_element_by_xpath('//*[@text="确定"]').click()
                element = self.driver.getElementByElement('xpath', '//*[@text="确定"]')
                self.driver.click(element)
                time.sleep(2)
            self.log.info('PASS，成功移除店铺内所有楼盘')