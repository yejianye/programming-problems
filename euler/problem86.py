import math

count = 0
threshold = 1000000
m = 2
while count <= threshold:
	a = m
	b = 2 * m
	sa = a * a
	sb = b * b
	c = int(math.sqrt(sa + sb))
	sc = c * c
	while b > 0:
		if sa + sb == sc:
			start = min(b-1, a)
			end = (b+1) / 2
			count += start - end + 1
			sb -= 2*b - 1
			sc -= 2*c - 1
			b -= 1
			c -= 1
		elif sa + sb > sc:
			sb -= 2*b - 1
			b -= 1
		else:
			sc -= 2*c - 1
			c -= 1
	m += 1

print m-1, count
