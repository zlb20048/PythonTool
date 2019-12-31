#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import tinify
import time
from multiprocessing.pool import Pool


def get_time_stamp():
    now_milli_time = int(time.time() * 1000)
    return now_milli_time


def getCompressCount():
    print("is already used ", tinify.tinify.compression_count)


def threadCompress(imgs):
    # 启用多线程压缩提高压缩速度
    startTime = get_time_stamp()
    p = Pool(4)
    for path in imgs:
        p.apply_async(compressPng, args=(path,))

    p.close()
    p.join()
    endTime = get_time_stamp()
    print("total used %f s", (endTime - startTime) / 1000)


def compressPng(imagePath):
    tinify.tinify.from_file(imagePath).to_file(imagePath)


# 遍历文件夹
def walkFile(file):
    imgs = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if root.__contains__("build"):
                break
            if f.endswith(".png"):
                imagePath = os.path.join(root, f)
                imgs.append(imagePath)
    threadCompress(imgs)


def doTinypng():
    tinify.key = "CrXJrQCjVMwRfywf9lfGcDNbmrnB1H6W"
    # ret = input('请填写需要压缩图片目录')
    # path = "/work/home/eric/source/QingV2_Flutter/package/qingv2/bundle_trainticket"
    path = "/home/zixiangliu/Desktop"
    walkFile(path)


if __name__ == '__main__':
    doTinypng()
