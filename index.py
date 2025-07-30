# Ask for numbers
number_1 = (input("Enter the first number: "))
number_2 = (input("Enter the second number: "))

# Ask for the mathematical operation
operation = input("Choose a mathematical operation (+, -, *, /): ")

# Perform only the selected operation and print the result
if operation == "+":
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
elif operation == "-":
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
elif operation == "*":
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
elif operation == "/":
    if number_2 != 0:
        print(f"{number_1} / {number_2} = {number_1 / number_2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")
