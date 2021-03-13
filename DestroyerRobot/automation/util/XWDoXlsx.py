#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/10/13
# @Author  : hopsonxw
# @FileName: xw_doXlsx.py
# @Software: PyCharm
# @email    ：190135@lifeat.cn
import os
import pandas as pd
import xlrd  # 导入读Excel的xlrd库
import xlutils.copy  # 导入xlutils库的copy模块
import json
import openpyxl

def get_Path():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    return current_path

class doExcel():

    def read_xls(self, path, xls_name, sheet_name, cell_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        # path = os.path.dirname(get_Path())  # 拿到该项目所在的绝对路径
        xlsPath = os.path.join(path, xls_name)  # 获取用例文件路径
        file = xlrd.open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
        # 获取这个sheet内容行数
        nrows = sheet.nrows
        cls = []
        data = []
        for i in range(nrows):  # 根据行数做循环
            cls.append(sheet.row_values(i)) #将excel读取出来的所有数据以list形式存入另一个list

        frist_p = cls[0]      #x字典的key
        last_p = cls[1:]      #x字典的value
        for j in range(len(last_p)):
            if last_p[j][0] == cell_name:  # 如果这个Excel的这个sheet的第i行的第一列等于[参数化cell_name]那么我们把这行的数据添加到cls[]
                x = dict(zip(frist_p, last_p[j])) #转成字典x
                data.append(x)
        return data

    # 获取单元格所在行
    def findLocation(self, path, xls_name, sheet_name, cell_name):

        xlsPath = os.path.join(path, xls_name)  # 获取用例文件路径
        demo_df = pd.read_excel(xlsPath, sheet_name)  # 读取sheet中所有单元格内容，返回的是一个类似数组的数据组，index和values两部分
        # li = demo_df.values   # 返回的是一个list

        for indexs in demo_df.index:
            values = demo_df.loc[indexs].values
            for i in range(len(values)):
                if (values[i] == cell_name):
                    row = indexs + 1
                    # print('行数：', row)
                    return row


    # 处理需要写入excel的数据格式为字符串
    def handleData(self, data):
        for j in range(len(data)):
            if type(data[j]) == tuple:
                data[j] = ','.join(data[j])
            elif type(data[j]) == list:
                data[j] = ','.join(data[j])
            elif type(data[j]) == dict:
                data[j] = json.dumps(data[j], ensure_ascii=False)
            else:
                pass

    # 通过xlrd,xlutils写入单元格，处理xls
    def writeCell(self, path, xls_name, sheet_name, cell_name, responds):

        my_excel = os.path.join(path, xls_name)  # 获取用例文件路径
        row = doExcel.findLocation(self, path, xls_name, sheet_name, cell_name)  # 取单元格所在行
        # print(row)
        file = xlrd.open_workbook(my_excel, formatting_info=True)  # 读取excel，formatting_info=True为保留文件原有格式，若无则保存的文件格式初始化
        cpbook = xlutils.copy.copy(file)  # 复制文件
        w_sheet = cpbook.get_sheet(file.sheet_names().index(sheet_name))  # 索引sheet表
        # 数据类型转换
        # print(type(responds))
        if type(responds) == dict:
            data = json.dumps(responds, ensure_ascii=False)
        elif type(responds) == list:
            self.handleData(responds)
            data = ','.join(responds)
        elif type(responds) == tuple:
            datali = []
            for i in range(len(responds)):
                datali.append(responds[i])
                self.handleData(datali)
            data = ','.join(datali)
        else:
            data = responds
            pass
        if sheet_name == "用例模板":
            # sheet_index=0
            col = 7  # 单元格所在列col
        else:
            col = 10
            pass
        # print(type(data))
        w_sheet.write(row, col, data)  # 写入坐标对应的单元格,row行list列responds写入值
        print("本次写入数据为：" + data)
        cpbook.save(my_excel)  # 保存文件

    # 通过openpyxl实现写入,处理xlsx
    def writexlsxCell(self, path, xls_name, sheet_name, cell_name, responds):
        my_excel = os.path.join(path, xls_name)  # 获取用例文件路径
        # print(my_excel)
        workbook1 = openpyxl.load_workbook(my_excel)  # 打开excel
        sheet = workbook1[sheet_name]  # 定位sheet
        row = doExcel.findLocation(self, path, xls_name, sheet_name, cell_name)  # 取单元格所在行
        # 数据类型转换
        # print(type(responds))
        if type(responds) == dict:
            data = json.dumps(responds, ensure_ascii=False)
        elif type(responds) == list:
            self.handleData(responds)
            data = ','.join(responds)
        elif type(responds) == tuple:
            datali = []
            for i in range(len(responds)):
                datali.append(responds[i])
                self.handleData(datali)
            data = ','.join(datali)
        else:
            data = responds
            pass
        if sheet_name == "用例模板":
            col = 7  # 单元格所在列col
        else:
            col = 10
            pass
        # print(type(data))
        sheet.cell(row=row+1, column=col+1).value = data  # 写入数据
        print("本次写入数据为：" + data)
        workbook1.save(my_excel)  # 保存修改


if __name__ == '__main__':#我们执行该文件测试一下是否可以正确获取Excel中的值
      parent_path = os.path.dirname(get_Path())  #拿到父级目录地址
      # print(parent_path)
      data_path = parent_path+'\\app\cn\housebroker\data'
      # print(doExcel().read_xls(data_path, 'UI模板.xlsx', '用例模板', u'broker_login'))
      # print(doExcel().read_xls(data_path, 'UI模板.xlsx', '用例模板', u'broker_login')[0][1])
      # doExcel().findLocation(data_path, 'UI模板.xlsx', '用例模板', 'report_customer')
      # doExcel().writeCell(data_path, 'UI模板.xlsx', '用例模板', 'report_customer', ["通过1", "通过2", {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}])
      # doExcel().writeCell(data_path, 'UI模板.xlsx', '用例模板', 'enterprise_Certify', {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]})
      # doExcel().writeCell(data_path, 'UI模板.xlsx', '用例模板', 'lounch_Look', "成功")
      doExcel().writeCell(data_path, 'UI模板.xls', '用例模板', 'broker_register', "1,2,3")
      doExcel().writexlsxCell(data_path, 'UI模板.xlsx', '用例模板', 'typeIn_customer', ["通过1", "通过2", {'bigberg': [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}])