from prime import hcd
def rightTri(xbound, ybound):
	count = 0
	for x1 in range(xbound+1):
		for y1 in range(ybound+1):
			if x1 == 0 and y1 == 0:
				continue
			elif x1 == 0:
				count += xbound * 2
			elif y1 == 0:
				count += ybound
			else:
				h = hcd(x1, y1)	
				dx = x1 / h
				dy = y1 / h
				count += min((xbound - x1) / dy, y1 / dx) + min(x1/dy, (ybound - y1)/dx)
	return count
				
print rightTri(50,50)

