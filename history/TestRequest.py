#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/20 23:57
# @Author  : Elegant
# @Site    : 
# @File    : TestRequest.py
# @Software: PyCharm Community Edition

import requests

r = requests.post('http://httpbin.org/post')
print( r.status_code)
print(r.text)