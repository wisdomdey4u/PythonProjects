#file not found

try:
    file = open("a_data.txt")
    a_dictionary = {"Key": "Value"}
    print(a_dictionary["weret"])
except FileNotFoundError:
    file = open("a_data.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"That key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that i made up")

height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

if height > 3:
    raise ValueError("Human height must be less than or equal to 3 meters")

bmi = weight / height ** 2
print(bmi)
