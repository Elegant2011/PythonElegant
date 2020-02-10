#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   string_io.py
@Time    :   2020/02/10 15:25:39
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

from io import StringIO
from io import BytesIO
import os

f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
print(f.getvalue())

fb = BytesIO()
fb.write('中文'.encode('utf-8'))
print(fb.getvalue())

print(os.name)
# windows 上不提供
# print(os.uname())

print(os.path.abspath('.'))
print(os.path.split('/Users/michael/testdir/file.txt'))

