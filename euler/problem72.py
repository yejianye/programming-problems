from prime import *
factors = bulkPrimeFactor(1000000)
#factors = bulkPrimeFactor(8)

total = 0
for n,f in enumerate(factors):
	if f:
		phi = n
		for i in f:
			phi = (phi / i) * (i-1)
		total += phi

print total
