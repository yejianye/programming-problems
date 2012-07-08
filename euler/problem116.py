#! /usr/bin/python
def func(n):
	r = [0] * (n+1)
	r[0] = r[1] = 1
	for i in range(2, n+1):
		if i == 2:
			r[i] = r[i-2] + r[i-1]
		elif i == 3:
			r[i] = r[i-3] + r[i-2] + r[i-1]
		else:
			r[i] = r[i-4] + r[i-3] + r[i-2] + r[i-1]

	return r[n]

print func(50)
