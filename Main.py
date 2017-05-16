from Deck import Deck

class Main():
	def __init__(self):
		self.Deck = Deck()
		self.Deck.Shuffle()
		
	def Player(self):
		Pcard = self.Deck.TakeFromTop()
		return Pcard
		#Pcard.displayCard()

	def CPU(self):
		Ccard = self.Deck.TakeFromBottom()
		#self.Deck.DisplayDeck()
		Ccard.displayCard()
		return Ccard

def Compare(Player, CPU):
	if(Player.checkSuit() > CPU.checkSuit()):
		return 0
	elif(Player.checkSuit() == CPU.checkSuit()):
		if(Player.checkRank() > CPU.checkRank()):
			return 0
		if(Player.checkRank() == CPU.checkRank()):
			return 2
		else: return 1
	else: return 1



gane = Main()
CPUS = 10000
PlayerS = 10000
PlayerN = raw_input("What is your name?")
print("Hello " + PlayerN)

while(CPUS > 0 or PlayerS > 0):
	start = raw_input("Press s to begin the game")
	if(start == "s"):
		print("Current " + PlayerN + " money: " + str(PlayerS) + "Current CPU money: " + str(CPUS))
		Bet = int(input("How much do you want to bet?"))
		P =gane.Player()
		C = gane.CPU()
		GS = raw_input("Press G to go, S to giveup")
		if(GS == "G")	:
			if(Compare(P,C) == 1):
				print("CPU wins!")
				CPUS += Bet
				PlayerS -= Bet
			if(Compare(P,C) == 0):
				print(PlayerN + "wins!")
				CPUS -= Bet
				PlayerS += Bet
			elif(Compare(P,C) == 2):
				print("Draw!")

		if(GS == 'S'):
			Bet/=2
			if(Compare(P,C) == 1):
				print("CPU wins!")
				CPUS += Bet
				PlayerS -= Bet
			if(Compare(P,C) == 0):
				print(PlayerN+ " wins!")
				CPUS -= Bet
				PlayerS += Bet
			elif(Compare(P,C) == 2):
				print("Draw!")
	if(start != "s"):
		break
	if(CPUS <= 0 or PlayerS <= 0):
		break
if(CPUS > PlayerS):
	print(PlayerN+ "lost all the money You lost!")
if(CPUS < PlayerS):
	print("CPU lost all the money You Win!")
if(CPUS == PlayerS):
	print("Draw!")