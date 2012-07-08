keylog = [
319,
680,
180,
690,
129,
620,
762,
689,
762,
318,
368,
710,
720,
710,
629,
168,
160,
689,
716,
731,
736,
729,
316,
729,
729,
710,
769,
290,
719,
680,
318,
389,
162,
289,
162,
718,
729,
319,
790,
680,
890,
362,
319,
760,
316,
729,
380,
319,
728,
716,
]

def addEdge(x, y, vertex):
	vertex[x]['out'].add(y)
	vertex[y]['in'].add(x)

vertex = dict([(x, {'in':set(), 'out':set()}) for x in range(10)])
for entry in keylog:
	seq = [int(x) for x in str(entry)]
	addEdge(seq[0], seq[1], vertex)
	addEdge(seq[1], seq[2], vertex)

# tripoly
while vertex:
	# find a number with empty IN
	next = [x for x in vertex.keys() if not vertex[x]['in']]
	assert next, 'cannot find a empty IN vertex'
	next = next[0]
	print next
	for x in vertex[next]['out']:
		vertex[x]['in'].remove(next)
	del vertex[next]
