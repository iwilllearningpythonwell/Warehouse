#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: vivid
@file: JosnUtil.py
@time: 2020/5/20 23:24
@software: PyCharm
@email: 331597811@QQ.com
@desc: json tool
"""
import json

class JsonUtils:
    def __init__(self):
        pass

    def json_dumps(self,data):
        """
        将 Python 对象编码成 JSON 字符串
        :param data:
        :return:
        """
        jsondata = json.dumps(data)
        return jsondata

    def json_loads(self,data):
        """
        将已编码的 JSON 字符串解码为 Python 对象
        :param data:
        :return:
        """
        jsontext = json.loads(data)
        return  jsontext


if __name__ == '__main__':
    stus =  '{"loginName":"13600000001","password":"123456","loginSysName":"bonus"}'
    s = JsonUtils().json_loads((stus))
    print(s)