#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/3/7 21:15
# @Author : vivid
# @FileName: testPytest.py
# @Software: PyCharm

"""
此文件是为了测试 pytest脚本如何使用
"""
import pytest
# def func(x):
#     return x+1
#
# def test_answer():
#     assert func(3)==6
#
# if __name__ == '__main__':
#
#     test_answer()

class TestClass:
    def test_one(self):
        x= 'this'
        assert 'h' in 'x'

    def test_two(self):
        x = "hello"
        assert hasattr(x,'check')

    def test_three(self):
        assert  1==2


if __name__ == '__main__':
    t = TestClass()
    t.test_three()