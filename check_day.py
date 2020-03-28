#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:check_day.py
@time:2020/03/27
"""
# -*- coding:utf-8 -*-
import json

import requests

date = "20170530"
server_url = "http://www.easybots.cn/api/holiday.php?d="

vop_url_request = requests.get(server_url + date)
# vop_response = request.urlopen(vop_url_request)

vop_data = json.loads(vop_url_request.read())

print(vop_data)

if vop_data[date] == '0':
    print
    "this day is weekday"
elif vop_data[date] == '1':
    print
    'This day is weekend'
elif vop_data[date] == '2':
    print
    'This day is holiday'
else:
    print
    'Error'
