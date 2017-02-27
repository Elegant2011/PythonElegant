#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/25 22:26
# @Author  : Elegant
# @Site    : 
# @File    : changeFileName.py
# @Software: PyCharm Community Edition


import os
import re
from tkinter import *
from tkinter.filedialog import askdirectory
path = askdirectory()

for (path, dirs, files) in os.walk(path):
    for filename in files:
        print(filename)
        print( re.search('\【.*?\】|\[.*?\]',filename))
        if  re.search('\【.*?\】\.|\[.*?\]\.',filename):
             key = re.sub(r'\【.*?\】\.|\[.*?\]\.','',filename)
             print(key)
             os.rename(path + "\\" + filename, path + "\\" +key)
        else:
             print("match")
            # print(filename.replace(re.search(r'\【.*?\】|\[.*?\]',filename)''))
             key = re.sub(r'\【.*?\】|\[.*?\]','',filename)
             print(key)
             os.rename(path + "\\" + filename, path + "\\" +key)
        print(os.stat(path + "\\" +key))
        print()

print('rename end')
             #os.rename(path + "\\" + filename, path + "\\" + key1)
