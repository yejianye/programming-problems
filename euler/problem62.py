hash = {}
n = 100
threshold = 10 ** len(str(n*n*n))
while True:
	print n
	x = n * n * n
	digs = list(str(x))
	digs.sort()
	key = ''.join(digs)
	if hash.has_key(key):
		hash[key].append(n)
	else:
		hash[key] = [n]
	if x >= threshold:
		match = [i for i in hash.values() if len(i) == 5]
		if match:
			print match
			break
		# clear hash
		hash = {}
		threshold = 10 ** len(str(x))
	n += 1

