#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 21:54
# @Author  : Elegant
# @Site    : 
# @File    : click.py
# @Software: PyCharm
import requests
import time

headers = {
    'Host':"localhost",
    'Accept-Language':"zh-CN,zh;q=0.8",
    'Accept-Encoding':"gzip, deflate",
    'Content-Type':"application/x-www-form-urlencoded",
    'Connection':"keep-alive",
    'Referer':"http://localhost/login",
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
}
#while 1:
r =requests.get('https://h5.qzone.qq.com/weishi/feed/BpXSRAaML1wqU2yNDO4Xhe/wsfeed?_proxy=1&_wv=1&id=BpXSRAaML1wqU2yNDO4Xhe')
print( r.status_code)
time.sleep(0.2)
print(r.text)
