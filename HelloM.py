#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/14 13:59
# @Author  : Aries
# @Site    : 
# @File    : HelloM.py
# @Software: PyCharm Community Edition

import reportlab
# data = [
#     # year month predicted high low
#     (2007,12, 4.8 ,    5.0,4.7)
#     (2008, 1, 4.3,     4.4, 4.2)
# ]

from reportlab.graphics.shapes import Drawing,String

from reportlab.graphics import renderPDF

d = Drawing (100,100)

s= String (50,50,'Hello World !',textAnchor ='middle')

d.add(s)

renderPDF.drawToFile(d,'hello.pdf','A simple pdf file')