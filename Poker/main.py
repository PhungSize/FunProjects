from art import logo

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
humanDeck = []
computerDeck = []
humanTotal = 0
computerTotal = 0

userAnswer = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")

if userAnswer == 'y':
    stillPlaying = True
    playersTurn = True
    computersTurn = True
else:
    stillPlaying = False
    print("Aw too bad, later!")


def draw(deck):
    randomIndex = random.randint(0,12)
    chosenCard = cards[randomIndex]
    deck.append(chosenCard)

def addTotal(deck, total):
    total = 0
    for currentCard in deck:
        total += currentCard
    return(total)

# def changeAces(deck):
#     print(f"Changing aces in deck: {deck}")
#     for card in deck:
#         print(f"current card: {card}")
#         if card == 11:
#             print("Card is an Ace!")
#             card = 1
#             print(f"Deck is now: {deck}")
#     return(deck)

def compare(total1, deck1, total2, deck2):
    if total1 > 21:
        print(f"\n\nYou busted! Computer wins!\n  Your current cards are: {deck1} and the total is {total1}\n  Computer's cards are {deck2} with its total as {total2}")
        
    if total1 < 22:
        if total2 > 21:
            print(f"\n\nYou beat computer!\n  Your current cards are: {deck1} and the total is {total1}\n  Computer's cards are {deck2} with its total as {total2}")
        elif total1 > total2:
            print(f"\n\nYou beat computer!\n  Your current cards are: {deck1} and the total is {total1}\n  Computer's cards are {deck2} with its total as {total2}")
        else:
            print(f"\n\nYou lost to computer!\n  Your current cards are: {deck1} and the total is {total1}\n  Computer's cards are {deck2} with its total as {total2}")

while stillPlaying == True:
    draw(humanDeck)
    draw(humanDeck)
    draw(computerDeck)
    draw(computerDeck)
    humanTotal = addTotal(humanDeck, humanTotal)
    computerTotal = addTotal(computerDeck, computerTotal)
    print(logo)
    print(f"  Your current cards are: {humanDeck} and the total is {humanTotal}\n  Computer's first card is {computerDeck[0]}")
    
    while playersTurn == True:
        userAnswer = input("Do you still want to draw? y/n ")
        if userAnswer == 'y':
            draw(humanDeck)
            humanTotal = addTotal(humanDeck, humanTotal)
            print(f"  \nYour current cards are: {humanDeck} and the total is {humanTotal}\n  Computer's first card is {computerDeck[0]}")
            # if humanTotal > 21:
            #     changeAces(humanDeck)
            if humanTotal > 21:
                playersTurn = False
        if userAnswer == 'n':
            playersTurn = False

    while computersTurn == True:
        while computerTotal <= 15:
            draw(computerDeck)
            computerTotal = addTotal(computerDeck, computerTotal)
            if computerTotal >= 21:
                computersTurn = False
        computersTurn = False
    
    compare(humanTotal, humanDeck, computerTotal, computerDeck)  
    
    if playersTurn == False:
        userAnswer = input("\nWould you like to play a new game? y/n ")
        if userAnswer == 'y':
            playersTurn = True
            computersTurn = True
            humanDeck = []
            computerDeck = []
            print("\n\n\n\n\n\n\n")
        if userAnswer == 'n':
            print("Thanks for playing! Goodbye!")
            stillPlaying = False