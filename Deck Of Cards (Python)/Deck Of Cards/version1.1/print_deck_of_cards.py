CLUB = "\u2663"
HEART = "\u2665"
DIAMOND = "\u2666"
SPADE = "\u2660"

def show_deck():
	#Defining deck of cards
	pips = ["2","3","4","5","6","7","8","9","10","A","J","Q","K"]
	suits = [CLUB, HEART, DIAMOND, SPADE]
	
	
	for i in pips:
        for j in suits:
            #cards = []
            #cards.append(i+j)
            print (i+j, end ="\t")
        print("")

show_deck()
