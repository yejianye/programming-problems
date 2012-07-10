import sys

while True:
	count = int(sys.stdin.readline())
	if count == -1:
		break
	packets = [int(sys.stdin.readline()) for i in xrange(count)]
	total_candies = sum(packets)
	avg = total_candies / count
	if avg * count != total_candies:
		print -1
	else:
		print sum(x - avg for x in packets if x > avg)
