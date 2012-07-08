import math
from prime import primeTable
primes = [i for i in primeTable if i < 1000]
square_table = [i*i for i in range(1, 40)]
def minD(d):
	y = 1
	sqrtd = math.sqrt(d)
	while True:
		x = int(math.ceil(y * sqrtd))
		if x * x - y * y * d == 1:
			return x
		y += 1

result = []
for i in primes:
	entry = (i, minD(i))
	result.append(entry)
	print entry
result.sort(key = lambda x: x[1], reverse =  True)
print result[0]
