#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Bubble.py
@Time    :   2020/02/07 12:20:22
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import random

def bubble_sort(seq :list) -> list:
    n = len(seq)

    for i in range(n):
        for j in range(0,n-1-i):
            if seq[j]>seq[j+1]:
                print(seq[j],'<-->',seq[j+1])
                seq[j],seq[j+1]=seq[j+1],seq[j]
                # print(seq)
        print('------ i :',i)
    return seq    



def main():
   testset = list(range(10))
   testcase = testset[:] # make a copy
   print(testcase)
   random.shuffle(testcase)
   print(testcase)
   print('begain \n')
   assert testcase != testset  # we've shuffled it
   bubble_sort(testcase)
   assert testcase == testset  # we've unshuffled it back into a copy

print('Bubble sort')
main()

