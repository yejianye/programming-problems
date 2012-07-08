def exp(n):
	(a,b) = (coff[n-1], 1)
	for i in range(n-2, -1, -1):
		(a,b) = (coff[i] * a + b, a)
	return (a,b)

coff = [2]
for i in range(1,100):
	coff.extend([1, 2*i, 1])
print coff

a,b =  exp(100)
print sum([int(x) for x in str(a)])

