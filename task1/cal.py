num1 = float(input("enter the 1st num "))
num2 = float(input("enter the 2nd num "))
operation = input("coose an operation//+, -, *, /, %//: ")


if operation == '+':
    result = num1 + num2
    print(f"the result of add is: {result}")

elif operation == '-':
    result = num1 - num2
    print(f"the result of sub is: {result}")

elif operation == '*':
    result = num1 * num2
    print(f"the result of mul is: {result}")

elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"the result of div is: {result}")
    else:
        print(" div by 0 is not posi.")

elif operation == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"the result of mod is: {result}")
    else:
        print(" modulus by 0 is not posi.")

else:
    print("invalided operation please coose from //+, -, *, /, %//")
