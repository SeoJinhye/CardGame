import random
class Hand:
	def __init__(self):
		self.trade()
		self.carrds = []

	def trade(handtotrade):
		card = handtotrade.pickrandomlyhand()
		self.addtohandcard(card)

	def pickrandomlyhand():
		i = random()
		self.remove(i)
		print(i)
    	return card

	def addtohandcard(card):
		carrds.append(card)