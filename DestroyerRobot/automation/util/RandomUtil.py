#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2019/6/14 9:32
# @Author  : vivid
# @FileName: testRandom.py
# @Software: PyCharm
# @email    ：331597811@QQ.com
import random
import time
class TestRamdom:
    """
    获取随机数类与取模
    """
    def __init__(self):
        pass

    def RandomTest(self):
        """
        获取随机数较大值 时间戳+随机数
        :return: 返回随机数
        """
        t=time.time()
        time.sleep(0.1)
        num = random.randint(0, 10000)
        randomnum = int(t)+int(num)
        return randomnum

    def RandomTestInt(self,num,randomNum=0):
        """
        获取指定范围的正数-随机数
        :param num:
        :return:
        """
        IntNum = random.randint(randomNum,num)
        return IntNum

    def RandomTestFloat(self,num,ndigits=2):
        """
        获取float类型数值
        :param num: 取值范围,
        :param ndigits:精度值，四舍五入，默认取值为2位小数
        :return:
        """
        FloatNum = random.uniform(0,num)
        FloatNum = round(FloatNum,ndigits)
        return FloatNum

    def RandomShang(self,num):
        """
        :param num:
        :return:quotient 商
        """
        randomnum=self.RandomTest()
        quotient = randomnum%num
        return quotient

    def choice(self,num):
        return random.choice(num)

    def choices(self,num):
        return random.choices(num)


if __name__=='__main__':

    # num = TestRamdom().RandomTestFloat(100)
    # print(num)
    lists=[1,2,3,4,5,6]
    s=random.choice(lists)
    print(s)
    c=random.choices(lists)
    print(c)
