# -*- coding: utf-8 -*-

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解。

#0提示：计算平方根可以调用math.sqrt()函数：

import math

def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')
	elif not isinstance(b, (int, float)):
		raise TypeError('bad operand type')
	elif not isinstance(c, (int, float)):
		raise TypeError('bad operand type')
	elif b == 0:
		raise TypeError('bad operand type')
	elif b*b -4*a*c <0:
		return('sorry, no answer')
	elif b*b -4*a*c ==0:
		x1=-b/(2*a)
		return(x1)
	elif b*b -4*a*c >0:
		x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
		x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
		return(x1,x2)
print(quadratic(1,3,2))
