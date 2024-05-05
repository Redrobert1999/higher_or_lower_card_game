class CardDeck:

    deck = {}
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    faces = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    for suit in suits:
        card_value = 1
        for face in faces:
            deck.update({face + " of " + suit: card_value})
            card_value += 1


deck_one = CardDeck()
print(deck_one.deck)
