# testing
from prime import isPrime, primeTable
set4 = [ 3, 7, 109, 673 ]

hash = {}

def merge(x,y):
	mergedSet = list(y)
	if x[0] in y and x[1] in y:
		return None

	for i in x:
		if i in y:
			continue
		add = True
		for j in y:
			if not isPrime(int(str(i) + str(j))) or not isPrime(int(str(j) + str(i))):
				add = False
				break
		if add: mergedSet.append(i)

	if len(mergedSet) > len(y):
		mergedSet.sort()
		mergedSet = tuple(mergedSet)
		if not hash.has_key(mergedSet):
			hash[mergedSet] = 1
			return mergedSet
	return None

def primeSet():
	i = 11
	result = []
	while True:
		if isPrime(i):
			rc = decompose(i)
			if rc:
				for x in rc:
					for y in result:
						mergedSet = merge(x,y)
						if mergedSet:
							if len(mergedSet) >= 4:
								print mergedSet
								if len(mergedSet) == 5:
									return
							result.append(mergedSet)
					result.append(x)
		i += 1 
	
def decompose(num):
	num = str(num)
	result = []
	for i in range(1,len(num)):
		if num[i] == '0':
			continue
		(x,y) = (int(num[:i]), int(num[i:]))
		if x > y:
			continue
		if isPrime(x) and isPrime(y) and isPrime(int(str(y) + str(x))):
			result.append((x,y))
	return result

print decompose(3673)
print primeSet()

