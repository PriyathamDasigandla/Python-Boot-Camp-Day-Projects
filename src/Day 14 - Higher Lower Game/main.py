import random
from art import logo, vs
from game_data import data

#TODO: To create a Higher Lower game. A game that chooses random people from our game data and asks which one has a higher follower count. If the user guesses correctly, 
# they get a point and the game continues. If they guess wrong, the game ends and their score is displayed. The user should be able to continue playing until they guess wrong.
# I will additionally make it so it won't display the same person, nor will it choose someone with the same follower count.

game = True
score = 0

print(logo)
initial_person = random.choice(data)
while game:
    print(f"Compare A: {initial_person['name']}, {initial_person['description']} from {initial_person['country']}.")
    print(vs)
    while True:
        next_person = random.choice(data)
        if next_person != initial_person and next_person['follower_count'] != initial_person['follower_count']:
            break
    print(f"Against B: {next_person['name']}, {next_person['description']} from {next_person['country']}.")
    while True:
        ourChoice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
        if ourChoice in ['a', 'b']:
            break
        else:
            print("Type properly buddy.")
    if ((ourChoice == 'a' and initial_person['follower_count'] > next_person['follower_count']) or 
        (ourChoice == 'b' and next_person['follower_count'] > initial_person['follower_count'])):
        score += 1
        print(f"CORRECTO! Your current score is {score}!\n")
        initial_person = next_person
    else:
        print(f"Wrong! Your final score is {score}")
        game = False