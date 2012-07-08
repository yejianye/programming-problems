from prime import *
max = 12000
factors = bulkPrimeFactor(max)
factors = [set(x) for x in factors]

count = 0
for n in range(4, max+1):
	if n % 2 == 0:
		up = n / 2 - 1
	else:
		up = n / 2
	low = n / 3 + 1

	for i in range(low, up + 1):
		if not (factors[i] & factors[n]):
			count += 1

print count
