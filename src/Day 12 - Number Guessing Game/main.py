import art
import random

#TODO: Create a number guessing game in easy and hard mode. Easy gives 10 attemps and Hard gives 5 attempts. The user should be able to guess a number between 1 and 100.
# The program should give feedback if the guess is too high or too low. If the user guesses the number correctly, they win. If they run out of attempts, they lose.
#Additional features I'm including myself, only easy or hard prompts allowerd from users, or loops. Attempting the same number is expempted from losing a round.
# And I will also print the correct number if the user loses. I will also not accept a guess below 1 and above 100

print(f"{art.logo}\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)
passedAway = []
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip.lower()
while difficulty not in ['easy', 'hard']:
    difficulty = input("Try again dumbass. Type 'easy' or 'hard': ").strip.lower()

attempts = 10 if difficulty == 'easy' else 5
while attempts > 0:
    print(f"You have {attempts} attempt(s) remaining to guess the number.")
    while True:
        try:
            guess = int(input("Make a guess: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100. Not your penis's size or the number of men your mom slept with.")
        continue
    elif guess in passedAway:
        print("You've already guessed that number. Try again.")
        continue
    passedAway.append(guess)
    if guess == number:
        print(f"Congratulations! You guessed the number {number} correctly!")
        break
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1
else:
    print(f"Sorry, you've run out of attempts. The correct number was {number}.")