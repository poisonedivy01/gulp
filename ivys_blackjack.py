import random

game = True
full_deck = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h','6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c', '8d', '8h', '9s', '9c', '9d', '9h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h']

tens = 4
jacks = 4
queens = 4
kings = 4
dealer_aces = 0
player_aces = 0
dealertotal = 0
playertotal = 0
money = 100
bet = 0
topscore = 100

def drawcard():
    global card
    card = random.choice(full_deck)
    full_deck.remove(card)
    return card

def reset():
    global full_deck, tens, queens, jacks, kings, dealer_aces, dealertotal, player_aces, playertotal
    
    full_deck = ['1s', '1c', '1d', '1h', '2s', '2c', '2d', '2h', '3s', '3c', '3d', '3h', '4s', '4c', '4d', '4h', '5s', '5c', '5d', '5h','6s', '6c', '6d', '6h', '7s', '7c', '7d', '7h', '8s', '8c', '8d', '8h', '9s', '9c', '9d', '9h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h', '0s', '0c', '0d', '0h']
    tens = 4
    jacks = 4
    queens = 4
    kings = 4
    dealer_aces = 0
    player_aces = 0
    dealertotal = 0
    playertotal = 0

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
    drawncard = carddrawslate()
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
        dealertotal += 10
    if player_aces >= 1 and playertotal <= 11:
        playertotal += 10
    if dealertotal > 21 and dealer_aces >= 1:
        dealertotal -= 10
        dealer_aces -= 1
    if playertotal > 21 and player_aces >= 1:
        playertotal -= 10
        player_aces -= 1

    return drawncard
runs = 0
def startgame():
    global game, tens, jacks, queens, kings, dealer_aces, player_aces, dealertotal, playertotal, runs, money, topscore
    while game == True:

        tens = 4
        jacks = 4
        queens = 4
        kings = 4
        dealer_aces = 0
        player_aces = 0
        dealertotal = 0
        playertotal = 0

        if runs == 0: 
            print("Welcome to Blackjack!")
        print("")
        while True:
            bet = (input(f"How much would you like to bet? ($1 - ${money}): "))
            bet = int(bet[1:(len(bet))])
            if bet > money: 
                print(f"Bet cannot exceed ${money}.")
            elif bet == 0:
                print("Bet cannot be $0.")
            else:
                print(f"You bet: ${bet}.")
                break
        print("The dealer draws a", (bjdraw('d')), f"for a total of {dealertotal}.")
        print("")
        print("You draw a", bjdraw('p'), "and a", bjdraw('p'), "totalling", str(playertotal) + ".")
        print("")

        # hit/stand

        while True:
            print("Do you hit or stand?")
            h_s = input("(hit/stand): ").lower()
            print("")
            if h_s != "hit" and h_s != "stand" and h_s != "h" and h_s != "s":
                print("Unknown input; please try again.")
                continue

            if h_s == 'hit' or h_s == 'h':
                draw = bjdraw('p')
                if player_aces >= 1 and playertotal > 21:
                    playertotal -= 10
                    player_aces -= 1
                print("You draw a", draw, "bringing your total to", str(playertotal) + ".")
                print("")
        
            if playertotal > 21 and player_aces == 0:
                print("You busted!")
                print("")
                money -= bet
                if money > topscore: topscore = money
                print(f"You have ${money} remaining.")
                game = False
                break
            
            elif h_s == 'stand' or h_s == 's':
                while dealertotal <= 17:
                    print("The dealer draws a", bjdraw('d'), "bringing their total to", str(dealertotal) + ".")
                    print("")
                if dealertotal > 21:
                    print("The dealer busted! You win!")
                    print("")
                    money += bet
                    if money > topscore: topscore = money
                    print(f"You have ${money} remaining.")
                    game = False

                elif dealertotal > playertotal:
                    print("You lose!")
                    print("")
                    money -= bet
                    if money > topscore: topscore = money
                    print(f"You have ${money} remaining.")
                    game = False

                elif dealertotal < playertotal:
                    print("You win!")
                    print("")
                    money += bet
                    if money > topscore: topscore = money
                    print(f"You have ${money} remaining.")
                    game = False

                elif dealertotal == playertotal:
                    print("The game tied!")
                    print("")
                    print(f"You have ${money} remaining.")
                    if money > topscore: topscore = money
                    game = False

                break
# game init
startgame()
# post game end
while True and game == False:
    print(f"Your high score is ${topscore}.")
    # check if broke
    if money == 0:
        refill = input("You're broke! Do you want to get more money and keep going? (y/n): ").lower()
        if refill == "y":
            money += 100
            game = True
            runs +=1
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            startgame()
            reset()
        elif refill == "n":
            quit()
            break
        else:
            print("Unknown input, please try again.")
            print("")   
    else:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay == 'y':
            game = True
            runs += 1
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            startgame()
            reset()
        elif replay == 'n':
            quit()
            break
        else:
            print("Unknown input, please try again.")
            print("")
