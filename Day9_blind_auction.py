from Day9_blind_auction_art import logo
import os

print(logo)

again = True

dictionary = {}

while again == True:
  name = input("What is your name?\n")
  bid = input("What is your bid?\n$")
  while not bid.isdigit():
    print("Please type a valid bid, your noob.")
    bid = input("What is your bid?\n$")
  dictionary[name] = bid
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  right_type_check = True
  while right_type_check == True:
    if more_bidders == "yes":
      os.system("cls")
      right_type_check = False
    elif more_bidders == "no":
      again = False
      right_type_check = False
    else:
      print("Please type only 'yes' or 'no.'")
      more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

list_of_bids = []
for n in dictionary:
  list_of_bids.append(int(dictionary[n]))

print(max(list_of_bids))
winner_bid = max(list_of_bids)

winner = ""
for key in dictionary:
  if dictionary[key] == str(winner_bid):
    winner = key

os.system("cls")
print(f"The winner is {winner} with a bid of ${winner_bid}")