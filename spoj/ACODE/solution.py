import sys

def acode(data):
	result = [1] * (len(data) + 1)
	for i in xrange(len(data) - 1, -1, -1):
		# corner cases
		if data[i] == '0':
			continue
		if i == len(data) - 1:
			continue
		# normal cases
		if data[i] >= '3':
			result[i] = result[i+1]
		elif data[i] == '2' and data[i+1] > '6':
			result[i] = result[i+1]
		elif data[i+1] == '0':
			result[i] = result[i+2]
		else:
			result[i] = result[i+1] + result[i+2]
	return result[0]

while True:
	data = sys.stdin.readline().strip()
	if data == '0':
		break
	print acode(data)
