#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sub_process.py
@Time    :   2020/02/11 11:36:20
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import subprocess








print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,
stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\n python.org \n exit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)


# print('nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)


