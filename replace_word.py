#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:replace_word.py
@time:2020/02/17
"""

# 遍历文件夹
import os
import re

order_key = {"fontSize:": "DHelper.setSp(", "width:": "DHelper.setWidth(", "height:": "DHelper.setHeight(",
             "left:": "DHelper.setWidth(", "right:": "DHelper.setWidth(", "top:": "DHelper.setHeight(",
             "bottom:": "DHelper.setHeight("}


def check_used(content_list):
    is_used = False
    for content in content_list:
        file = open(content, 'r')
        alllines = file.readlines()
        file.close()
        file = open(content, 'w+')

        for line in alllines:
            a = re.sub("", "", line)
            for key in order_key.keys():
                if key in line:
                    # has key , we will replace it
                    splits = line.split(key)
                    result = splits[1]
                    currentNunber = result.split(",")[0]
                    currentNunber = currentNunber.split(")")[0]
                    if currentNunber.strip().isdigit():
                        order_str = key  + currentNunber
                        new_str = key + " " + order_key[key] + currentNunber.strip() + ")"
                        a = re.sub(order_str, new_str, line)
            file.write(a)
        file.close()
    return is_used


def replace_word(list):
    check_used(list)


def walkFile(file):
    list = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if root.__contains__("build"):
                break
            if f.endswith(".dart"):
                path = os.path.join(root, f)
                list.append(path)
    replace_word(list)


if __name__ == '__main__':
    path = "/home/zixiangliu/project/pateo/flutter/qingv2/package/qingv2/bundle_trainticket"
    walkFile(path)
