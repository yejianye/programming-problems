factorMap = {}
def getPrimeFactor(n):
	orig = n
	while True:
		for i in range(math.sqrt(n)):
			if n % i 
	factorMap[orig] = factorSet
	return factorSet

def phi(n):
	factorSet = getPrimeFactor(n)
	result = n
	for i in factorSet:
		result = (result / i) * (i - 1)
	return result

total = 10
n = [0] + [i for i in range(total-1)]

for i in range(2, total):
	for j in range(2*i,total,i):
		n[j] -= 1

print [(i+1, j) for i,j in enumerate(n[1:])]

