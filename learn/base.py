#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#print('\\\t\\')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(u'中文测试')

userID = 'hello,%s' % 'test'
print(userID)

userName ='hello,{1},{0}'.format('pass',int(77.77))
print(userName)

print ("----------------")

# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# list example
names =['Michael','Bob','Tracy']
for name in names:
    print(name)
print ("---------------- \n")

L = ['Bart', 'Lisa', 'Adam']
n =0
while n <len(L):
    print(L[n])
    n = n + 1

# tuple example

classmates = ('Michael', 'Bob', 'Tracy')
print (classmates)