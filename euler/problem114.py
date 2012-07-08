#!/usr/bin/python

def func(m, n):
	f = [0] * (n+1)
	for i in range(m):
		f[i] = 1
	f[m] = 2
	for i in range(m+1, n+1):
		f[i] += f[i-1]
		f[i] += sum(f[0:i-m]) + 1
	return f[n]

n = 100
while True:
	if func(50, n) > 1000000:
		print n, func(50,n)
		break
	n += 1
