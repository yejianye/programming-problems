import sys

lookup = {}

def build_lookup():
	for i in range(10):
		lookup[(i, 0)] = i 
		for j in range(1, 32):
			lookup[(i,j)] = (lookup[(i, j-1)] * lookup[(i, j-1)]) % 10

def lastdig(base, idx):
	base = base % 10
	bits = [i for i in range(32) if (1 << i) & idx]
	result = 1
	for i in bits:
		result = (result * lookup[(base, i)]) % 10
	return result

build_lookup()
data = sys.stdin.readlines()
for i in xrange(1, len(data)):
	base, idx = map(int, data[i].split(' '))
	print lastdig(base, idx)
