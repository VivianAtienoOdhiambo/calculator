# simple calculator program
# ask the user for the first number
num1 = float(input("Enter first number: "))
# ask the user for the second number
num2 = float(input("Enter second number: "))
# ask the user for the operation
operation = input("Enter operation (+, -, *, /): ")
# perform the operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} /{num2}={result}")
    else:
        result = ("Error: Division by zero not allowed.")
    
print("Invalid operation. Please enter +, -, *, or /.")

print("Result:", result)
