hash = {}
INC = 1
DEC = 2
TBD = 3
BOUNCY = 4
for i in range(1, 10):
	hash[i] = INC 

for i in range(10, 100):
	if i/10 > i % 10:
		hash[i] = DEC
	elif i/10 < i % 10:
		hash[i] = INC
	else:
		hash[i] = TBD

i = 99
bouncy = 0
ratio = 0.99
while bouncy < i * ratio:
	i += 1
	k = i / 10
	sec = k % 10
	last = i % 10
	type = hash.get(k, BOUNCY)
	if type == INC and last >= sec:
		hash[i] = INC
	elif type == DEC and last <= sec:
		hash[i] = DEC
	elif type == TBD:
		if last == sec:
			hash[i] = TBD
		elif last > sec:
			hash[i] = INC
		else:
			hash[i] = DEC
	else:
		bouncy += 1
print i
