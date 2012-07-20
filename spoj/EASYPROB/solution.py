
caches = {
	0 : '0',
}

def binary_form(num):
	if not caches.has_key(num):
		binary = [i for i in xrange(32) if (1 << i) & num]
		caches[num] = '+'.join((i==1 and '2' or '2(%s)' % binary_form(i)) for i in reversed(binary))
	return caches[num]
tests = [137, 1315, 73, 136, 255, 1384, 16385]
for t in tests:
	print '%s=%s' % (t, binary_form(t))
