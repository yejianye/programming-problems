import sys
import re

camelcase = re.compile(r'^[a-z]+|[A-Z][a-z]*')
def transform(id):
	is_cplus = id.find('_') > -1
	is_java = not id.islower()
	if is_cplus and is_java:
		return 'Error!'
	if not is_cplus and not is_java:
		return id
	if is_cplus:
		words = id.split('_')
		if not all(words):
			return 'Error!'
		return ''.join((i > 0 and x.capitalize() or x) for i, x in enumerate(words))
	elif is_java:
		words = camelcase.findall(id)
		if not all(words) or id[0].isupper():
			return 'Error!'
		return '_'.join(x.lower() for x in words)

for l in sys.stdin.readlines():
	print transform(l.strip())

