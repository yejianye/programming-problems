import sys

caches = {}
def max_exchange(coins):
	if not caches.has_key(coins):
		c1 = coins/2
		c2 = coins/3 
		c3 = coins/4
		if c1 + c2 + c3 > coins:
			caches[coins] = max_exchange(c1) + max_exchange(c2) + max_exchange(c3)
		else:
			caches[coins] = coins
	return caches[coins]

for data in sys.stdin.readlines():
	print max_exchange(int(data))
