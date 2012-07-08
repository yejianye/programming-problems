import math
def getNext(n, b, c):
	root = int(math.sqrt(n))
	y = (n - c*c) / b
	x = (root + c) / y 
	z = - (c - x*y)
	return (x, y, z)

def seq(n):
	first = int(math.sqrt(n))
	if n - first * first == 0.0:
		return 0
	(a, b, c) = (first, 1, first)
	hash = {}
	period = []
	while True:
		period.append(a)
		(a, b, c) = getNext(n, b, c)
		if hash.has_key((a,b,c)):
			break
		else:
			hash[(a,b,c)] = True
	print n, "=", period
	return len(period) - 1

count = 0
for i in range(2, 10001):
	if seq(i) % 2 == 1:
		count += 1

print count
