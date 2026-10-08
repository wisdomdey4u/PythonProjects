print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child ticket are 5$.")
    elif age  <= 18:
        bill = 7
        print ("Youth ticket are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")

    wants_photo = input("Do you want to have photo take? Type y for Yes and n for No.")
    if wants_photo == "y":
        #Add 3$ to their bill
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
