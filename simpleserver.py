#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/15 23:10
# @Author  : Elegant
# @Site    : 
# @File    : simpleserver.py
# @Software: PyCharm

import socket
s= socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)

while True:
    c, addr = s.accept()
    print ('Got connection from',addr)
    c.send('Thank you for connecting')
    c.close()


