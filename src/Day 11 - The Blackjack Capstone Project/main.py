import art
import random

# Scenario 1: A Blackjack --> "Win with a Blackjack 😎"
# Scenario 2: We bust --> "You went over. You lose 😭"
# Scenario 3: Computer busts --> "Opponent went over. You win 😁"
# Scenario 4: We draw --> "Draw 🙃"
# Scenario 5: Higher score than opponent --> "You win 😃"
# Scenario 6: Lower score than opponent --> "You lose 😤"
# Scenario 7: Computer has a Blackjack --> "You lose, opponent has Blackjack 😱"

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#single function for all Y/N prompts
def yesOrNo(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

#to calculate the score of a hand (both users and computers)
def calculateScore(hand):
    points = 0
    countAces = hand.count('A') #counting Aces in hand

    #iterate thru hand to calcualte
    for card in hand:
        points += cardValue[cards.index(card)]

    #handling Ace    
    while points > 21 and countAces > 0:
        points -= 10
        countAces -= 1

    return points


while True:
    if yesOrNo("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
        print("\033c", end="") #clears the screen
    else:
        print("Goodbye!")
        break   #end of the program
    print(art.logo)

    #resetting all variables for a new game
    myHand = []
    compHand = []
    mePlaying = True
    compPlaying = True
    weAcing = False
    weBusting = False
    theyAcing = False
    theyBusting = False

    #initializing hands and scores
    myHand.append(random.choice(cards))
    myHand.append(random.choice(cards))
    ourScore = calculateScore(myHand)
    compHand.append(random.choice(cards))
    compHand.append(random.choice(cards))
    theirScore = calculateScore(compHand)

    #Ace checkpoint
    if ourScore == 21 or theirScore == 21:
        mePlaying = False
        compPlaying = False
        weAcing = ourScore == 21
        theyAcing = theirScore == 21

    #User's hand
    while mePlaying:
        print(f"Your cards: {myHand}, current score: {ourScore}")
        print(f"Computer's first card: {compHand[0]}")
        if ourScore >= 21 or not yesOrNo("Type 'y' to get another card, type 'n' to pass: "):
            break

        myHand.append(random.choice(cards))
        ourScore = calculateScore(myHand)

    #handling over 21
    if ourScore > 21:
        weBusting = True
        compPlaying = False
    print(f"Your final hand: {myHand}, final score: {ourScore}")

    while compPlaying:
        if theirScore >= 17:
            break

        compHand.append(random.choice(cards))
        theirScore = calculateScore(compHand)

    theyBusting = theirScore > 21   #handling over 21 
    print(f"Computer's final hand: {compHand}, final score: {theirScore}")

    #Final results for all scenarios
    if weAcing and not theyAcing:
        print("Win with a Blackjack 😎")
    elif theyAcing and not weAcing:
        print("You lose, opponent has Blackjack 😱")
    elif weBusting:
        print("You went over. You lose 😭")
    elif theyBusting:
        print("Opponent went over. You win 😁")
    elif ourScore > theirScore:
        print("You win 😃")
    elif ourScore < theirScore:
        print("You lose 😤")
    else:
        print("Draw 🙃")