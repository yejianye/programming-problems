import sys

permut_caches = {}
def permut(n, k):
	if not permut_caches.has_key((n,k)):
		if k == 0:
			return 1
		elif k > n * (n - 1) / 2:
			return 0
		result = 0
		for i in xrange(min(n, k+1)):
			result += permut(n - 1, k - i)
		permut_caches[(n,k)] = result
	return permut_caches[(n,k)]

count = int(sys.stdin.readline())
for i in xrange(count):
	n, k = sys.stdin.readline().strip().split(' ')
	print permut(int(n), int(k))
