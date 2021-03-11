# -*- coding:utf-8 -*-
import urllib.request

def downloadImg(imgPaht,url,filename):
    """

    :param imgPaht: "D:\\Download"
    :param url:
    :param filename:
    :return:
    """
    conn = urllib.request.urlopen(url)
    f = open(imgPaht+'/'+filename,'wb')
    f.write(conn.read())
    f.close()