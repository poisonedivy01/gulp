import random

full_deck = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h','6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c', '8d', '8h', '9s', '9c', '9d', '9h', 'as', 'ac', 'ad', 'ah', 'as', 'ac', 'ad', 'ah', 'as', 'ac', 'ad', 'ah']

def drawcard():
    
    card = random.choice(full_deck)
    full_deck.remove(card)

    return card

def cardtranslate():
    global a
    a = drawcard()
    global b
    if str(a[0]) != 'a':
        b = int(a[0])
    elif a[0] == 'a':
        b = 10
    if a[0] == 1:
        card_w = 'Ace of '
    elif a[0] == 'a':
        card_w = 'Jack/King/Queen of '
    else:
        card_w = str(a[0]) + " of "
    if a[1] == 's':
        card_w = card_w + "Spades"
    elif a[1] == 'c':
        card_w = card_w + "Clubs"
    elif a[1] == 'h':
        card_w = card_w + "Hearts"
    elif a[1] == 'd':
        card_w = card_w + "Diamonds"
    
    return card_w

def dealerdraw():
    cardtranslate()
    global dealertotal
    dealertotal = 0 + b
    return cardtranslate()

print("The dealer drew a", dealerdraw(), "and a", dealerdraw() + ",", "totalling to", str(dealertotal) + ".")