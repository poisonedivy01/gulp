import random

full_deck = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h','6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c', '8d', '8h', '9s', '9c', '9d', '9h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h']
global tens
global jacks
global queens
global kings
tens = 4
jacks = 4
queens = 4
kings = 4

def drawcard():
    global card
    card = random.choice(full_deck)
    full_deck.remove(card)
    return card

def cardtranslate():
    drawcard()
    # rank
    if card[0] == '1':
        cardw = 'Ace of '
    elif card[0] == '0':
        undecided = True
        while undecided == True:
            c = random.randrange(1, 4, 1)
            if c == 1 and tens >= 1:
                cardw = '10 of '
                tens = tens - 1
                undecided = False
            elif c == 2 and jacks >= 1:
                cardw = 'Jack of '
                jacks = jacks - 1
                undecided = False
            elif c == 3 and queens >= 1:
                cardw = 'Queen of '
                undecided = False
            elif c == 4 and kings >= 1:
                cardw = 'King of '
                undecided = False
    else:
        cardw = str(card[0]) + ' of '
    # suit
    if card[1] == 's':
        cardw = cardw + 'Spades'
    elif card[1] == 'c':
        cardw = cardw + 'Clubs'
    elif card[1] == 'h':
        cardw = cardw + 'Hearts'
    elif card[1] == 'd':
        cardw = cardw + 'Diamonds'
        return cardw

print(cardtranslate())
print(str(full_deck))
