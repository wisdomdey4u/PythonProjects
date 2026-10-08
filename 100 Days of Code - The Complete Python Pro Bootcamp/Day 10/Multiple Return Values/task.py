def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You did not provide valid input"
    formatted_first_name = first_name.title()
    formatted_last_name = last_name.title()
    return f"Result: {formatted_first_name} {formatted_last_name}"


print(format_name(input("What ia your first name"), input("What is your last name")))
