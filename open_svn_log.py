#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:zixiangliu
@file:open_svn_log.py
@time:2020/01/14
"""
import os
import sys

import pexpect


def do_open_vpn_login():
    child = pexpect.spawn(
        'sudo openvpn --config /home/zixiangliu/bdconfig/bdclient.ovpn --ca '
        '/home/zixiangliu/bdconfig/ca.crt --tls-auth /home/zixiangliu/bdconfig/ta.key')
    logfile = "logfile.txt"
    if os.path.exists(logfile):
        os.remove(logfile)

    # logFileId = open(logfile, 'wb')
    # child.logfile = logFileId
    child.expect('zixiangliu')
    child.sendline("pateo")
    child.expect('Username:')
    child.sendline("huizhang")
    child.expect('Password')
    child.sendline('Hui#@*2019')
    child.expect(pexpect.EOF)


if __name__ == '__main__':
    do_open_vpn_login()
