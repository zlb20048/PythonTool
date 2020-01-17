#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import subprocess

dartList = []
dictImage = {}

except_paths = [
    "bundle_trainticket",
    "bundle_violation",
    "bundle_movieticket",
    "app_refuel",
    "app_washcar",
    "build",
    "ios",
    "android",
]


def do_grep(path, key_word):
    command = "grep -w -q '%s' '%s'" % (key_word, path)
    if subprocess.call(command, shell=True) == 0:
        return 1
    else:
        return 0


def is_need_delete(key, dartList):
    is_need_delete = True
    for dart in dartList:
        file = open(dart)
        for line in file.readlines():
            if key in line:
                is_need_delete = False
                break
        file.close()
    return is_need_delete


def delete_image(dictImage, dartList):
    for image in dictImage.keys():
        if is_need_delete(image, dartList):
            print("is need to delete ", dictImage[image])
            os.remove(dictImage[image])


def is_inside_path(root):
    is_except = False
    for do_not_check_path in except_paths:
        if root.__contains__(do_not_check_path):
            is_except = True
            break
    return is_except


def save_images(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        if is_inside_path(root):
            continue
        # 遍历文件
        for f in files:
            if f.endswith(".png"):
                dictImage[f] = os.path.join(root, f)
                break
            if f.endswith(".dart"):
                dartList.append(os.path.join(root, f))


def doImageCheck():
    print("doImageCheck...")
    save_images("/home/zixiangliu/project/pateo/flutter/qingv2/package/qingv2")
    delete_image(dictImage, dartList)


if __name__ == '__main__':
    doImageCheck()
