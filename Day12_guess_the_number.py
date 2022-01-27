from Day12_guess_the_number_art import logo
import random

print(logo)

print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. Can you guess it?")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
play = True


if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

chosen_number = random.randint(1, 100)

def check(guess):
  if guess > chosen_number:
    print("Too high.")
  elif guess < chosen_number:
    print("Too low")
  return attempts - 1

while play:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == chosen_number:
    print(f"You got it! The answer was {chosen_number}.")
    play = False
  else:
    attempts = check(guess)
    if attempts == 0:
      print("You've run out of guesses. You lose...")
      play = False