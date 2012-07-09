import sys

data = sys.stdin.readlines()
count = int(data[0])
for i in xrange(count):
	men = map(int, data[i * 3 + 2].split(' '))
	women = map(int, data[i * 3 + 3].split(' '))
	men.sort()
	women.sort()
	print sum(x*y for x,y in zip(men, women))
