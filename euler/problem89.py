import re
# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
# Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.

romanMap = dict(
 I = 1,
 IV = 4,
 V = 5,
 IX = 9,
 X = 10,
 XL = 40,
 L = 50,
 XC = 90,
 C = 100,
 CD = 400,
 D = 500,
 CM = 900,
 M = 1000,
)

romanPri = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def romanToInt(s):
	l = len(s)
	i = 0
	total = 0
	while i < l:
		if s[i:i+2] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
			total += romanMap[s[i:i+2]]
			i += 2
		else:
			total += romanMap[s[i]]
			i += 1
	return total

def intToRoman(num):
	roman = '' 
	i = 0
	while num > 0:
		unit = romanMap[romanPri[i]]
		x = num / unit
		if x > 0:
			num -= x * unit
			roman += x * romanPri[i]
		i += 1
	#sec pass opt
	#roman = re.sub('MDCCC','CMCM', roman)
	#roman = re.sub('CLXXX', 'XCXC', roman)
	#roman = re.sub('XVIII', 'IXIX', roman)
	return roman

f = open('roman.txt', 'r')
of = open('new_roman.txt', 'w')
lines = f.readlines()
f.close()
origCnt = 0
count = 0
result = []
for i in lines:
	origin = i.strip()
	origCnt += len(origin)
	val = romanToInt(origin)
	roman = intToRoman(val)
	assert romanToInt(roman) == val, 'failed to match'
	result.append(roman)
	#print origin, val, roman, len(origin), '->', len(roman)
	print origin, val 
	print roman + '\n'
	count += len(roman)
of.writelines(result)
of.close()
print origCnt, count, origCnt - count
