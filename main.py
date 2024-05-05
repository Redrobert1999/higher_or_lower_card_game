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

    def merge(self):
        for card in range(len(self.discard)):
            self.deck.append(self.discard.pop(0))


deck_one = CardDeck()

print("deck = " + str(deck_one.deck))
deck_one.shuffle()
print("shuffled deck = " + str(deck_one.deck))
deck_one.top_card()
deck_one.top_card()
deck_one.top_card()
deck_one.top_card()
print("deck = " + str(deck_one.deck) + "\n discard = " + str(deck_one.discard))
deck_one.merge()
print("deck = " + str(deck_one.deck) + "\n discard = " + str(deck_one.discard))




