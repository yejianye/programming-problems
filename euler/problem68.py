def perm(n):
	result = [-1] * n
	cursor = 0
	used = [0] * n
	while True:
		if cursor == n:
			yield result
			used[result[n-1]] = 0
			cursor = n - 2
			i = n - 1
			while used[i] == 1: i -= 1
			max_unused = i
			while result[cursor] > max_unused:
				used[result[cursor]] = 0
				max_unused = result[cursor]
				cursor -= 1
				if cursor < 0:
					return
			i = result[cursor] + 1
			while used[i] == 1: i += 1
			used[result[cursor]] = 0
			result[cursor] = i
			used[i] = 1
			cursor += 1
		else:
			i = 0
			while used[i] == 1: i += 1
			result[cursor] = i
			used[i] = 1
			cursor += 1

def checkMagic(p):
	if p[0] > p[3] or p[0] > p[5] or p[0] > p[7] or p[0] > p[9]:
		return False
	if p.index(9) not in [3,5,7,9]:
		return False
	t1 = p[0] + p[1] + p[2]
	t2 = p[2] + p[3] + p[4]
	t3 = p[4] + p[5] + p[6]
	t4 = p[6] + p[7] + p[8]
	t5 = p[8] + p[9] + p[1]
	if t1 == t2 and t1 == t3 and t1 == t4 and t1 == t5:
		return True

for x in perm(10):
	if checkMagic(x):
		s = [str(i + 1) for i in x]
		print ''.join([s[0],s[1],s[2],s[3],s[2],s[4],s[5],s[4],s[6],s[7],s[6],s[8],s[9],s[8],s[1]])
