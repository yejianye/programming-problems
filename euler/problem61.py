def getNumbers(low, upper, func):
	result = []
	i = 1
	while True:
		num = func(i)
		if num > upper:
			return result
		if num >= low:
			result.append(num)
		i += 1

def findChain(start, remainSet):
	result = []
	if not remainSet:
		return [[start]]
	for i in remainSet:
		matchedSet = [x for x in set[i] if x / 100 == start % 100]
		nextSet = [x for x in remainSet if x != i]
		for j in matchedSet:
			subchain = findChain(j, nextSet)
			for k in subchain:
				result.append([start] + k)
	return result

set = []
low = 1000
up = 9999
set.append(getNumbers(low, up, lambda n: n*(n+1)/2))
set.append(getNumbers(low, up, lambda n: n*n))
set.append(getNumbers(low, up, lambda n: n*(3*n-1)/2))
set.append(getNumbers(low, up, lambda n: n*(2*n-1)))
set.append(getNumbers(low, up, lambda n: n*(5*n-3)/2))
set.append(getNumbers(low, up, lambda n: n*(3*n-2)))


for x in set[5]:
	chain = findChain(x, [0,1,2,3,4])
	if chain:
		for y in chain:
			if y[5] % 100 == y[0] / 100:
				print y, sum(y)

