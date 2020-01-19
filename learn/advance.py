#from collections import Iterable

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

#trim('hello  ')
trim('       hello  pass ')

# 2、 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

#print (isinstance('abc', Iterable) ) # str是否可迭代

def findMinAndMax(L):
     if len(L)==0:
         return (None, None)
     min,max =L[0],L[0]
     for k in L:
      if k >= max:
        max = k
      if k <=min:
        min = k
     return (min,max)


if findMinAndMax([]) != (None, None):
    print('测试失败! 1')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败! 2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败! 3')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败! 4')
else:
    print('测试成功! 5')


print (list(range(1,11)))
print([x * x for x in range(1,11)])

print([x * x for x in range(1,11)if x %2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])