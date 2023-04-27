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
guessed_list = []

while len(guessed_list) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_list)} / 50 guessed. Guess the states", prompt="Which states in here??").title()

    if user_guess == "Exit":
        homework = [item for item in states_list if item not in guessed_list]
        break

    if user_guess in states_list:
        guessed_list.append(user_guess)
        state = data[data.state == user_guess]
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.goto(int(state.x), int(state.y))
        state_turtle.write(user_guess, font=font)

pd.DataFrame(homework).to_csv("a.csv")