# Create a Python program that simulates a basic calculator.
# It should repeatedly ask the user for two numbers and an operator (+, -, *, /)
# and perform the corresponding operation using if/elif statements.
# Use a while loop to allow the user to perform multiple calculations until they choose to exit


while True:
    operator = input("Enter operator (+, -, *, /) or 'q' to exit: ")
    if operator == 'q':
        print('Calculation ended!')
        break
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    if operator == '+':
        print(num1 + num2)
    if operator == '-':
        print(num1 - num2)
    if operator == '*':
        print(num1 * num2)
    if operator == '/':
        print(num1 / num2)




