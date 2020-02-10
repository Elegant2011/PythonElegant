#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   quick.py
@Time    :   2020/02/07 18:13:02
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import random
from pprint import pprint as pp

# def quickSort(arr):
#     less = []
#     pivotList = []
#     more = []
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         print(pivot)
#         for i in arr:
#             if i < pivot:
#                 less.append(i)
#             elif i > pivot:
#                 more.append(i)
#             else:
#                 pivotList.append(i)

#     return quickSort(less)+pivotList+quickSort(more)


def quickSort(tseq):
    less = []
    pivotList = []
    more = []

    if len(tseq) <= 1:
        return tseq
    else:
        pivot = tseq[0]
        for x in tseq:
            if x > pivot:
                more.append(x)
            elif x < pivot:
                less.append(x)
            else:
                pivotList.append(x)

        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


def testList(seq):
    seq[0] = 100
    return seq


def main():
    testset = list(range(8))
    testcase = testset[:]  # make a copy
    print(testcase)
    random.shuffle(testcase)
    print(testcase)

    assert testcase != testset  # we've shuffled it
    print('begain \n')
#    arr = [10, 7, 8, 9, 1, 5]
    testcase = quickSort(testcase)

    print('after')
    print(testcase)

    assert testcase == testset  # we've unshuffled it back into a copy


print('quick sort')
main()
print('end')
