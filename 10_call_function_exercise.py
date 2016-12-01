# -*- coding: utf-8 -*-

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：

# -*- coding: utf-8 -*-

n1 = 255
n2 = 1000
a1 = str(hex(n1))
a2 = str(hex(n2))
print( '%s %s ' % (a1, a2) )

a = input("Please input an int number: ")
b = str(hex(a))
print('%d transfer into hexadecimal equals : %s' % (a,b))