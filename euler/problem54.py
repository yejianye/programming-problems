#!/usr/bin/python
#* High Card: Highest value card.
#* One Pair: Two cards of the same value.
#* Two Pairs: Two different pairs.
#* Three of a Kind: Three cards of the same value.
#* Straight: All cards are consecutive values.
#* Flush: All cards of the same suit.
#* Full House: Three of a kind and a pair.
#* Four of a Kind: Four cards of the same value.
#* Straight Flush: All cards are consecutive values of same suit.
#* Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR = 7
STRAIGHT_FLUSH = 8

RANK = ( 
'HIGH_CARD',
'ONE_PAIR',
'TWO_PAIR',
'THREE',
'STRAIGHT',
'FLUSH',
'FULL_HOUSE',
'FOUR',
'STRAIGHT_FLUSH',
)

v_map = {
	'1' : 1,
	'2' : 2,
	'3' : 3,
	'4' : 4,
	'5' : 5,
	'6' : 6,
	'7' : 7,
	'8' : 8,
	'9' : 9,
	'T' : 10,
	'J' : 11,
	'Q' : 12,
	'K' : 13,
	'A' : 14,
}

def count(value, list):
	return len([x for x in list if x == value])

def getRank(cards):
	values = [v_map[x[0]] for x in cards]
	values.sort(reverse=True)
	v_set = [{'count':count(v, values), 'val': v} for v in set(values)]
	v_set.sort(key=lambda x: (x['count'], x['val']), reverse=True)
	v_set_val = [x['val'] for x in v_set]
	suit = set([x[1] for x in cards])
	same_suit = (len(suit) == 1)
	# STRAIGHT_FLUSH
	if (len(v_set) == 5 and values[0] - values[4] == 4 and same_suit):
		return (STRAIGHT_FLUSH, values)
	# FOUR
	if (v_set[0]['count'] == 4):
		return (FOUR, v_set_val)
	# FULL_HOUSE
	if (v_set[0]['count'] == 3 and v_set[1]['count'] == 2):
		return (FULL_HOUSE, v_set_val)
	# FLUSH
	if same_suit:
		return (FLUSH, values)
	# STRAIGHT
	if (len(v_set) == 5 and values[0] - values[4] == 4):
		return (STRAIGHT, values)
	# THREE
	if v_set[0]['count'] == 3:
		return (THREE, v_set_val)
	# TWO PAIR
	if v_set[0]['count'] == 2 and v_set[1]['count'] == 2:
		return (TWO_PAIR, v_set_val)
	# ONE PAIR
	if v_set[0]['count'] == 2:
		return (ONE_PAIR, v_set_val)

	return (HIGH_CARD, values)

def winner(player1, player2):
	# if player1 win return 1
	# if player2 win return 0
	(rank1, value1) = getRank(player1)
	print 'player1:', player1, RANK[rank1], value1
	(rank2, value2) = getRank(player2)
	print 'player2:', player2, RANK[rank2], value2
	if rank1 > rank2 or (rank1 == rank2 and value1 > value2):
		print 'player1 win\n'
		return 1
	else:
		print 'player2 win\n'
		return 0

f = open('poker.txt', 'r')
lines = f.readlines()
total = 0;
for line in lines:
	line = line[:-1]
	cards = line.split(' ')
	player1 = cards[:5]
	player2 = cards[5:]
	total += winner(player1, player2)

print total
