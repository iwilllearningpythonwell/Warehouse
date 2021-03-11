 #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2020/1/15 11:34
# @Author  : vivid
# @FileName: MongoUtil.py
# @Software: PyCharm
# @email    ：331597811@QQ.compymongo
import pymongo
from DestroyerRobot.automation.util.ConfigUtil import Config
class MongoUtil:
    """
    操作mongoDB数据工具类文件
    """
    def __init__(self):
        self.get_configMongoDb()

    def get_configMongoDb(self):
        conf = Config('MongoDB')
        self.host = conf.get_mongodb("mongo_host")
        self.port = conf.get_mongodb("mongo_port")
        self.mongodb = conf.get_mongodb("mongo_db")
        self.mongo_mycol = conf.get_mongodb("mongo_mycol")

    def get_connect_client(self,**kwargs):
        """
        目前对应的测试服务器没有相关的密码,所以password相关解析为空，mongodb配置信息：mongodb="mongodb://10.2.39.129:27017",db="easylife",mycol='CustomerFollow
        :param kwargs:  可以 动态修改mongo数据库相关配置信息
        :return:
        """
        try:
            db_info={
                "host" :self.host,
                "port" :self.port,
                "mongdb" : self.mongodb,
                "mongo_mycol" : self.mongo_mycol
            }
            dbinfo = list(db_info.keys())
            for k in kwargs.keys():
                if k in dbinfo:
                    db_info[k]=kwargs[k]
            self.host = db_info["host"]
            self.port = db_info["port"]
            self.mongdb = db_info["mongdb"]
            self.mongo_mycol = db_info["mongo_mycol"]
            mongodb = self.host+":"+self.port
            self.connect_client = pymongo.MongoClient(mongodb)
            self.mydb = self.connect_client[self.mongodb]  # 连接指定数据库
            self.mycol = self.mydb[self.mongo_mycol]
        except Exception as e:
            """关闭mongo 数据库"""
            self.connect_client.close()
            print(e)


    # def __init__(self,mongodb="mongodb://10.2.39.129:27017",db="easylife",mycol='CustomerFollow'):
    #     """
    #     初始化链接
    #     :param db: 服务器地址
    #     myclient = pymongo.MongoClient("mongodb://10.2.39.129:27017")
    #     mydb = myclient["easylife"]
    #     #获取easylife  mongo库
    #     # collist = mydb.list_collection_names()
    #     # if "CustomerFollow" in collist:
    #     mycol = mydb['brokerage_broker_apply_operation']
    #     """
    #     self.connect_client = pymongo.MongoClient(mongodb)
    #     self.mydb = self.connect_client[db]  # 连接指定数据库
    #     self.mycol= self.mydb[mycol]

    def close_connect(self):
        self.connect_client.close()
        return 'mongo连接已关闭'

    def select_one(self):
        """
        find_one() 方法来查询集合中的一条数据
        :param search_col:
        :return:
        """
        try:
            result =self.mycol.find_one()
            return  result
        except TypeError as e:
            print("查询条件错误"+e)
        finally:
            self.close_connect()

    def select_all(self,limits=0):
        """
        查询出所有数据，数据量比较大时，过于消耗性能,
        默认limit限制为0,查询为条件语句全部内容
        :return:
        """
        try:
            result = self.mycol.find().limit(limits)
            return result
        except TypeError as e:
            print("查询条件错误"+e)
        finally:
            self.close_connect()

    def select_many(self,myquery,limits=0):
        """
        条件查询,默认limit限制为0,查询为条件语句全部内容
        myquer:   myquer={"customer_phone":"17033733446"}
        :return:
        """
        try:
            result = self.mycol.find(myquery).limit(limits)
            return  result
        except TypeError as e:
            print("查询条件错误")
        finally:
            self.close_connect()

    def inser_one(self,mydict):
        """
        插入数据 mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
        :return:
        """
        try:
            self.mycol.insert_one(mydict)
            return  True
        except TypeError as e:
            print("查询条件与需要修改的字段只能是dict类型"+e)
        finally:
            self.close_connect()

    def insert_many(self,mylist):
        """
        插入多条数据，
        :param mylist:
        :return:
        """
        try:
            self.mycol.insert_many(mylist)
            return True
        except TypeError as e:
            print("查询条件与需要修改的字段只能是dict类型"+e)
        finally:
            self.close_connect()


    def update_one(self,myquery,newvalues):
        """
        将 alexa 字段的值 10000 改为 12345:
        :param myquery:   myquery = { "alexa": "10000" }
        :param nwevalues: newvalues = { "$set": { "alexa": "12345" } }
        :return:
        """
        try:
            self.mycol.update_one(myquery,newvalues)
            return  True
        except TypeError as e:
            print("查询条件与需要修改的字段只能是dict类型"+e)
        finally:
            self.close_connect()

    def update_many(self, myquery, newvalues):
        """
        以下实例将查找所有以 F 开头的 name 字段，并将匹配到所有记录的 alexa 字段修改为 123：
        :param myquery:   myquery = { "name": { "$regex": "^F" } }
        :param nwevalues: newvalues = { "$set": { "alexa": "12345" } }
        :return:
        """
        try:
            self.mycol.update_many(myquery, newvalues)
            return True
        except TypeError as e:
            print("查询条件与需要修改的字段只能是dict类型" + e)
        finally:
            self.close_connect()

    def delete_one(self,myquery):
        try:
            self.mycol.delete_one(myquery)
            return  True
        except TypeError as e:
            print("查询条件与需要修改的字段只能是dict类型" + e)
        finally:
            self.close_connect()

    def delete_many(self,myquery):
        """
        :param myquery: myquery = { "name": {"$regex": "^F"} }

        :return:
        """
        try:
            self.mycol.delete_many(myquery)
            return  True
        except TypeError as e:
            print("查询条件与需要修改的字段只能是dict类型" + e)
        finally:
            self.close_connect()




if __name__=="__main__":
    mongoutil=MongoUtil()
    # result =mongo.select_one()
    # print(result)





    # mydoc = mongoutil.select_many(myquery)
    # idlist=[]
    # for x in mydoc:
    #     idlist.append(x['_id'])

    # print(idlist[1])
    mongoutil.get_connect_client()