#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import time


def get_time_stamp():
    now_milli_time = int(time.time() * 1000)
    return now_milli_time


def statistics_chinese(all_file):
    chineses = []
    for file in all_file:
        file = open(file)
        for line in file.readlines():
            if line.__contains__("//") or line.__contains__("/**") or line.__contains__("*"):
                # print(line)
                break
            for x in range(0, len(line)):
                if '\u4e00' <= line[x] <= '\u9fff':
                    chineses.append(line[x])
        file.close()
    return chineses


def dowalkFile(file):
    javaList = []
    xmlList = []
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if root.__contains__("build"):
                break
            if f.endswith(".java"):
                javaList.append(os.path.join(root, f))
            if f.endswith(".xml"):
                xmlList.append(os.path.join(root, f))
    start_time = get_time_stamp()
    print("java文件: ", javaList.__sizeof__())
    chineses = statistics_chinese(javaList)
    print("java文件中汉字个数: ", chineses.__sizeof__())
    print("共有", list(set(chineses)).__sizeof__(), "个不同的汉字")
    end_time = get_time_stamp()
    print("耗时: ", (end_time - start_time), "ms")
    start_time = get_time_stamp()
    print("xml文件: ", xmlList.__sizeof__())
    chineses = statistics_chinese(xmlList)
    print("xml文件中汉字个数: ", chineses.__sizeof__())
    print("共有", list(set(chineses)).__sizeof__(), "个不同的汉字")
    end_time = get_time_stamp()
    print("耗时: ", (end_time - start_time), "ms")


if __name__ == '__main__':
    # ret = input("请输入需要检测的目录: \n")
    ret = "/home/zixiangliu/project/pateo/ArielAPP_QingPhoto/ArielAPP"
    print(ret)
    if ret == "":
        ret = os.getcwd()
    print(ret)
    dowalkFile(ret)
