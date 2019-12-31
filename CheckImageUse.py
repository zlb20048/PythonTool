#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import subprocess


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


def save_images(file):
    dartList = []
    dictImage = {}
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if root.__contains__("build"):
                break
            if f.endswith(".png"):
                dictImage[f] = os.path.join(root, f)
            if f.endswith(".dart"):
                dartList.append(os.path.join(root, f))
    delete_image(dictImage, dartList)


def doImageCheck():
    print("doImageCheck...")
    paths = ["/work/home/eric/source/QingV2_Flutter/package/qingv2/bundle_hotel",
             "/work/home/eric/source/QingV2_Flutter/package/qingv2/qingv2_config",
             "/work/home/eric/source/QingV2_Flutter/package/qingv2/bundle_car_gas",
             # "/work/home/eric/source/QingV2_Flutter/package/qingv2/bundle_takeaway",
             "/work/home/eric/source/QingV2_Flutter/package/qingv2/bundle_washcar"]
    # paths = [
    #          "/work/home/eric/source/project/q2fe_wuling/q2fe-steward.wuling/q2fe-bundle/qingv2_config",
    #          "/work/home/eric/source/project/q2fe_wuling/q2fe-steward.wuling/q2fe-bundle/bundle_car_gas",
    #          "/work/home/eric/source/project/q2fe_wuling/q2fe-steward.wuling/q2fe-bundle/bundle_washcar"]

    for path in paths:
        save_images(path)


if __name__ == '__main__':
    doImageCheck()
