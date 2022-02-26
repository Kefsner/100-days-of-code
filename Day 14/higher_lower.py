import art
import random
import replit

from data import data


def compare(a, b):
    if a > b:
        return 'a'
    elif a < b:
        return 'b'
    else:
        return 'equal'


game_over = False

account_a = random.choice(data)
account_b = account_a

answer = compare(account_a['follower_count'], account_b['follower_count'])

score = 0

while not game_over:
    print(art.logo)

    while answer == 'equal':
        account_b = random.choice(data)
        answer = compare(account_a['follower_count'], account_b['follower_count'])

    print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}.\n")

    print(art.vs)

    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}.\n")

    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_guess == answer:
        score += 1
        replit.clear()
        print(f"You're right! Current score: {score}.")
        account_a = account_b
        answer = compare(account_a['follower_count'], account_b['follower_count'])
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True
