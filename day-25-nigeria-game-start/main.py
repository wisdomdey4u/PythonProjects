import turtle
import pandas as pd

# --- Step 0: Load the data ---
data = pd.read_csv("36_states.csv")
all_states = data["state"].to_list()  # list of state names for membership testing

TOTAL = len(all_states)  # 36 states + FCT Abuja = 37

screen = turtle.Screen()
screen.title("Nigeria States Game")

# Use a blank Nigeria map image if available, otherwise draw a placeholder.
image = "nigeria_map.gif"
try:
    screen.addshape(image)
    turtle.shape(image)
except turtle.TurtleGraphicsError:
    # No image file provided: draw a simple placeholder rectangle as the map area.
    bg = turtle.Turtle()
    bg.hideturtle()
    bg.penup()
    bg.speed(0)
    bg.goto(-220, -170)
    bg.pendown()
    bg.pensize(2)
    for _ in range(2):
        bg.forward(440)
        bg.left(90)
        bg.forward(340)
        bg.left(90)
    bg.penup()
    bg.goto(0, 150)
    bg.write("Nigeria (placeholder map - blank_nigeria_img.gif for the real map)",
             align="center", font=("Arial", 10, "italic"))

# --- A turtle dedicated to writing state names on the map ---
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# --- Requirement 4: the loop ---
guessed_states = []

while len(guessed_states) < TOTAL:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/{TOTAL} States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None or answer_state == "":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x_coord = int(state_data.x.item())
        y_coord = int(state_data.y.item())
        pen.goto(x_coord, y_coord)
        pen.write(answer_state)
