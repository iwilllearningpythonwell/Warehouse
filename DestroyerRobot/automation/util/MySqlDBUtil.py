#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/6 17:15
# @Author  : vivid
# @FileName: MySQLDB.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import pymysql
from DestroyerRobot.automation.util.ConfigUtil import Config
#DestroyerRobot/DestroyerRobot/automation/com/cn/util/ConfigUtil.py
"""
bug 修复：传递参数时元祖接受值只能唯一，已修复
"""
class MysqlDB:
    def __init__(self):
        """
            数据库操作类    初始化
        """
        self.get_configMySql()

    def get_configMySql(self):
        conf= Config('MySqlDB')
        self.host = conf.get_mysqldb("db_host")
        self.uname = conf.get_mysqldb("db_user")
        self.passwd = conf.get_mysqldb("db_pwd")
        self.sqltable = conf.get_mysqldb("db_table")
        self.port = int(conf.get_mysqldb("db_port"))

    def getCursor(self,**kwargs):
        """
        获取数据库游标对象cursor
        游标对象，用于执行查询和获取结果
        :param kwargs:  可以 动态修改数据库相关配置信息
        :return: 返回游标
        """
        # 建立数据库链接,
        try:
            db_info = {
                "host": self.host,
                "uname": self.uname,
                "passwd": self.passwd,
                "sqltable": self.sqltable,
                "port": self.port  # self.port 为 int类型
            }
            dbinfo = list(db_info.keys())
            for k in kwargs.keys():
                if k in dbinfo:
                        #print("包含 %s" % k)
                    db_info[k]=kwargs[k]
            self.host = db_info["host"]
            self.uname = db_info["uname"]
            self.passwd = db_info["passwd"]
            self.sqltable = db_info["sqltable"]
            self.port = int(db_info["port"])
            self.db = pymysql.connect(self.host, self.uname, self.passwd, self.sqltable, self.port)
            # 创建游标对象
            cur = self.db.cursor()
            return cur
        except Exception as e:
            cur.close()
            print(e)


    def querydict(self, sql, *value):
        """
        执行sql语句分装成字典对象
        :param sql:
        :param value:
        :return:
        """
        try:
            # 建立链接获取游标对象
            cur = self.getCursor()
            # 执行sql语句
            cur.execute(sql, *value)
            # all 所有数据,one 取结果的一行.
            datList = cur.fetchall()
            print("datList:",datList)
            descList = cur.description
            print("descList:",descList)
            datcLists = []
            for i in descList:
                datcLists.append(i[0])
            print("datcLists:",datcLists)
            dataList = []
            for j in range(datList.__len__()):
                dicts = {}
                for i in range(datcLists.__len__()):
                    dicts[datcLists[i]] = datList[j][i]
                dataList.append(dicts)
            return dataList

        except Exception as e:
            print(e)
            # 异常数据回滚
            self.db.rollback()
        finally:
            cur.close()
            # 关闭链接
            self.db.close()
            # 返回数据

    def queryOperation(self,sql, *value):
        """
        查询操作数据
        :param sql: sql语句
        :param username: sql查询的字段
        :return: dataList 数据，row 行数
        """
        try:
            # 建立链接获取游标对象
            cur = self.getCursor()
            # 执行sql语句
            cur.execute(sql,*value)
            # 获取数据的行数
            row = cur.rowcount
            # 获取查询数据
            # fetch*
            # all 所有数据,one 取结果的一行，many(size),去size行
            datList = cur.fetchall()
            return datList,row

        except Exception as e :
            print(e)
            # 异常数据回滚
            self.db.rollback()
        finally:
            cur.close()
            # 关闭链接
            self.db.close()
            # 返回数据

    def deleteOperation(self, sql, *value):
        """
        删除操作
        :param sql:执行删除操作sql
        :return:null
        """
        # 获取游标
        cur = self.getCursor()
        try:
            # 执行sql语句
            cur.execute(sql,*value)
            # 正常结束事务
            self.db.commit()
        except Exception as e:
            print(e)
            # 异常数据回滚
            self.db.rollback()
        finally:
            cur.close()
            self.db.close()

    def updateOperation(self, sql, *value):
        """
        更新操作,部分操作说明参考deleteOperation()函数
        :param sql: 更新语句
        :return: null
        """

        cur = self.getCursor()
        try:
            cur.execute(sql,*value)
            # 正常结束事务
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            cur.close()
            self.db.close()

    def insertOperation(self, sql, *value):
        """
        插入操作，部分操作说明参考deleteOperation()函数
        :param sql:
        :return: null
        """

        cur = self.getCursor()
        try:
            cur.execute(sql,*value)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        finally:
            cur.close()
            self.db.close()
#
if __name__=='__main__':
    my = MysqlDB()
    my.getCursor(sqltable="easylife_ysis")
    sql = "SELECT * FROM easylife_BD_debt "

    dataList = my.querydict(sql)
    print(dataList)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(dataList.__len__())
    # my = MysqlDB()
    # my.getCursor()
    # sql = "SELECT * FROM u_user where mobile='15811478363' "
    #
    # dataList = my.queryOperation(sql)[0]
    #
