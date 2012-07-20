import sys
import math

def area(fence):
	r = fence / math.pi
	return r * r * math.pi / 2.0

while True:
	fence = sys.stdin.readline().strip()
	if fence == '0':
		break
	print '%.2f' % area(float(fence))
