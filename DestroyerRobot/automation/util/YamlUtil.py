#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/3/5 11:34
# @Author  : vivid
# @FileName: yamlutil.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import yaml

class yamlUtil:
    def __init__(self,yamlpath):
        self.yamlpath = yamlpath

    def get_yalm(self):
        """
        读取数据
        :return:
        """
        try:
            with open(self.yamlpath, "r", encoding="utf-8") as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
        except AttributeError:
            with open(self.yamlpath, "r", encoding="utf-8") as f:
                data = yaml.load(f)
        finally:
            return data

    def write_yaml(self,data):
        # 写入数据：
        # data = {"S_data": {"test1": "hello"}, "Sdata2": {"name": "汉字"}}
        with open(self.yamlpath, "a+", encoding="utf-8") as f:
            f.write("\n")
            yaml.dump(data, f, allow_unicode=True)

    def update_yaml(self,param,data):
        with open(self.yamlpath, "r", encoding="utf-8") as f:
            content = yaml.load(f, Loader=yaml.FullLoader)

        content[param] = data
        with open(self.yamlpath, 'w') as f:
            yaml.safe_dump(content, f, default_flow_style=False)



if __name__=="__main__":
    datainfo = yamlUtil("C:/Users/vivid/PycharmProjects/untitled/DestroyerRobot/yaml_file/header_cms.yaml").get_yalm()
    print(datainfo)





