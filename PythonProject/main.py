from turtle import Turtle,Screen
turtle=Turtle()
screen =Screen()

screen.title("U.S. States Game")
image = r"C:\Users\ITN\Downloads\day-25-us-states-game-start\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

import pandas as pd
data=pd.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state =screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="what's another state name?").title()
    print(answer_state)

    if answer_state=="Exit":
        missing_states= []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        df = pd.DataFrame(missing_states)
        df.to_csv("missing_states.csv",index=False)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)

screen.exitonclick()

