import sys

def fix(case):
	comps = case.split(' ')
	first = comps[0]
	second = comps[2]
	result = comps[4]
	if first.find('machula') >= 0:
		first = str(int(result) - int(second))
	elif second.find('machula') >= 0:
		second = str(int(result) - int(first))
	else:
		result = str(int(first) + int(second))
	return '%s + %s = %s' % (first, second, result)

lines = sys.stdin.readlines()
cases = [x.strip() for x in lines[1:] if x.strip()]
for c in cases:
	print fix(c)
