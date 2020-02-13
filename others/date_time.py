#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   date_time.py
@Time    :   2020/02/12 20:13:05
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from datetime import datetime

now = datetime.now()
print(now)

dt = datetime(2020,2,12,22,5)
print(dt.timestamp()/1000)
