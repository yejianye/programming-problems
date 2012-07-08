#import Queue
#def perm(n):
#	queue = Queue.Queue()
#	queue.put([n])
#	count = 0
#	while not queue.empty():
#		comb = queue.get()
#		#print comb
#		count += 1
#		start = len(comb) >= 2 and comb[-2] or 1
#		end = comb[-1]/2
#		for i in range(start, end+1):
#			queue.put(comb[0:-1] + [i, comb[-1] - i])
#	return count
#
#print perm(20)

def perm():
	f = {}
	threshold = 1000000
	for x in range(2, threshold):
		for y in range(1, x/2+1):
			z = x-y
			f[(y, z)] = 1 + sum([f[(i, z - i)] for i in range(y, z/2+1)]) 
		count = sum([f[(i,x - i)] for i in range(1, x/2+1)]) + 1
		print x, count
		if count % 1000000 == 0:
			return

print perm()
