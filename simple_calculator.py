a = int(input("first number: "))
b = int(input("second number: "))
operation = input("Choose the operation (+, -, *, /, //, %): ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
elif operation == "//":
    print(a // b)
elif operation == "%":
    print(a % b)
else:
    print("invalid operation")
