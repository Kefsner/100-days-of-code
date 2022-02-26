from art import logo
import replit

print(logo)

again = True

dictionary = {}

while again:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n$")
    while not bid.isdigit():
        print("Please type a valid bid, your noob.")
        bid = input("What is your bid?\n$")
    dictionary[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    right_type_check = True
    while right_type_check:
        if more_bidders == "yes":
            replit.clear()
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

replit.clear()

print(f"The winner is {winner} with a bid of ${winner_bid}")
