import art
import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# TODO: Begin the loop with art. Then first line with 2 cards and my socre. Second line with computer's 
# score and first card. Then ask if they want to draw another card. If yes, add a card to their score and print the new score. 
# If no, then computer draws cards until it has 17 or more. Then compare scores and print the winner.
# End loop if we want to play again. If yes, clear the screen and start over. If no, end the game.

# Scenario 1: A Blackjack --> "Win with a Blackjack 😎"

# Scenario 2: We bust --> "You went over. You lose 😭"

# Scenario 3: Computer busts --> "Opponent went over. You win 😁"

# Scenario 4: We draw --> "Draw 🙃"

# Scenario 5: Higher score than opponent --> "You win 😃"

# Scenario 6: Lower score than opponent --> "You lose 😤"

# Scenario 7: Computer has a Blackjack --> "You lose, opponent has Blackjack 😱"

game = True
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def yesOrNo(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def calculateScore(hand):
    points = 0

    #iterate thru hand to calcualte
    for card in hand:
        points += cardValue[cards.index(card)]

        countAces = hand.count('A')

    #handling Ace    
    while points > 21 and countAces > 0:
        points -= 10
        countAces -= 1

    return points


while True:
    if yesOrNo("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
        print("\033c", end="") #clears the screen
    else:
        print("Good job losing money. Goodbye!")
    print(art.logo)
    myHand = []
    compHand = []
    ourScore = 0
    theirScore = 0
    mePlaying = True
    compPlaying = True

    weAcing = False
    weBusting = False
    theyAcing = False
    theyBusting = False

    myHand.append(random.choice(cards))
    myHand.append(random.choice(cards))
    ourScore = calculateScore(myHand)
    compHand.append(random.choice(cards))
    compHand.append(random.choice(cards))
    theirScore = calculateScore(compHand)

    if ourScore == 21 or theirScore == 21:
        mePlaying = False
        compPlaying = False

        if ourScore == 21:
            weAcing = True
        else:
            theyAcing = True

    if theirScore == 21:
        theyAcing = True
        compPlaying = False

    while mePlaying:
        print(f"Your cards: {myHand}, current score: {ourScore}")
        print(f"Computer's first card: {compHand[0]}")
        if ourScore >= 21 or not yesOrNo("Type 'y' to get another card, type 'n' to pass: "):
            break

        myHand.append(random.choice(cards))
        ourScore = calculateScore(myHand)

    if ourScore > 21:
        weBusting = True
        compPlaying = False
    print(f"Your final hand: {myHand}, final score: {ourScore}")

    while compPlaying:
        compHand.append(random.choice(cards))
        theirScore = calculateScore(compHand)

        if theirScore >= 17:
            break

    theyBusting = theirScore > 21
    print(f"Computer's final hand: {compHand}, final score: {theirScore}")

    