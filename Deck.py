import random
from Card import Card

class Deck:
    def __init__(self):
		self.value =[]
		self.validSuits=["Clubs","Spades","Hearts","Diamonds"]
		self.validRanks=["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
		for suit in self.validSuits:
			for rank in self.validRanks:
			    self.value.append(Card(rank,suit))
                self.value.append(Card("Joker","Joker"))
    
    def DisplayDeck(self):
        for c in self.value:
    	    c.displayCard()
    def Shuffle(self):
    	firstHalf,secondHalf = self.Cut()
    	self.Combine(firstHalf,secondHalf)
    	
    def TakeFromTop(self):
    	c = self.value[-1]
    	self.value.remove(c)
    	return c
    def TakeFromBottom(self):
    	#bottom is 0, top is 52
    	c = self.value[0]
    	self.value.remove(c)
    	return c

    def AddToBottom(self,cardToAdd):
    	self.value.insert(0,cardToAdd)
    def AddToTop(self,cardToAdd):
    	self.value.append(cardToAdd)

    def Cut(self):
    	first = Deck()
    	second = Deck()
    	halfway = len(self.value)/2
    	first.value = self.value[halfway:]
    	second.value=self.value[:halfway]
    	self.value = []
    	return first,second

    def Combine(self,first,second):
        ticker=True
        while(first.value != [] or second.value !=[]):
            cardToAdd = Card("temp","temp")
            if(ticker and first != []):
                cardToAdd=first.TakeFromTop()
            elif(not ticker and second != []):
                cardToAdd=second.TakeFromTop()
            self.value.insert(random.randint(0,len(self.value)),cardToAdd)
            ticker = not ticker



    def Concat(self,first,second):
    	self.value = first.value + second.value

if(__name__=="__main__"):
    startingDeck = Deck()
    print(len(startingDeck.value))
    startingDeck.DisplayDeck()
    startingDeck.Shuffle()
    print("--------------------------")
    startingDeck.DisplayDeck()


#print len(startingDeck.value)