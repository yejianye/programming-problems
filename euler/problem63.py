#!/usr/bin/python

total = 0
for n in range(1,30):
	threshold = 10 ** (n-1)
	k = 1
	for i in range(k,10):
		if (i ** n >= threshold):
			print i, '**', n, '=', i**n
			total += (9 - i) + 1
			k = i
			break
print total
