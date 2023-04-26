import pandas as pd
import turtle

font = ('Arial', 8, 'normal')


def get_mouse_click_coor(x, y):
    print(x, y)


screen = turtle.Screen()
screen.title("U.S. States Game")

states_img = "blank_states_img.gif"
data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()

screen.addshape(states_img)
turtle.shape(states_img)

while True:
    user_guess = screen.textinput(title="Guess the states", prompt="Which states in here??")

    if user_guess in states_list:
        state = data[data.state == user_guess]
        print(state)
        state_turtle = turtle.Turtle()
        state_turtle.goto(int(state.x), int(state.y))
        state_turtle.write(user_guess, font=font)

turtle.mainloop()
