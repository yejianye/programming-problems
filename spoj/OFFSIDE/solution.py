import sys
def offside(attackers, defenders):
	attacker_distance = min(attackers)
	defenders.sort()
	return attacker_distance < defenders[1]

while True:
	if sys.stdin.readline().strip() == '0 0':
		break
	attackers = map(int, sys.stdin.readline().strip().split(' '))
	defenders = map(int, sys.stdin.readline().strip().split(' '))
	if offside(attackers, defenders):
		print 'Y'
	else:
		print 'N'
