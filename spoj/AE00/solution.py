import sys
import math

def rects(n):
	m = int(math.sqrt(n))
	count = 0
	for i in xrange(1, m+1):
		count += int(n/i) - i + 1
	return count

n = int(sys.stdin.readline())
print rects(n)
