#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/18 11:26
# @Author  : vivid
# @FileName: testDateTime.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import datetime
import time
class TestDateTime:
    def __init__(self):
        pass
    def time_stamp(self):
        """
        时间戳
        :return:
        """
        t=time.time()
        return t
    def chioce_time(self,times=0):
        """
        :param times: 增加的秒数
        :return:
        """
        t = time.time()+times
        chioce_times=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
        return chioce_times

    def local_time(self):
        """
        获取本地时间
        :return:
        """
        local_times=time.strftime("%Y-%m-%d %X", time.localtime())
        return local_times
    def local_day(self):
        """
        获取本地日期
        :return:
        """

        local_times=time.strftime("%Y-%m-%d", time.localtime())
        return local_times

    def report_file(self):
        """
        获取文件日期时间后缀
        :return:
        """

        local_times = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        return local_times


if __name__=='__main__':
    td = TestDateTime()
    # t=td.chioce_time(60*60*24*10)
    # t=str(t)
    # print(t)
    # k,v=t.split(" ")
    # print(k)
    # print(v)
    t=td.local_time()

    print(t)

