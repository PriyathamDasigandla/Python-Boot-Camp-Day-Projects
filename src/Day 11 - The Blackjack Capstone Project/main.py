import art
import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# TODO: Begin the loop with art. Then first line with 2 cards and my socre. Second line with computer's 
# score and first card. Then ask if they want to draw another card. If yes, add a card to their score and print the new score. 
# If no, then computer draws cards until it has 17 or more. Then compare scores and print the winner.
# End loop if we want to play again. If yes, clear the screen and start over. If no, end the game.

game = True
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
herHand = []

# def dealCard(myHand):
#     myHand.append(random.choice(cards))
#     myHand.append(random.choice(cards))

#     print(f"Your cards: {myHand}, current score: {calculateScore(myHand)}")

def calculateScore(hand):
    points = 0

    #iterate thru hand to calcualte
    for card in hand:
        points += cardValue[cards.index(card)]

    #handling Ace    
    while points > 21 and 'A' in hand:
        points -= 10

    return points

# dealCard(herHand)
while True:
    weContinue = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
    if weContinue == 'y':
        print("\033c", end="") #clears the screen
    elif weContinue == 'n':
        game = False
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
    print(art.logo)
    myHand = []
    compHand = []
    myHand.append(random.choice(cards))
    myHand.append(random.choice(cards))

    print(f"Your cards: {myHand}, current score: {calculateScore(myHand)}")

    compHand.append(random.choice(cards))
    print(f"Computer's first card: {compHand}")

    while True:
        print()