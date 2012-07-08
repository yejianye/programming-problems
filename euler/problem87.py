from prime import primeTable

MAX = 50000000

square_bound = MAX ** 0.5
cubic_bound = MAX ** (1.0 / 3)
quad_bound = MAX ** 0.25

square = [x for x in primeTable if x < square_bound]
cubic = [x for x in primeTable if x < cubic_bound]
quad = [x for x in primeTable if x < quad_bound]

square = [x*x for x in square]
cubic = [x*x*x for x in cubic]
quad = [x*x*x*x for x in quad]

hash = {}
for i in quad:
	for j in cubic:
		if i + j >= MAX:
			break
		for k in square:
			if i + j + k >= MAX:
				break
			hash[i+j+k] = 1
print len(hash.keys())
