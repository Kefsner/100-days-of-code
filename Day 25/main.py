import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=500, width=800)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pd.read_csv('50_states.csv')

already_guessed = []
score = len(already_guessed)

game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()

    check_answer = pd.Series.isin(data['state'], [answer_state])

    if len(check_answer[check_answer]) == 0:
        pass
    else:
        if answer_state in already_guessed:
            print("That was already guessed")
        else:
            index = check_answer[check_answer].index
            state_coord_x = data.loc[index]['x'].item()
            state_coord_y = data.loc[index]['y'].item()
            writer.goto(state_coord_x, state_coord_y)
            writer.write(answer_state)
            already_guessed.append(answer_state)
            score = len(already_guessed)
            if score == 50:
                print("You win!")
                game_is_on = False

    if answer_state == "Exit":
        data_already_guessed = pd.DataFrame({'state': already_guessed})

        states_left = pd.Series.isin(data['state'], data_already_guessed['state'])
        index = states_left[states_left == False].index
        data.loc[index].to_csv("./states_left.csv", index=False)
        game_is_on = False

screen.exitonclick()
