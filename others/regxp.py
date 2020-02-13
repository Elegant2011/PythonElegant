#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   regxp.py
@Time    :   2020/02/12 17:52:12
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import re

print(re.match(r'^\d{3}\-\d{3,8}$','010-12345')) 
print("")
print(re.match(r'^\d{3}\-\d{3,8}$','010 12345'))

#切分字符串
print('a b   c'.split(' '))
print(re.split(r'\s+','a b  c'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

#贪婪匹配
print(re.match(r'^(\d+)(0*)$', '102300').groups())

# 非贪婪匹配
print(re.match(r'^(\d+?)(0*)$','102300').groups())

def is_valid_email(addr):
    m = re.match(r'^[0-9a-zA-Z.]+@\w+.com',addr)
    print(addr,m)
    if m !=None:
       return True
    return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')