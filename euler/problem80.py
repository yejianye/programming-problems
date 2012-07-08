import math
def test(n, dec):
	first = int(math.sqrt(n))
	result = first
	remain = n - result * result
	i = 1
	while i < dec:
		remain *= 100
		next = 0
		for y in range(1,11):
			if 20 * y * result + y * y > remain:
				next = y - 1
				break
		remain = remain - (20 * next * result + next * next) 
		result = result * 10 + next
		i+=1
	return sum([int(x) for x in str(result)])

total = 0
for n in range(100):
	if int(math.sqrt(n)) == math.sqrt(n):
		print n
	else:
		total += test(n,100)
print total
