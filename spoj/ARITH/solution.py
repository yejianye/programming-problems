import sys
import re
import itertools
from pprint import pprint

re_expr = re.compile(r'([0-9]+)([*+-])([0-9]+)')
def add(n1, n2):
	if len(n1) > len(n2):
		n2 = n2.zfill(len(n1))
	else:
		n1 = n1.zfill(len(n2))
	carry = 0
	result = []
	for x, y in itertools.izip(reversed(n1), reversed(n2)):
		z = int(x) + int(y) + carry
		if z > 9:
			z, carry = z - 10, 1
		else:
			carry = 0
		result.append(z)
	if carry == 1:
		result.append(1)
	return ''.join(str(x) for x in reversed(result))

def substract(n1, n2):
	carry = 0
	result = []
	for x, y in itertools.izip(reversed(n1), reversed(n2)):
		z = int(x) - int(y) - carry
		if z < 0:
			z, carry = z + 10, 1
		else:
			carry = 0
		result.append(z)
	if carry:
		result = decrement(n1[:(len(n1) - len(n2))]) + ''.join(str(x) for x in reversed(result))
	else:
		result = n1[:(len(n1) - len(n2))] + ''.join(str(x) for x in reversed(result))
	return result.lstrip('0')

def decrement(x):
	for idx, val in enumerate(reversed(x)):
		if val > '0':
			break
	if idx == len(x) - 1 and val == '1':
		return '9' * idx
	else:
		return x[:-(idx+1)] + str(int(val) - 1) + '9' * idx

def mul(n1, n2):
	mul_pass_caches.clear()
	intermedia = [mul_pass(n1, int(x)) for x in reversed(n2)]
	return mul_sum(intermedia, len(n1)+1), [''.join(str(x) for x in reversed(one_pass)) for one_pass in intermedia]

mul_pass_caches = {}
def mul_pass(n, m):
	if not mul_pass_caches.has_key(m):
		if m == 0:
			mul_pass_caches[m] = [0] 
		else:
			carry = 0
			result = []
			for x in reversed(n):
				y = int(x) * m + carry
				carry, z = y / 10, y % 10
				result.append(z)
			if carry:
				result.append(carry)
			mul_pass_caches[m] = result 
	return mul_pass_caches[m]

def mul_sum(intermedia, max_length):
	total_length = len(intermedia) - 1 + len(intermedia[-1])
	carry = 0
	result = []
	for i in xrange(total_length):
		y = carry
		for j in xrange(max(0, i - max_length), min(i+1, len(intermedia))):
			if i - j < len(intermedia[j]):
				y += intermedia[j][i-j]
		carry = y / 10
		result.append(y % 10)
	if carry:
		result.append(carry)
	return ''.join(str(x) for x in reversed(result))

def calc(expr):
	first, op, second = re_expr.match(expr).groups()
	if op == '+':
		result = add(first, second)
		return format(first, '+' + second, result)
	elif op == '-':
		result = substract(first, second)
		return format(first, '-' + second, result)
	else:
		result, intermedia = mul(first, second)
		if len(intermedia) == 1:
			return format(first, '*' + second, result)
		else:
			return format(first, '*' + second, result, intermedia)

def format(first, second, result, intermedia=None):
	length = max(len(first), len(second), len(result))
	output = [first.rjust(length), second.rjust(length)]
	if intermedia:
		output.append(('-' * max(len(second), len(intermedia[0]))).rjust(length))
		output.extend(
			x.rjust(length-idx) for idx, x in enumerate(intermedia)
		)
		output.append(('-'*len(result)).rjust(length))
		output.append(result.rjust(length))	
	else:
		output.append(('-' * max(len(second), len(result))).rjust(length))
		output.append(result.rjust(length))	
	for l in output: print l

#print calc('325*4405')
count = int(sys.stdin.readline().strip())
for i in xrange(count):
	calc(sys.stdin.readline().strip())	
	print ''
