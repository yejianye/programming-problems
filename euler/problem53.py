#!/usr/bin/python

def c(n, r):
	return perm(n) / (perm(r) * perm(n-r))

def perm(x):
	result = 1
	for i in range(1, x+1):
		result *= i
	return result

print c(5,3)
total = 0
for n in range(23, 101):
	print "n = ", n
	for r in range(1, n/2):
		if c(n, r) > 1000000:
			count = (n - r) - r + 1
			print "r = ", r, "count = ", count
			total += count
			break
print total
