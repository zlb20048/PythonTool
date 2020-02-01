#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:check_java_png.py
@time:2020/01/20
"""
import os

content_list = []
used_xml = {}
images = {}

except_paths = [
    "build",
    ".idea",
]


def is_inside_path(root):
    is_except = False
    for do_not_check_path in except_paths:
        if root.__contains__(do_not_check_path):
            is_except = True
            break
    return is_except


def find_png(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        if is_inside_path(root):
            continue
        # 遍历文件
        for f in files:
            if f.endswith(".png"):
                images[f.split(".")[0]] = os.path.join(root, f)
            if f.endswith(".xml"):
                used_xml[f.split(".")[0]] = os.path.join(root, f)
            if f.endswith(".java") or f.endswith(".xml"):
                content_list.append(os.path.join(root, f))


def check_used(key):
    is_used = False
    for content in content_list:
        file = open(content)
        for line in file.readlines():
            if key in line:
                is_used = True
                break
        file.close()
    return is_used


def do_check_png():
    x = 0
    for key in images.keys():
        if not check_used(key):
            x = x + 1
            print("delete ", x, ":", images[key])
            os.remove(images[key])


def do_check_xml():
    x = 0
    for key in used_xml.keys():
        if not check_used(key):
            x = x + 1
            print("delete ", x, ":", used_xml[key])
            content_list.remove(used_xml[key])
            os.remove(used_xml[key])


if __name__ == '__main__':
    ret = "/home/zixiangliu/project/pateo/ArielAPP_QingPhoto/ArielAPP"
    find_png(ret)
    do_check_xml()
    do_check_png()
