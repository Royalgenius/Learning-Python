#dict
name = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

d = {'Michael':95, 'Bob':75, 'Tracy':85}
d['Michael']

d['Adam'] = 67
d['Adam']

d['Jack'] = 90
d['Jack']

d['Jack'] = 88
d['Jack']

'Thomas' in d
d.get('Thomas')
d.get('Thomas', -1)

d.pop('Bob')
d

#dict的key必须是不可变对象!!

#set
s = set([1, 2, 3])
s
s = set([1, 1, 2, 2, 3, 3])
s

#add
s.add(4)
s
#remove
s.remove(4)
s

# &
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
# |
s1 | s2

#可变对象
a = ['c', 'b', 'a']
a.sort()
a
#不可变对象
a = 'abc'
a.replace('a', 'A')
a

