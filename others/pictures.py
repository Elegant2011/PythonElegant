#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pictures.py
@Time    :   2020/02/13 16:21:55
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''
# here put the import lib

from PIL import Image
import os

filepath = os.path.realpath('.')

filepath = os.path.join(filepath,'others','test.jpg')
print(filepath)

im = Image.open(filepath)

w,h = im.size
print('original image size: %sx%s' %(w,h))