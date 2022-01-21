import random
import Day4_ASCII_art

should_continue = True

while should_continue == True:
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

  if user_choice == 0:
    print(Day4_ASCII_art.rock)
  elif user_choice == 1:
    print(Day4_ASCII_art.paper)
  elif user_choice == 2:
    print(Day4_ASCII_art.scissors)

  computer_choice = random.randint(0, 2)

  print("Computer chose: ")

  if computer_choice == 0:
    print(Day4_ASCII_art.rock)
  elif computer_choice == 1:
    print(Day4_ASCII_art.paper)
  elif computer_choice == 2:
    print(Day4_ASCII_art.scissors)

  if computer_choice == user_choice:
    print("It is a draw!")
  elif computer_choice == 0:
    if user_choice == 1:
      print("You win!")
    else:
      print("You lose.")
  elif computer_choice == 1:
    if user_choice == 0:
      print("You lose.")
    else:
      print("You win!")
  elif computer_choice == 2:
    if user_choice == 0:
      print("You Win!")
    else:
      print("You lose.")
  play_again = input("Want to play again? Type 'y' for yes and 'n' for no.\n")
  if play_again == "y":
    continue
  elif play_again == "n":
    print("Good bye!")
    should_continue = False