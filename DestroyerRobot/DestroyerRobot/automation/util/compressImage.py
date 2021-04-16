#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020\06\23 12:48:09
# @File    : compressImage.py

from PIL import  Image
import  os
from PIL import ImageDraw
"""
图片压缩
"""
class fix_image:

    def get_size(self,file):
        """
        获取文件大小：kb
        :param file:
        :return:
        """
        size = os.path.getsize(file)
        return  size/1024


    def get_outfile(self,infile, outfile):
        if outfile:
            return outfile
        dir, suffix = os.path.splitext(infile)
        outfile = '{}-out{}'.format(dir, suffix)
        return outfile

    def compress_image(self,infile, outfile='', mb=400, step=30, quality=60):
        """不改变图片尺寸压缩到指定大小
        :param infile: 压缩源文件
        :param outfile: 压缩文件保存地址
        :param mb: 压缩目标，KB
        :param step: 每次调整的压缩比率
        :param quality: 初始压缩比率
        :return: 压缩文件地址，压缩文件大小
        """
        o_size = self.get_size(infile)
        if o_size <= mb:
            return infile
        outfile = self.get_outfile(infile, outfile)
        while o_size > mb:
            im = Image.open(infile)
            im.save(outfile, quality=quality)
            if quality - step < 0:
                break
            quality -= step
            o_size = self.get_size(outfile)
        return outfile, self.get_size(outfile)


    def resize_image(self,infile, outfile='', x_s=12005):
        """修改图片尺寸
        :param infile: 图片源文件
        :param outfile: 重设尺寸文件保存地址
        :param x_s: 设置的宽度
        :return:
        """
        im = Image.open(infile)
        x, y = im.size
        y_s = int(y * x_s / x)
        out = im.resize((x_s, y_s), Image.ANTIALIAS)
        outfile = self.get_outfile(infile, outfile)
        out.save(outfile)





if __name__=="__main__":

    #输入文件夹，文件下的图片名称遍历将大于500kb的图片压缩到450kb,压缩后生成到当前目录
    #file = 'C:\\Users\\vivid\\Desktop\\bug\\认证'

    # list = os.listdir(file)  # 列出文件夹下所有的目录与文件
    # for i in range(0, len(list)):
    #     path = os.path.join(file, list[i])
    #     # if os.path.isfile(path):
    #     # # 你想对文件的操作
    #     image_size=fix_image().get_size(path)
    #     #print(path)
    #     if int(image_size) < 100:
    #
    #         print("不压身图片",image_size)
    #     else:
    #         print("开始压缩图片",image_size)
    #         #compress_image(path)
    #         fix_image().resize_image(path)
    # #compress_image(file)
    yuanfile = "C:\\Users\\vivid\\Desktop\\bug\\yuan.png"
    difile = "C:\\Users\\vivid\\Desktop\\bug\\di2.png"

    images = fix_image().get_water2(yuanfile,difile)
