#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:15
# @Author  : 路培强
# @FileName: MySQLDB.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import logging
from DestroyerRobot.automation.util.SystemOsUtil import SystemOs
from DestroyerRobot.automation.util.ConfigUtil import Config


class Log:
    def __init__(self,logs="logs_root"):
        """
        日志信息
        """
        self.logs = logs
    def logger(self):
        """
        封装一个记录的日志方法
        :return:
        """

        # 创建一个logger
        logger = logging.getLogger("myLogger")
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        conf = Config("FilePath")
        log_path=conf.get_path_config(self.logs)

        log_file = logging.FileHandler(SystemOs().sys_path(log_path))
        log_file.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        log_file.setFormatter(formatter)
        console.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(log_file)
        logger.addHandler(console)
        return logger

if __name__=='__main__':
    log = Log().logger()
    log.info("点击【%s】的【%s】元素" %("你好","时间"))