import math

while True:
    operator = input("What mathematical operator do you want to do? (+, -, *, /, **, sqrt, %) ")
    if operator == ".":
        break

    if operator == "sqrt":
        try:
            input1 = float(input("Which number would you like to find the square root of? "))
        except ValueError:
            print("Inputs must be numbers.")
            continue
    else:
        try:
            input1 = float(input("Enter the first number: "))
            input2 = float(input("Enter the second number: "))
        except ValueError:
            print("Inputs must be numbers.")
            continue
    digits = int(input("How many digits would you like to round to? (must be an int) "))

    try:
        if operator=="+":
            print(input1," + ",input2," = ",round(input1+input2, digits))
        elif operator == "-":
            print(input1," - ",input2," = ",round(input1-input2, digits))
        elif operator == "*":
            print(input1," * ",input2," = ",round(input1*input2, digits))
        elif operator=="/":
            print(input1," / ",input2," = ",round(input1/input2, digits))
        elif operator=="**":
            print(input1," ** ",input2," = ",round(input1**input2, digits))
        elif operator=="sqrt":
            print("√",input1," = ",round(math.sqrt(input1), digits))
        elif operator=="%":
            print(input1," % ",input2," = ",round(input1%input2, digits))
        else:
            print("You put in an invalid operator.")
    except ZeroDivisionError:
        print("You can't divide by zero.")
