import sys

def decode(encoded, cols):
	rows = [encoded[i:(i+cols)] for i in xrange(0, len(encoded), cols)]
	for idx in xrange(1, len(rows), 2):
		rows[idx] = rows[idx][::-1]
	return ''.join(
		''.join(rows[row_idx][col_idx] for row_idx in xrange(len(rows))) 
		for col_idx in xrange(cols)
	)

while True:
	cols = int(sys.stdin.readline())
	if cols == 0:
		break
	encoded = sys.stdin.readline().strip()
	print decode(encoded, cols)
