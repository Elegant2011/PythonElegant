#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hash.py
@Time    :   2020/02/13 11:27:29
@Author  :   elegantm
@Version :   1.0
@Desc    :   None
'''

# here put the import lib
import hashlib
import hmac

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    hash = db.get(user)
    if hash == None: 
      return False
    if hash == calc_md5(password):
      return True
    return False

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

message = b'Hello, world!'
key = b'secret'

print(key,message)

h = hmac.new(key,message,digestmod='sha1')
print(h.hexdigest())

h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())