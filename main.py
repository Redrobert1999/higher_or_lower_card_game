import random


class CardDeck:

    deck = []
    discard = []
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    faces = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

    # List goes from [Top, ... , Bottom]
    for suit in suits:
        for face in faces:
            deck.append([face + " of " + suit])

    def top_card(self):
        top_card = self.deck[0]
        self.discard.append(self.deck.pop(0))
        return top_card

    def shuffle(self):
        for i in range(100):
            shuffled = self.deck.pop(random.randrange(0, 51, 1))
            self.deck.append(shuffled)

    def merge(self):
        index = 0
        for card in range(len(self.discard)):
            self.deck.insert(index, self.discard.pop(0))
            index += 1


def main_menu():
    print("Welcome to project_one! My first proper Python project using stuff I learned.")
    print("Here is just a basic game of Higher or Lower.")
    main_screen_select = input("Type \"Start\" to start or \"Instructions\" for how to play the game.")
    if main_screen_select.upper() == "INSTRUCTIONS":
        print("""Welcome to Higher or Lower! The rules are simple:
                 A card will appear on screen and you have to guess whether the next
                 card will be of higher or lower value.
                 All numbered cards will be their respective value with Ace's having
                 a value of one, Jack's a value of 11, Queen's a value of twelve and
                 King's a value of 13.
                 Any draws will count as a loss.
                 The game ends when you guess incorrectly, get a draw or run out of 
                 cards in the deck (a standard 52 card deck).
                 Good luck!""")
        back = input("Type \"Back\" to return to main menu")
        if back.upper() == "BACK":
            main_menu()
    elif main_screen_select.upper() == "START":
        higher_or_lower()

def card_value(card):
    value = 0
    if "Ace" in card: value = 1
    elif "Two" in card: value = 2
    elif "Three" in card: value = 3
    elif "Four" in card: value = 4
    elif "Five" in card: value = 5
    elif "Six" in card: value = 6
    elif "Seven" in card: value = 7
    elif "Eight" in card: value = 8
    elif "Nine" in card: value = 9
    elif "Ten" in card: value = 10
    elif "Jack" in card: value = 11
    elif "Queen" in card: value = 12
    elif "King" in card: value = 13
    return value


deck_one = CardDeck



def higher_or_lower():
    deck_one.merge(deck_one)
    deck_one.shuffle(deck_one)
    count = 0
    current_card = deck_one.top_card(deck_one)
    next_card = deck_one.top_card(deck_one)
    current_card_value = card_value(current_card)
    next_card_value = card_value(next_card)
    while deck_one.deck != []:
        print("Score = ", count)
        high_or_low = input(current_card)
        if (current_card_value < next_card_value and high_or_low.upper() == "HIGHER") or (current_card_value > next_card_value and high_or_low.upper() == "LOWER"):
            print("Correct!")
            current_card = next_card
            next_card = deck_one.top_card
            current_card_value = card_value(current_card)
            next_card_value = card_value(next_card)
            count += 1
        else:
            print(next_card)
            break

    print("Game Over! Score = ", count)
    game_over = input("Type \"Back\" to go back to the main menu or \"Retry\" for another game")
    if game_over.upper() == "BACK":
        main_menu()
    elif game_over.upper() == "Retry":
        higher_or_lower()


main_menu()
