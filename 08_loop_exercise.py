#请利用循环依次对list中的每个名字打印出Hello, xxx!：

# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']

#for
for name in  L:
	print('Hello,%s!' %name)
print('END')

#for
for name in ['Bart', 'Lisa', 'Adam']:
	print('Hello,%s!' %name)
print('END')

#range
l = len(L)
a = 0
for a in range(l):
	print('Hello, %s!' %L[a])
print('END')

#while
l = len(L)
a = 0
while l > a :
	print('Hello, %s!' %L[a])
	a = a + 1
print('END')