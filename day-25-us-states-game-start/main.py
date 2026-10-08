import turtle
import pandas as pd
from pandas.core.ops import missing

# --- Step 0: Load the data ---
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()  # This gives you a list of state names for membership testing

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# --- A turtle dedicated to writing state names on the map ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# --- Requirement 4: the loop ---
# The game ends when the player has guessed all 50 states.
guessed_states = []   # Requirement 5

# Loop continues until all 50 states are guessed
while len(guessed_states) < 50:
    # Requirement 1: Get the user's guess and convert to Title case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    # If the user cancels or types nothing, end the game
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    # Requirement 2: If guess is a valid state and hasn't been guessed yet
    if answer_state in all_states and answer_state not in guessed_states:
        # Requirement 5: Add to guessed_states
        guessed_states.append(answer_state)
        # Get x, y for that state
        state_data = data[data.state == answer_state]
        # Requirement 3: Move pen to (x, y) and write the name
        x_coord = int(state_data.x.item())
        y_coord = int(state_data.y.item())
        pen.goto(x_coord, y_coord)
        pen.write(answer_state)
        # Requirement 6: Score updates automatically via len(guessed_states) shown in the next prompt

# states_to_learn.csv
