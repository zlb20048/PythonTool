#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:transform_file.py
@time:2020/01/09
"""
import os
import shutil
import sys
import time

replace_suffix = {".java": ".javax",
                  ".c": ".xc",
                  ".h": ".hx",
                  ".xml": ".xmlx",
                  ".png": ".pngx"}


def get_time_stamp():
    now_milli_time = int(time.time() * 1000)
    return now_milli_time


def cp_file(source, target):
    # source = '/home/zixiangliu/project/pateo/ArielAPP_QingPhoto/OnlineService'
    # target = '/home/zixiangliu/Desktop/OnlineService'
    ss = source.split('/')
    if ss[len(ss) - 1] != "":
        target = os.path.join(target, ss[ss.__len__() - 1])
    elif ss[len(ss) - 2] != "":
        target = os.path.join(target, ss[ss.__len__() - 2])
    else:
        print("no target menu")
        return
    print("target = ", target)
    if os.path.exists(target):
        ret = input("The dir is exists, remove of change back R C N :\n")
        if ret == "R":
            start_time = get_time_stamp()
            shutil.rmtree(target)
            # adding exception handling
            try:
                shutil.copytree(source, target)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())
            suffix = replace_suffix
        elif ret == "C":
            start_time = get_time_stamp()
            suffix = dict(zip(replace_suffix.values(), replace_suffix.keys()))
        else:
            print("Do Nothing")
            return

    do_transform_file(target, suffix)
    print("used time", get_time_stamp() - start_time, "ms")


def do_transform_file(path, suffix):
    for root, dirs, files in os.walk(path):
        # 遍历文件
        for f in files:
            if root.__contains__("build"):
                break
            for key in suffix.keys():
                if f.endswith(key):
                    source = os.path.join(root, f)
                    target = source.replace(key, suffix[key])
                    shutil.copy(source, target)
                    os.remove(source)
                    break


if __name__ == '__main__':
    # copy_tree(source, target)
    source = '/home/zixiangliu/project/pateo/ArielAPP_QingPhoto/OnlineService'
    target = '/home/zixiangliu/Desktop'
    cp_file(source, target)
    # do_transform_file(target)
