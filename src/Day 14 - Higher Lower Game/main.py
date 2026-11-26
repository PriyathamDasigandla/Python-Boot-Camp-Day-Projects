import os
import random
from art import logo, vs
from game_data import data

#TODO: To create a Higher Lower game. A game that chooses random people from our game data and asks which one has a higher follower count. If the user guesses correctly, 
# they get a point and the game continues. If they guess wrong, the game ends and their score is displayed. The user should be able to continue playing until they guess wrong.
# I will additionally make it so it won't display the same person, nor will it choose someone with the same follower count.

print(logo)
intial_person = random.choice(data)
print(f"Compare A: {intial_person['name']}, {intial_person['description']} from {intial_person['country']}.")
print(vs)
while True:
    next_person = random.choice(data)
    if next_person != intial_person and next_person['follower_count'] != intial_person['follower_count']:
        break
print(f"Against B: {next_person['name']}, {next_person['description']} from {next_person['country']}.")
