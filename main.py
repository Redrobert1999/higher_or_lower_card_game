import random

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

    def shuffle(self):
        for i in range(100):
            shuffled = self.deck.pop(random.randrange(0,51,1))
            self.deck.append(shuffled)


deck_one = CardDeck()

print("deck = " + str(deck_one.deck))
deck_one.shuffle()
print("shuffled deck = " + str(deck_one.deck))




