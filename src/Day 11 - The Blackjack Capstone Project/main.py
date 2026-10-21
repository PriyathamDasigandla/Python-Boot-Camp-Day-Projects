import art
import random

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# TODO: Begin the loop with art. Then first line with 2 cards and my socre. Second line with computer's 
# score and first card. Then ask if they want to draw another card. If yes, add a card to their score and print the new score. 
# If no, then computer draws cards until it has 17 or more. Then compare scores and print the winner.
# End loop if we want to play again. If yes, clear the screen and start over. If no, end the game.

game = True
score = 0
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
cardValue = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def deadCard():
#     print(f"Your cards: [{random.choice(cards)}, {random.choice(cards)}]")

# def calculateScore(hand, score):
#     for card in hand:
#         score += cardValue[cards.index(card)]

while game:
    print(art.logo)
    print(f"Your cards: []")
