#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ppurllib.py
@Time    :   2020/02/13 15:25:25
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib


# import urllib3
# http = urllib3.PoolManager()  # 创建请求
# ret = http.request('GET', 'www.baidu.com')  # 返回一个 HTTPResponse 对象
# print(ret.status)  # 返回状态 200/404/...
# # print(ret.headers)  # 返回的数据

# for k in ret.headers:
#     print('%s: %s' % (k, ret.getheader(k)))




from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))