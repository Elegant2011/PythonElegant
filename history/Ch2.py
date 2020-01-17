#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/22 20:38
# @Author  : Elegant
# @Site    : 
# @File    : Ch2.py
# @Software: PyCharm Community Edition

greeting = 'Hello'
print(' indexing:')
print('>>greeting[0] :'+greeting[0])
print('>>greeting[1] :'+greeting[1])
print('>>greeting[-1] :'+greeting[-1])

# 分片
numbers =[1,2,3,4,5,6,7,8,9,10]
print(numbers[1:6:2])
print(numbers[-3:-1])
print(numbers[:3:-1])

# 乘法
print(' python love you '
      '; '*10)
print([42]*5)

prmmissions = 'locomotive'
print(  'ti' in prmmissions)
print(  'ciq' in prmmissions)