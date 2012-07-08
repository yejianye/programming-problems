from prime import *
blacklist = [2,3,5,7]

threshold = 79180.0/87109

def phi(n):
	factor = getPrimeFactor(n)
	result = n
	for i in factor:
		result = (result / i) * (i - 1)  
	return result


for n in range(11, 10000000, 1):
	if n % 10000 == 0:
		print n
	skip = False
	for j in blacklist:
		if n % j == 0:
			skip = True
			break
	if skip:
		continue
	p = phi(n)
	if (p * 1.0 / n) > threshold:
		# permute
		list1 = [x for x in str(n)]
		list2 = [x for x in str(p)]
		list1.sort()
		list2.sort()
		if list1 == list2:
			print n, p
			threshold = p * 1.0 / n

