#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:15
# @Author  : vivid
# @FileName: MySQLDB.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import os,sys
class SystemOs:
    def __init__(self,project_paths='DestroyerRobot'):
        self.project_paths = project_paths

    def is_file(self, filepath):
        """

        :param filepath:
        :return:
        """
        pathBoolean = False
        try:
            if os.path.isfile(filepath):
                pathBoolean = True
        except Exception as e:
            print(e)
        return pathBoolean

    def remove_file(self, filepath):
        """
        删除指定文件
        :param filepath:
        :return:
        """
        isfile = self.isFile(filepath)
        msg = ""
        try:
            if isfile:
                os.remove(filepath)
                msg = "文件删除成功"
            else:
                msg = "文件不存在"
        except Exception as e:
            print(e)
        return msg

    def mkdirs_file(self, dirpath):
        """
        创建文件目录，先判断文件目录是否存在
        :param dirpath:
        :return:
        """
        if os.path.isdir(dirpath):
            print("目录已经存在，不用创建")
        else:
            os.mkdir(dirpath)

    """
        获取文件路径操作,建议使用sys_path函数进行操作。
    """
    def project_path(self):
        """
        返回项目的根目录 ，
        :return:
        """
        # 获取根项目路径
        curPath = os.path.dirname(__file__)
        #print("curPath==============",curPath)
        rootPath = curPath[:curPath.find(self.project_paths) + len(self.project_paths)]
        #print("rootPath==============",rootPath)
        return rootPath

    def sys_path(self, *paths):
        """
        将多个路径组合后返回，第一个绝对路径之前的参数将被忽略，为空 返回rootPath路径， "/"为分隔符
        :param paths:
        :return:返回文件路径
        """
        sysPath = os.path.join(self.project_path(), *paths)
        sysOsPath = sysPath.replace('\\', '/')
        return sysOsPath

if __name__ == "__main__":
    s = SystemOs()
    paths="automation/app/cn/apk/经纪人测试.apk"
    print(s.sys_path(paths))




