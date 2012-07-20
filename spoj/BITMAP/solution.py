import sys

def dist_fill(bitmap, rows, cols):
	result = [(0, -1)] * (rows * cols)
	start = bitmap.find(1)

count = int(sys.stdin.readline())
for i in xrange(count):
	rows, cols = map(int, sys.stdin.readline().strip().split(' '))
	bitmap = [0] * (rows * cols)
	for j in xrange(rows):
		bitmap[j*cols : (j+1)*cols] = map(int, sys.stdin.readline().strip())
	result = dist_fill(bitmap, rows, cols)
	print '\n'.join(
		' '.join(str(result[r * cols + c]) for c in xrange(cols))
		for r in xrange(rows)
	)
	# skip the blank line
	sys.stdin.readline()
