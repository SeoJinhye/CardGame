from Deck import Deck


def Player1(firsthalf):
	print("-----Player 1-----")
	firsthalf.DisplayDeck()

def CPU(secondhalf):
	startingDeck.Cut()
	print("------CPU------")
	secondhalf.DisplayDeck()

startingDeck = Deck()
startingDeck.Shuffle()
firsthalf,secondhalf = startingDeck.Cut()
Player1(firsthalf)
CPU(secondhalf)

