print("\nThis is a simple two number calculator for integers.")
while True:
    num1 = input("\n\tEnter the first number: ")
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print("\nInvalid response. Please type in an integer")

while True:
    operation = input("\n\tEnter your operation: ")
    if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "**":
        break
    else:
        print("\nInvalid operation. Please try again.")

while True:
    num2 = input("\n\tEnter the second number: ")
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print("\nInvalid response. Please type in an integer")


if operation == "+":
    ans = num1+num2
elif operation == "*":
    ans = num1*num2
elif operation == "-":
    ans = num1-num2
elif operation == "/":
    ans = num1/num2
elif operation == "**":
    ans = num1**num2

print(f"\nThe answer is {ans}.")