from prime import relativePrime
upbound = 3.0/7
lowbound = 0.4 

min = (2,5)
for n in range(1000000, 7, -1):
	start = int(n * upbound)
	end = int(n* lowbound) - 1
	if start == end:
		break
	for m in range(start, end, -1):
		if relativePrime(n,m):
			tmp =  m * 1.0 / n
			if tmp > lowbound:
				min = (m, n)
				print min
				lowbound = tmp
			break
