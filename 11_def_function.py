# -*- coding: utf-8 -*-

def my_abs(x):
	if x >=0:
		return x
	else:
		return -x

#my_abs(9)
#my_abs(-5)

def nop():
	pass

if age >=18:
	pass

def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
	
import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny
