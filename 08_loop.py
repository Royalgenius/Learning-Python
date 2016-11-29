names= ['Michael','Bob','Tracy']
for name in  names:
	print(name)

#1~10和
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)

list(range(5))

#1~100和
sum =0
for x in range(101):
	sum =sum + x
print(sum)

#99以内奇数和
sum =0
n =99
while n>0:
	sum = sum + n
	n = n - 2
print(sum)

#打印1~100
n = 1
while n <= 100:
	print(n)
	n = n + 1
print('END')

#break打印1~10
n = 1
while n <= 100:
	if n > 10: # 当n = 11时，条件满足，执行break语句
		break # break语句会结束当前循环
	print(n)
	n = n + 1
print('END')

#continue打印1~10
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0: # 如果n是偶数，执行continue语句
		continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)

#死循环
while True:
	print('haha')
	#continue #死循环，未避免脚本执行问题，此处先注释掉



