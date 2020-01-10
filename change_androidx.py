#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

replaceDict = {}


def do_replace(java):
    print(java)
    f = open(java, 'r')
    alllines = f.readlines()
    f.close()
    f = open(java, 'w+')
    for eachline in alllines:
        for replace_str in replaceDict.keys():
            a = re.sub(replace_str, replaceDict[replace_str], eachline)
        f.writelines(a)
    f.close()


def replace(javaList):
    for java in javaList:
        do_replace(java)


# 遍历文件夹
def walkFile(path):
    javaList = []
    for root, dirs, files in os.walk(path):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            if root.__contains__("build"):
                break
            if f.endswith(".xml") or f.endswith(".java"):
                javaPath = os.path.join(root, f)
                javaList.append(javaPath)
    replace(javaList)


def doAndroidXchange():
    path = "/home/zixiangliu/project/pateo/ArielAPP_QingPhoto/ArielAPP/"
    walkFile(path)
    replaceDict["android.support.v7.widget.Toolbar"] = "androidx.appcompat.widget.Toolbar"
    replaceDict["android.support.annotation.Nullable"] = "androidx.annotation.Nullable"
    replaceDict["android.support.v7.widget.AppCompatImageView"] = "androidx.appcompat.widget.AppCompatImageView"
    replaceDict["android.support.annotation.ColorInt"] = "androidx.annotation.ColorInt"
    replaceDict["android.support.v7.widget.RecyclerView"] = "androidx.recyclerview.widget.RecyclerView"


if __name__ == '__main__':
    doAndroidXchange()
