from prime import primeTable, isPrime
def perm():
	f = {}
	threshold = 10000
	for x in range(2, threshold):
		yset = [i for i in primeTable if i < x/2+1]
		for y in yset:
			z = x - y
			f[x, y] = sum([f[z,i] for i in yset if i < z/2 + 1 and i >= y])
			if isPrime(z):
				f[x,y] += 1
		count = sum([f[x,i] for i in yset])
		print x, count
		if count > 5000:
			return

perm()
