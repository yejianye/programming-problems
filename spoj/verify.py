#!/usr/bin/env python
import subprocess

test = open('test.txt', 'r')
expected = open('expected.txt', 'r')
p = subprocess.Popen(['/usr/bin/python', 'solution.py'], stdin=test, stdout=subprocess.PIPE)
lineno = 1
while True:
	exp = expected.readline().strip()
	act = p.stdout.readline().strip()
	if exp != act:
		print 'Mismatch on line %d, expected %s, got %s' % (lineno, exp, act)
		break
	if not act:
		print 'SUCCESS'
		break
	lineno += 1
