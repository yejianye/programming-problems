import sys

lines = sys.stdin.readlines()
for i in xrange(2, len(lines), 4):
	g = map(int, lines[i + 1].strip().split(' '))
	m = map(int, lines[i + 2].strip().split(' '))
	if max(g) >= max(m):
		print 'Godzilla'
	else:
		print 'MechaGodzilla'
