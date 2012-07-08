from helper import *
def solution():
	f = ('3', '2')
	total = 0
	for i in range(500):
		f = (bigPlus(f[0], bigPlus(f[1], f[1])), bigPlus(f[0], f[1]))
		if len(f[0]) > len(f[1]):
			total += 1
		print "iter %d: %s/%s" % (i, f[0], f[1])
	print total

def temp_solution():
	f = (3, 2)
	total = 0
	for i in range(500):
		f = (f[0] + 2 * f[1], f[0]+f[1])
		if len(str(f[0])) > len(str(f[1])):
			total += 1
		print "iter %d: %d/%d" % (i, f[0], f[1])
	print total

solution()


