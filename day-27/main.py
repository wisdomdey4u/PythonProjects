from tkinter import *

def butten_click():
    print("I got clicked")
    new_text = imput.get()
    my_label.config(text=new_text)

windows = Tk()
windows.title("My First GUI Program")
windows.minsize(500, 300)
windows.config(padx=100, pady=200)

#Label
my_label = Label(text="I am a label", font=("Arial", 18))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=30)

#Butten
butten = Button(text="Click Me", command=butten_click)
butten.grid(row=1, column=1)

#New Butten
new_butten = Button(text="New Butten")
new_butten.grid(row=2, column=0)

#Entry
imput = Entry(width=10)
print(imput.get())
imput.grid(row=3, column=2)








windows.mainloop()