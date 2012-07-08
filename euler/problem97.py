hash = {}
num = 1
hash[1] = 0
threshold = 10000000000
for i in range(1,7830457 + 1):
	num = (2 * num) % threshold

print (num * 28433 + 1) % threshold

