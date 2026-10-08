import art

def add(n1, n2):
    return n1 + n2

def substraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substraction,
    "*": multiplication,
    "/": division,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number: "))

    while should_accumulate:
        for symbol in operations:
           print(symbol)
        operation_symbol = input("Pick an operator")
        num2 = float(input("What is the next number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculator: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()