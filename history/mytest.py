#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/22 20:38
# @Author  : Elegant
# @Site    :
# @File    : mytest.py 
# @Software: PyCharm Community Edition


# words = ['thie','is','an','ex','parrot']
# for word in words:
#     print(word)32
from  math import sqrt
# for n in range(130,0,-1):
#     root =sqrt(n)
#     print(root,n)
#     if root == int(root):
#         print('sqrt max',n)
#         break

fibs = [0,1]
for i in range(10):
    fibs.append(fibs[-2]+fibs[-1])
print(fibs)

def helloname(name):
    return 'hello,'+name+'!'
print(helloname('world'))
print(helloname('Gumby'))

def  fibs(num):
    result =[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return  result
print(fibs(8))
print(fibs(10))



