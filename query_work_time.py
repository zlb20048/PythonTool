#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:query_work_time.py
@time:2020/03/27
"""
import time

import xlrd

filter_query_no = ["02639", "03590", "02574", "01949", "05516", "05572", "05862"]
all_my_partment = []

all_query_map = {}


def do_day_print():
    for name in all_query_map:
        # print("------%s--------" % name)
        print(name)
        eight_clock = all_query_map[name][0]
        ten_clock = all_query_map[name][1]
        aa = sorted(eight_clock.items(), key=lambda x: x[1])
        if aa.__len__() > 0:
            print("======工作到晚上8点, 天数 =", aa.__len__(), "饭补金额 =", str(35 * aa.__len__()))
            for i in aa:
                print(i[0], end=" ")
            print(" ")
            for i in aa:
                tmp = time.struct_time(i[1])
                print(str(tmp.tm_hour) + str(":") + str(tmp.tm_min), end=" ")
            print(" ")
        else:
            print("没有加班到晚上8点的记录", "\n")
        #
        aa = sorted(ten_clock.items(), key=lambda x: x[1])
        if aa.__len__() > 0:
            print("=======工作到晚上10点=======")
            for i in aa:
                print(i[0], end=" ")
            print(" ")
            for i in aa:
                tmp = time.struct_time(i[1])
                print(str(tmp.tm_hour) + str(":") + str(tmp.tm_min), end=" ")
            print("\n", " ")
        else:
            print("没有加班到晚上10点的记录", "\n")


def do_time(tmp_time, name):
    eight_clock = all_query_map[name][0]
    ten_clock = all_query_map[name][1]
    if tmp_time.tm_year == 2020 and tmp_time.tm_mon == 3:
        if tmp_time.tm_wday <= 5:
            if 20 <= tmp_time.tm_hour or tmp_time.tm_hour <= 6:
                eight_clock[str(tmp_time.tm_mon) + str(".") + str(tmp_time.tm_mday)] = tmp_time
            if 22 <= tmp_time.tm_hour or tmp_time.tm_hour <= 6:
                ten_clock[str(tmp_time.tm_mon) + str(".") + str(tmp_time.tm_mday)] = tmp_time


def do_query(rowVale, colNum):
    for no in all_my_partment:
        if rowVale[colNum] == no:
            name = rowVale[1]
            if name not in all_query_map:
                eight_list = {}
                ten_list = {}
                all_list = [eight_list, ten_list]
                all_query_map[name] = all_list
            tmp_time = time.strptime(rowVale[3], "%Y-%m-%d %H:%M")
            do_time(tmp_time, name)


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)

    for rowNum in range(table.nrows):
        rowVale = table.row_values(rowNum)
        for colNum in range(table.ncols):
            no = rowVale[0]
            if rowVale[2] == "APP研发组":
                if not all_my_partment.__contains__(no):
                    all_my_partment.append(no)
            do_query(rowVale, colNum)
    do_day_print()


if __name__ == '__main__':
    excelFile = '/home/zixiangliu/Desktop/打卡查询按钮.xlsx'
    read_xlrd(excelFile=excelFile)
