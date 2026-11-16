import random

full_deck = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h','6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c', '8d', '8h', '9s', '9c', '9d', '9h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h']

game = True
tens = 4
jacks = 4
queens = 4
kings = 4
dealer_aces = 0
player_aces = 0
dealertotal = 0
playertotal = 0

def drawcard():
    global card
    card = random.choice(full_deck)
    full_deck.remove(card)
    return card

def carddrawslate():
    global kings, queens, tens, jacks
    drawcard()
    # rank
    if card[0] == '1':
        cardw = 'Ace of '
    elif card[0] == '0':
        undecided = True
        while undecided == True:
            c = random.randrange(1, 5, 1)
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
                queens = queens - 1
                undecided = False
            elif c == 4 and kings >= 1:
                cardw = 'King of '
                kings = kings - 1
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
    global value
    global ace
    if card[0] == '1':
        value = 1
    elif card[0] == '0':
        value = 10
    else:
        value = int(card[0])
    return cardw

def bjdraw(x):
    carddrawslate()
    global dealertotal, playertotal, dealer_aces, player_aces, value
    if x == 'd':
        dealertotal += value
    elif x == 'p':
        playertotal += value
    if x == 'd' and value == 1:
        dealer_aces += 1
    elif x == 'p' and value == 1:
        player_aces += 1
    if dealer_aces >= 1 and dealertotal <= 11:
        dealertotal += 10 * dealer_aces
    return carddrawslate()

print(bjdraw('d'), bjdraw('d'), dealertotal, dealer_aces)


# hit/stand

hs1inputneeded = True

while hs1inputneeded == True:
    print("Do you hit or stand?")
    h_s = input("(hit/stand): ").lower()
    if h_s == "hit" or h_s == "stand":
        hs1inputneeded = False
    else:
        print("Unknown input; please try again.")

print("")