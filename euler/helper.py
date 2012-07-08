plusStep = 10
plusThreshold = 10 ** plusStep

def bigMul(a, b):
	pass

def bigPlus(a, b):
	(first, second) = len(a) > len(b) and (a,b) or (b,a)
	first = [int(first[(x > plusStep and x - plusStep or 0) : x]) for x in range(len(first), 0,  -plusStep)]
	second = [int(second[(x > plusStep and x - plusStep or 0) : x]) for x in range(len(second), 0, -plusStep)]
	second.extend([0 for x in range(len(first) - len(second))])
	result = []
	carry = 0
	fmt = '%0'+str(plusStep)+'d'
	for i in range(len(first)):
		temp = first[i] + second[i] + carry
		if temp > plusThreshold:
			temp -= plusThreshold
			carry = 1
		else:
			carry = 0
		result.append(fmt % temp)
	if carry:
		result.append('1')
	result.reverse()
	result[0] = str(int(result[0]))
	return ''.join(result)
