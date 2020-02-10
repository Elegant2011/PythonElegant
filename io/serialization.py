#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   serialization.py
@Time    :   2020/02/10 17:24:26
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib

import pickle

# d = dict(name='Bob',age=20,score=88)
# print(pickle.dumps(d))

# f =open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

f =open('dump.txt','rb')
d =pickle.load(f)
f.close()
print(d)




