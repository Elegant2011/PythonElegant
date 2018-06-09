#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/9 20:42
# @Author  : Elegant
# @Site    : 
# @File    : pythonchar.py
# @Software: PyCharm

  # print("包含中文的str")
# precise = 3
# print("%.3s " % ("python"))

print("包含中文str")
print(ord('B'))
print(ord('中'))
print(chr(66))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(len('ABC'))
print(len('中文'.encode('utf-8')))

print('Hello,%s'%'world1')
print('Hello,{0}，成绩提升了{2:t>20f}%'.format('小明',15.123,16.30))

# s1=input()
# s2=input()
s1=72
s2=95

r=(float(s2)/float(s1)-1)*100
print('小明成绩提升百分比%.1f%%'%r)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[0][0])

height = 1.70
weight = 60

bmi = weight/(height*height)
print("BMI is %.3f"%bmi)
if bmi<18.5:
    print("less thin")
elif 18.5<=bmi<25:
    print("正常")
elif 25<=bmi<28:
    print("过重")
elif 28<=bmi<32:
    print("肥胖")
else:
    print("严重肥胖")