#!/usr/bin/python

def reverseNum(n):
	return int(''.join(reversed(str(n))))

def isPalin(n):
	return n == reverseNum(n)

def isLychrel(n):
	print 'n = ',n
	for iter in range(50):
		print n, '+', reverseNum(n)
		n = n + reverseNum(n)
		if isPalin(n):
			print 'Not a Lychrel'
			return False
	print 'It is a Lychrel'
	return True

total = 0
for i in range(1, 10000):
	 isLychrel(i)
print total

