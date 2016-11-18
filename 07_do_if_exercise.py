# -*- coding: utf-8 -*-

weight = input('Please enter your weight(kg):')
height = input('Please enter your height(m):')
h= float(height)
w= float(weight)
bmi = w/h/h
print(bmi)
if bmi<18.5:
	print('Your BMI is %.2f, your are too slender.' %bmi)
elif bmi>=18.5 and bmi<25:
	print('Your BMI is %.2f, your are normal weight.' %bmi)
elif bmi>=25 and bmi<28:
	print('Your BMI is %.2f, your are over weight.' %bmi)
elif bmi>=28 and bmi<32:
	print('Your BMI is %.2f, your are obese.' %bmi)
elif bmi>=32:
	print('Your BMI is %.2f, your are too heavy.' %bmi)

