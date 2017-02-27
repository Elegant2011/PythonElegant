#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/18 19:03
# @Author  : Aries
# @Site    : 
# @File    : Sunspots_roto.py.py
# @Software: PyCharm Community Edition

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

data = [
    # year Month Predicted  High   Low
    (  2007, 8 ,  113.2  ,114.2 ,112.2 ),
    (  2007 ,9  ,  112.8 , 115.8,109.8 ),
    ( 2007 , 10 ,  111.0  , 116.0 ,106.0 ),
    ( 2007 , 11  ,  109.8  , 116.8 ,102.8 ),
    ( 2007  ,12  ,  107.3  , 115.3 ,99.3 ),
    ( 2008 , 1  ,   105.2   , 114.2 ,96.2 ),
]

drawing = Drawing(200,150)

pred = [row[2]-40 for row in data]
high = [row[3]-40 for row in data]
low  =  [row[4]-40 for row in data]
times =[200*((row[0]+row[1]/12.0)- 2007) -110 for row in data]

drawing.add(PolyLine(list(zip(times,pred)), strokeColor = colors .blue))
drawing.add(PolyLine(list(zip(times,high)), strokeColor = colors .red))
drawing.add(PolyLine(list(zip(times,low)),  strokeColor = colors .green))
drawing.add(String(65,115,'Sunspots',fontSize = 18,fillcolor = colors.red))

renderPDF.drawToFile(drawing,'report1.pdf','Sunspots')