import turtle
from turtle import Turtle
import random

turtle.colormode(255)

joe = Turtle()
joe.shape("turtle")
joe.color("purple")


def randomcolor():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# for _ in range(4):
#     joe.forward(100)
#     joe.right(90)

# for _ in range(15):
#     joe.forward(10)
#     joe.up()
#     joe.forward(10)
#     joe.down()

# for m in range(3, 11):
#     joe.pencolor(randomcolor())
#     for n in range(m):
#         joe.forward(100)
#         joe.right(360 / m)

# joe.hideturtle()
# joe.pensize(5)
# joe.speed(0)
# for n in range(200):
#     joe.pencolor(randomcolor())
#     joe.setheading(random.choice([0, 90, 180, 270]))
#     joe.forward(25)


joe.hideturtle()
joe.speed(0)

# for n in range(0, 361, 2):
#     joe.setheading(n)
#     joe.circle(100)
#     joe.pencolor(randomcolor())

for n in range(0, 361):
    joe.setheading(n)
    joe.forward(2)
    joe.pencolor(randomcolor())

screen = turtle.Screen()
screen.exitonclick()
