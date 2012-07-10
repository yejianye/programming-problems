import sys

def check_ambiguous(perm):
	for idx, val in enumerate(perm):
		if perm[val-1] != idx+1:
			print 'not ambiguous'
			return
	print 'ambiguous'

while True:
	count = int(sys.stdin.readline())
	if count == 0:
		break
	perm = map(int, sys.stdin.readline().split(' '))
	check_ambiguous(perm)
