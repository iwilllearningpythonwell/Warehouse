#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time    : 2021/3/11
# @Author  : hopsonxw
# @FileName: practice.py
# @Software: PyCharm
# @email    ：190135@lifeat.cn

def bubble_Sort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(i+1, n):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li

if __name__ == '__main__':
    list = [0,2,5,3,8,6,4]
    ls= bubble_Sort(list)
    print(ls)