import sys
import re
import itertools
from pprint import pprint

re_expr = re.compile(r'([0-9]+)([*+-])([0-9]+)')
def add(n1, n2):
	return str(long(n1) + long(n2))

def substract(n1, n2):
	return str(long(n1) - long(n2))

def mul(n1, n2):
	n1_int = long(n1)
	n2_int = long(n2)
	intermedia = [n1_int * int(x) for x in reversed(n2)]
	return str(n1_int * n2_int), map(str, intermedia)

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
