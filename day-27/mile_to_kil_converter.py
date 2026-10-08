from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km =  round(miles * 1.689)
    kilometer_resalt_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_resalt_label = Label(text="0")
kilometer_resalt_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

calculate_butten = Button(text="Calculator", command=miles_to_km)
calculate_butten.grid(column=1, row=2)






window.mainloop()