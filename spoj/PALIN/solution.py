import sys

def get_half(number):
	return number[:(len(number)+1)/2]

def expand_half(number, is_even):
	if is_even:
		return number + number[::-1]
	else:
		return number[:-1] + number[::-1]

def inc(number):
	for i in xrange(len(number) - 1, -1, -1):
		if number[i] != '9':
			break
	else:
		return '1' + '0' * len(number)
	return number[:i] + str(int(number[i])+1) + '0' * (len(number) - i - 1)

def find_next_palindrome(number):
	is_even = bool(len(number) % 2 == 0)
	half = get_half(number)
	palin = expand_half(half, is_even)
	if palin > number:
		return palin
	else:
		new_half = inc(half)
		if len(new_half) != len(half):
			is_even = not is_even
		palin = expand_half(new_half, is_even)
		return palin

count = int(sys.stdin.readline())
for i in xrange(count):
	number = sys.stdin.readline().strip()	
	print find_next_palindrome(number)
