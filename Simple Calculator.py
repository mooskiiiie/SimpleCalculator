num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operator = input('What operator are you using: ')

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "//":
    print(num1 // num2)
else:
    print("operator not found")