import random
from matplotlib.colors import is_color_like
from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
winning_color = ""

while user_bet not in colors:
    if is_color_like(user_bet):
        colors[3] = user_bet
    else:
        user_bet = screen.textinput(title="Please type a valid color!",
                                    prompt="Which turtle will win the race? Enter a color: ")

for n in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[n].color(colors[n])
    turtles[n].penup()
    turtles[n].setpos(x=-230, y=-200 + (2 * n + 1) * 200 / len(colors))

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if is_race_on:
            turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            is_race_on = False
            print(f"The {turtle.pencolor()} turtle has won!")
            winning_color = turtle.pencolor()

if winning_color == user_bet:
    print("You've won!")
else:
    print("You lose...")

screen.exitonclick()
