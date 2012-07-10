"""
	x+y start_idx
	2:  1
	3:  2 (1 -> 2)
	4:  4 = 1 + 1 + 2 (3 -> 1)
	5:  7 = 1 + 1 + 2 + 3 (1 -> 4)
	6:  11  = 1 + 1 + 2 + 3 + 4
	...
	k:  kidx = 1 + (k-1) * (k-2) / 2
    
	y > (n - 1) * (n - 2) / 2
"""

import sys
import math

basics = {
	1: "1/1",
	2: "1/2",
	3: "2/1",
}

def find_term(idx):
	if idx in basics:
		print 'TERM %d IS %s' % (idx, basics[idx])
		return
	n = int(math.sqrt(idx * 2)) + 1
	while True:
		if n * (n - 1) / 2 + 1 > idx:
			break
		n += 1
	base_idx = (n - 1) * (n -2) / 2 + 1
	direction = bool(n % 2)
	if direction:
		# from 1 -> (n-1)
		print 'TERM %d IS %d/%d' % (idx, idx - base_idx + 1, n - idx + base_idx - 1)
	else:
		# from (n-1) -> 1
		print 'TERM %d IS %d/%d' % (idx, n - 1 - (idx - base_idx), 1 + idx - base_idx)

count = int(sys.stdin.readline())
for i in xrange(count):
	find_term(int(sys.stdin.readline()))
