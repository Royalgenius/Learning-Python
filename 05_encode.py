#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#cmd运行
ord('A')
ord('中')
chr(66)
chr(25991)
'\u4e2d\u6587'
'中文'
'ABC'.encode('ascii')
'中文'.encode('utf-8')
'中文'.encode('ascii')
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
len('ABC')
len('中文')
len(b'ABC')
len(b'\xe4\xb8\xad\xe6\x96\x87')
len('中文'.encode('utf-8'))
print('中文测试正常')
'Hello, %s' % 'world'
'Hi, %s, you have $%d.' % ('Michael', 1000000)
'%2d-%02d' % (3, 1)
'%.2f' % 3.1415926
'Age: %s. Gender: %s' % (25, True)
'growth rate: %d %%' % 7