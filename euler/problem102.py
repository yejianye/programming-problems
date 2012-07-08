def isContainOrigin(x1, y1, x2, y2, x3, y3):
	vertex = [(x1, y1), (x2, y2), (x3, y3)]
	param = [ x1 == x2 and 'special' or  (y1 - y2) * 1.0 / (x1 - x2), 
			  x1 == x3 and 'special' or (y1 - y3) * 1.0 / (x1 - x3), 
			  x2 == x3 and 'special' or (y2 - y3) * 1.0 / (x2 - x3)]
	for i in range(3):
		# y = ax
		all_signs = 0
		for j in range(3):
			if param[i] == 'special':
				all_signs += vertex[j][0] < 0 and -1 or 1
			else:
				all_signs += (param[i] * vertex[j][0] - vertex[j][1]) < 0 and -1 or 1
		if all_signs == -3 or all_signs == 3:
			return False
	return True

f = open('triangles.txt', 'r')
lines = f.readlines()
count = 0
for l in lines:
	(x1,y1,x2,y2,x3,y3) = [int(x) for x in l.strip().split(',')]
	if isContainOrigin(x1,y1,x2,y2,x3,y3):
		count += 1
		print "%s , yes" % l.strip()
	else:
		print "%s , no" % l.strip()
print count
