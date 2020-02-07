#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
#     print('try...')
#     r = 10 / 2
#     print('result: ',r)
# except ZeroDivisionError  as e:
#     print('excpt:',e)
# finally:
#     print('finally...')
# print('END')

import logging


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

foo('0')
# main()
# print('--------------')
# print('END')