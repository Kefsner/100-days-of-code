import random
from ASCII_art import stages, logo, you_lose, you_win
from words import word_list
import replit

print(logo)

input("Hit enter to start!\n")

replit.clear()

game_is_finished = False
lives = len(stages) - 1
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
guessed_letters = []
for n in range(word_length):
    display += "_"

while not game_is_finished:
    print(chosen_word)
    if guessed_letters:
        print(f"Letters that you've already guessed: {guessed_letters}")

    print(stages[lives] + "\n" + " ".join(display) + "\n")
    guess = input("Guess a letter: ").lower()
    replit.clear()

    if len(guess) > 1:
        print("Please type only one letter.")
        guess = ""
    if guess in guessed_letters:
        print(f"You've already guessed {guess}.")
    else:
        guessed_letters += guess

    for n in range(word_length):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose...")
            print(you_lose)
            input("Hit enter to exit.")

    if "_" not in display:
        game_is_finished = True
        print("You win!")
        print(you_win)
        input("Hit enter to exit.")
