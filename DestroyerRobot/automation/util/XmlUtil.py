# _*_ coding: utf-8 _*_

# @Time         : 2019-03-23 11:30
# @Author        : 路培强
# @Email         : 136024009@qq.com
# @File          :XmlUtil.py
# @Software      :PyCharm

import xml.dom.minidom as xmldom

class XmlUtil:
    def __init__(self, xml_filepath):
        self.page_list = self.xml_util(xml_filepath)

    def xml_util(self, xml_filepath):
        """
        解析xml（定位元素的方式）
        :param xml_filepath: 路径
        :return:
        """
        # 使用minidom解析器打开 XML 文档
        #print("xml文件路径：", xml_filepath)
        # 得到文档对象
        DOMTree = xmldom.parse(xml_filepath)
        # 得到元素对象
        root = DOMTree.documentElement
        # 获得子标签
        pages_element = root.getElementsByTagName("Page")
        # for i in pages_element:
        #     print(i.getAttribute("keyword"))
        page_list = []
        for page_element in range(len(pages_element)):
            ui_list = []
            #print(page_element)
            page_dict = {"keyword": "", "UIElement": ""}
            page_keyword = pages_element[page_element].getAttribute("keyword")
            ui_elements = pages_element[page_element].getElementsByTagName("UIElement")
            for ui_element in range(len(ui_elements)):
                ui_dict = {"keyword": "", "by": "", "UIElement": ""}
                keyword = ui_elements[ui_element].getAttribute("keyword")
                by = ui_elements[ui_element].getAttribute("by")
                value = ui_elements[ui_element].getAttribute("value")
                ui_dict["keyword"] = keyword
                ui_dict["by"] = by
                ui_dict["value"] = value
                ui_list.append(ui_dict.copy())
            page_dict["keyword"] = page_keyword
            page_dict["UIElement"] = ui_list
            page_list.append(page_dict)
        return page_list


    def xml_parsing(self,page_keyword, ui_keyword):
        by = None
        value = None
        for i in self.page_list:
            if page_keyword == i["keyword"]:
                ui_element = i["UIElement"]
                for j in ui_element:
                    if j["keyword"] == ui_keyword:
                        by = j["by"]
                        value = j["value"]
                        return by, value
        return by, value
if __name__ == '__main__':
    filepath = 'C:/Users/vivid/PycharmProjects/untitled/DestroyerRobot/automation/app/cn/Customer/data/fristpage/fristpage.xml'
    xmls= XmlUtil(filepath)


    s = xmls.xml_parsing("首页","客户管理")
    print(s)
    # m = xmls.xml_parsing("首页","客户管理")
    # print(m)

