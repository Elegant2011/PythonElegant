from collections import Iterable

L = ['Michael','Sarah','Tracy','Bob','Jack']
print (L[0:3])
print (L[:3])

#  1、切片处理

### 功能：去除字符串  首尾空格
def trim(s):
    print('len ',len(s),'before:',s)
    while s != '' and s[0]==' ':
        s = s[1:]
    while s != '' and s[-1]==' ':
        s = s[:-1]
    print('len ',len(s),'after:',s)
    return s


trim('hello  ')
trim('       hello  pass ')

# 2、 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)