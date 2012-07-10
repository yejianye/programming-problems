import sys
from bisect import bisect_left

hangovers = [0] * 1000

def build_lookup():
	for i in xrange(1, 1000):
		hangovers[i] = hangovers[i-1] + 1.0 / (i+1)

def find_idx(n):
	return bisect_left(hangovers, n)

build_lookup()
while True:
	n = sys.stdin.readline().strip()
	if n == '0.00':
		break
	print '%d card(s)' % find_idx(float(n))
