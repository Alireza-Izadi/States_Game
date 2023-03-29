from turtle import Turtle, Screen
from state import State
import pandas

data = pandas.read_csv("./50_states.csv")

turtle = Turtle()
screen = Screen()
screen.addshape("blank_states_img.gif")
screen.title("50 States Game")
image = "blank_states_img.gif"
turtle.shape(image)

#states list
states_list = data.state.to_list()

game_is_on = True
correct_guess = 0
while game_is_on:
    answer_state = screen.textinput(f"{correct_guess}/50:Guess the state", "What's another state's name?").title()
    
    if correct_guess == 50:
        game_is_on = False
    
    if answer_state == "Exit":
        break
    
    if answer_state in states_list:
        correct_guess += 1
        state = State(answer_state)
        st = data[data.state == answer_state]
        state.text(answer_state, st.x.item(), st.y.item())
        states_list.remove(answer_state)
        
#show you the states you missed in csv file!   
missed_states = {
    "Missed States": states_list
    }
state_learn = pandas.DataFrame(missed_states)
state_learn.to_csv("states_missed.csv")


screen.exitonclick()
