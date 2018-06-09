#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/28 0:26
# @Author  : Elegant
# @Site    : 
# @File    : changfile.py
# @Software: PyCharm

import os
import re
from tkinter import *
from tkinter.filedialog import askdirectory
path = askdirectory()

for (path, dirs, files) in os.walk(path):
    for filename in files:
        print(filename)
        if re.search('.null',filename):
            key = filename[:-5]
            print(key)
            os.rename(path + "\\" + filename,path + "\\" + key)