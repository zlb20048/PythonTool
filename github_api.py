#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:github_api.py
@time:2020/01/13
"""

import requests as r

url = "https://api.github.com/search/repositories?q=language:java&sort"
import json

L = json.loads(r.get(url).text)
for item in L['items'][:10]:
    print(item['html_url'])
