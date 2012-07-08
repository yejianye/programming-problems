import math
MAX = 15000
first_threshold = MAX/3
hash = {}

for a in range(2, first_threshold):
	second_threshold = int(min((a*a - 1)/2, (MAX-a)/2))
	c = int(math.sqrt(a * a * 2))
	b = a
	sa = sb = a*a
	sc = c*c
	l = a + b + c
	while b <= second_threshold:
		if l > MAX:
			break
		if sc == sa + sb:
			hash[l] = hash.has_key(l) and (hash[l] + 1) or 1
			sb += 2*b + 1
			sc += 2*c + 1
			b += 1
			c += 1
			l += 2
		elif sc > sa + sb:
			sb += 2*b + 1
			b += 1
			l += 1
		else:
			sc += 2*c + 1
			c += 1
			l += 1

#print hash[120]
print len([x for x in hash.values() if x == 1])
