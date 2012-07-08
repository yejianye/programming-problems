n = 1
table = {'0':1}
for i in range(1,10):
	n *= i
	table[str(i)] = n

max = 1000000
result = [0] * max
for i in range(1, max):
	if i % 10000 == 0:
		print i
	linked = []
	n = i
	while n not in linked:
		linked.append(n)
		n = sum([table[x] for x in str(n)])
	result[i] = len(linked)

print len([x for x in result if x == 60])
