#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

import Day3_logo
import os

print(Day3_logo.logo)

print("Welcome to Treasure Island!\n")
print("You are at a bar drinking some nice orange juic when, suddenly, two guys enter the bar whispering something about a treasure nearby that they weren't able to find. You felt like there was some truth in their conversation and decided to give it a try.\n")
print("HOW TO PLAY -> The commands that you can input are highlighted as 'command'\n")
print("Good luck!\n")

play = input("Type 'play' to start\n")

while play == "play":
  os.system('cls')
  first_input = input("You get out of the bar and follow the main road out of the city, where you find a crossroad. You want to go 'left' or 'right'?\n")
  lower_first_input = first_input.lower()

  if first_input == "left":
    os.system('cls')
    second_input = input("You've reached a lake. There is a small house on the other side. You want to 'swim' across the river or 'look' for a boat?\n")
    lower_second_input = second_input.lower()

    if lower_second_input == "look":
      os.system('cls')
      third_input = input("By spending more timing looking, you end up finding a small boat, which you used to cross the river. You then enter the small house and see tree doors. The 'yellow', the 'blue' and the 'green'. Which one do you choose?\n")
      lower_third_input = third_input.lower()
      
      if lower_third_input == "yellow":
        print('You find the treasure! When openning, you find a note: "You are your own true treasure!"')
        play_again = input("Play again? 'yes' or 'no'?\n")
        if play_again == "yes":
          continue
        else:
          play = "don't play"
      else:
        print("There is a big hungry Lion behind that door. You should run, but you are probably dead.")
        print("Game over...")
        play_again = input("Play again? 'yes' or 'no'?\n")
        if play_again == "yes":
          continue
        else:
          play = "don't play"
    else:
      print("In the middle of the lake, you heard at least three other things entering the water. Well, it were aligators and you are probably dead by now.")
      print("Game over...")
      play_again = input("Play again? 'yes' or 'no'?\n")
      if play_again == "yes":
        continue
      else:
        play = "don't play"
  else:
    print("Well, the right road actually was dead ended. When turing back, you see yourself right in the front of a big hungry bear. There is nowhere to run and you are probably dead.")
    print("Game over...")
    play_again = input("Play again? 'yes' or 'no'?\n")
    if play_again == "yes":
      continue
    else:
      play = "don't play"
