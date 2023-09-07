import random

class Deck:
    cards = []
    count = 0

def init_deck():

    for i in range(4):
        suits = ""
            
        if i == 0:
            suits = "Hearts"
        if i == 1:
            suits = "Spades"
        if i == 2:
            suits = "Diamonds"
        if i == 3:
            suits = "Clubs"

        for x in range(0, 14):
            number = x

            if number == 0:
                number = "Ace"

            if number == 11:
                number = "Jack"
                
            if number == 12:
                number = "Queen"

            if number == 13:
                number = "King"

            Deck.cards.append(suits + "_" + str(number))               
            Deck.count = Deck.count + 1
    suffel_deck()

def suffel_deck():
    random_no = 0
    temp_deck_1 = []
    temp_deck_2 = []

    for i in range(Deck.count):
        temp_deck_2.append(Deck.cards[i])        

    for i in range(Deck.count):
        list_len = len(temp_deck_2) - 1
        random_no = random.randint(0, list_len)
        temp_deck_1.append(temp_deck_2[random_no])
        temp_deck_2.remove(temp_deck_2[random_no])
        
    for i in range(Deck.count):
        Deck.cards[i] = temp_deck_1[i]
        

init_deck()

print("the first 4 cards in the deck is:")
print(Deck.cards[0])
print(Deck.cards[1])
print(Deck.cards[2])
print(Deck.cards[3])

for i in range(4):
    spilt_str = Deck.cards[i].split("_")
    if spilt_str[1] == "Ace":
        print("congrats you got an Ace")


