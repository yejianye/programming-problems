import math
target = 2000000
nearest = target

for x in range(1,38):
	f1 = (x + 1) * x / 2
	f2 = target * 1.0 / f1
	y = int(math.sqrt(2 * f2))
	near1 = f1 * (y + 1) * y / 2
	near2 = f1 * (y + 2) * (y + 1) / 2
	tmp_min = min(abs(near1 - target), abs(near2 - target))
	if tmp_min < nearest:
		nearest = tmp_min
		if tmp_min == abs(near1 - target):
			print x, y, near1
		else:
			print x, y+1, near2
