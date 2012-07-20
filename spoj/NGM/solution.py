import sys

num = int(sys.stdin.readline())
if num < 10 or num % 10 == 0:
	print '2'
else:
	print '1'
	print num % 10
