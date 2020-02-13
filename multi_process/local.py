#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   local.py
@Time    :   2020/02/12 10:19:30
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello , %s (in %s)' % (std,threading.current_thread().name))

def process_thread(name):
    local_school.student = name 
    process_student()


t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-B')

t1.start()
t2.start()
t1.join()
t2.join()













  