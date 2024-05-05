class CardDeck:

    deck = []
    discard = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    faces = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    #List goes from [Top, ... , Bottom]
    for suit in suits:
        for face in faces:
            deck.append([face + " of " + suit])


    def top_card(self):
        top_card = self.deck[0]
        self.discard.append(self.deck.pop(0))
        return top_card



deck_one = CardDeck()
print("top_card =" + str(deck_one.top_card()))
print("discard = " + str(deck_one.discard))
print("deck = " + str(deck_one.deck))




