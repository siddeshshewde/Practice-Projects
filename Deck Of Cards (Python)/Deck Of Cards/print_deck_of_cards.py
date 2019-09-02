

def show_deck():
	#Defining deck of cards
	pips = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
	suits = ["C","S","D","H"]
	
	#Printing all the deck possibilities
	for i in pips:
		for j in suits:
		    cards = []
		    cards.append(i+j)
		    print (cards)

show_deck()