#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/7/28
# @FileName: test_mp_login.py
# @Software: PyCharm

from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.ConfigUtil import Config
import datetime
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import traceback
# 处理图片需要 MIMEImage 类
from email.header import Header

class Email:
    def __init__(self,reportPath):
        self.reportPath = reportPath

    def sendEmail(self):
        config = Config("Email")
        fromAddress = config.get_email("fromaddress")
        password = config.get_email("password")
        toAddress = config.get_email("toAddress").split(",")

        #主题
        content = "您好：\n  测试已完成，详情请查看附件报告！\n  祝好"
        textApart = MIMEText(content)
        m = MIMEMultipart()
        openFile = open(self.reportPath, 'rb')
        addFile = openFile.read()
        apart = MIMEApplication(addFile)
        openFile.close()
        apart.add_header('Content-Disposition', 'attachment', filename="report.html")
        m.attach(apart)
        m.attach(textApart)
        now_time = datetime.datetime.now().strftime('%Y-%m-%d')
        m["Subject"] = "测试报告" + now_time
        try:
            server = smtplib.SMTP('smtp.163.com')
            server.login(fromAddress, password)
            server.sendmail(fromAddress, toAddress, m.as_string())
            print('success')
            server.quit()
        except smtplib.SMTPException as e:
            print(traceback.format_exc())


if __name__ == "__main__":
    files = "E:\\python_workspace\\DestroyerRobot\\automation\\com\\cn\\markerting_points\\report\\测试报告2019_07_30_21_48_35.html"
    Email(files).sendEmail()
