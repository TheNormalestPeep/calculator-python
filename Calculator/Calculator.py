import math
pi = math.pi #allows the use of Pi for circle
print("TYPE EVERYTHING IN LOWERCASE UNLESS SAID OTHERWISE.\n")
mode = input("Are you looking for area or number?               ") #determines mode
if mode == "area":
    mode2 = input("Circle, rectangular prism, or rectangle?          ")
    if mode2 == "circle":
        r = float(input("Input radius.                                     "))
        if pi*r**2 <= 9223372036854775807 and pi*r**2 >= -9223372036854775808: #code for area of a circle
            print(f"The circle has a radius of {r}.\n(pi){r}^2 = {pi*r**2}")
        elif pi*r**2 > 9223372036854775807 or pi*r**2 < -9223372036854775808: #detects an integer overflow
            print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.") 
    elif mode2 == "cube" or mode2 == "rectangular prism" or mode2 == "prism": #code for volume of rectangular prisms
        x2 = float(input("Enter a number for X.                             "))
        y2 = float(input("Enter another number for Y.                       "))
        z = float(input("Enter another number for Z.                       "))
        if x2*y2*z <= 9223372036854775807 and x2*y2*z >= -9223372036854775808:
            print(f"Width = {x2}\nHeight = {y2}\nDepth = {z}\nArea of your rectangular prism = {x2*y2*z}")
        elif x2*y2*z > 9223372036854775807 or x2*y2*z < -9223372036854775808: #detects an integer overflow
            print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.") 
    elif mode2 == "rectangle": #transfers to Number
        print("Transferring you to the Number calculator. Use the Area function.\n")
        mode = "number" #code for the Area calculator
if mode == "number":
    x = float(input("Enter a number for X.                             "))
    y = float(input("Enter another number for Y.                       "))
    operator = input("Enter an operator. Must be lowercase.\nType HELP (case sensitive!) for keywords.         ")
    if operator == "secret code":
        print("You found my little secret.\nWell, for that, you deserve a little something.\nTry loading the code 'import antigravity' :)\nAnyways, good job!")
    while operator == "HELP":
        print("Addition        -  Adds X and Y.\n      Keywords  -  add, addition, plus\n")
        print("Subtraction     -  Subtracts X by Y.\n      Keywords  -  subtract, subtraction, minus\n")
        print("Multiplication  -  Multiplies X and Y.\n      Keywords  -  multiply, multiplication, times\n")
        print("Division        -  Divides X by Y. Shows modulus if there is one.\n                   Results in error if Y = 0.\n      Keywords  -  divide, division, over\n")
        print("Exponent        -  Multiplies X by itself Y times.\n      Keywords  -  exponent, power\n")
        print("Root            -  Finds the Yth root of X. Error if Y = 0.\n                   Doesn't allow decimals.\n      Keywords  -  root\n")
        print("Area            -  Finds area of a square or rectangle using X*Y.\n      Keywords  -  area\n")
        print("Regardless of operator, calculations\nwill not run if the result breaks the\n64-bit integer limit.\n")
        operator = input("Enter an operator. Must be lowercase.             ")
        break #help menu

    if operator == "add" or operator == "addition" or operator == "plus": #code for addition
        if y == 0:
            print(f"{x} + 0 = {x}") #identity rule
        else:
            if x+y <= 9223372036854775807 and x+y >= -9223372036854775808:
                print(f"{x} + {y} = {x+y}")
            elif x+y > 9223372036854775807 or x+y < -9223372036854775808: #detects an integer overflow
                print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")

    elif operator == "subtract" or operator == "subtraction" or operator == "minus": #code for subtraction
        if y == 0:
            print(f"{x} - 0 = {x}") #identity rule
        else:
            if x-y <= 9223372036854775807 and x-y >= -9223372036854775808:
                print(f"{x} - {y} = {x-y}")
            elif x-y > 9223372036854775807 or x-y < -9223372036854775808: #detects an integer overflow
                print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")

    elif operator == "multiply" or operator == "multiplication" or operator == "times": #code for multiplication
        if y == 0:
            print(f"{x} * 0 = 0") #rule of 0
        elif x == 0:
            print(f"0 * {y} = 0") #rule of 0
        elif y == 1:
            print(f"{x} * 1 = {x}") #identity rule
        elif y == -1:
            print(f"{x} * -1 = -{x}") #negative identity rule
        elif x == 1:
            print(f"1 * {y} = {y}")
        elif x == -1:
            print(f"-1 * {y} = -{y}")
        else:
            if x*y <= 9223372036854775807 and x*y >= -9223372036854775808:
                print(f"{x} * {y} = {x*y}")
            elif x*y > 9223372036854775807 or x*y < -9223372036854775808: #detects an integer overflow
                print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")

    elif operator == "divide" or operator == "division" or operator == "over": #code for division
        if y == 0:
            print("One does not simply divide by 0.") #ZeroDivisionError protection
        elif y == 1:
            print(f"{x} / 1 = {x}") #identity rule
        elif y == -1:
            print(f"{x} / -1 = -{x}") #negative identity rule
        elif x/y <= 9223372036854775807 and x/y >= -9223372036854775808:
            print(f"{x} / {y} = {x/y}")
            if x%y != 0:
                print("    This equation has a remainder.")
                print(f"    The remainder in {x} / {y} is {x%y}.")
        elif x/y > 9223372036854775807 or x/y < -9223372036854775808: #detects an integer overflow
            print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")

    elif operator == "exponent" or operator == "power": #code for exponents
        if y == 0:
            print(f"{x} ^ 0 = 1") #zero rule
        else:
            if x**y <= 9223372036854775807 and x**y >= -9223372036854775808:
                print(f"{x} ^ {y} = {x**y}")
            elif x**y > 9223372036854775807 or x**y < -9223372036854775807: #detects an integer overflow
                print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")

    elif operator == "root": #code for roots
        x = int(x)
        y = int(y)
        if y == 0:
            print("Y U DIVIDE BY 0?") #ZeroDivisionError protection
        elif y == 1:
            print(f"The Nth root of {x} is {x} while N = {y}.") #identity rule
        else:
            if x**(1/y) <= 9223372036854775807 and x**(1/y) >= -9223372036854775808:
                print(f"The Nth root of {x} is {x**(1/y)} while N = {y}.")
            elif x**(1/y) > 9223372036854775807 or x**(1/y) < -9223372036854775808: #detects an integer overflow
                print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")

    elif operator == "area": #code for area
        if x*y <= 9223372036854775807 and x*y >= -9223372036854775808:
            print(f"The width is {x}. The height is {y}.\n{x} * {y} = {x*y}")
        elif x*y == 0:
            print("It seems you have a line. Please try again.") #0 rule
        elif x*y > 9223372036854775807 or x*y < -9223372036854775808: #detects an integer overflow
            print("The calculation has exceeded the 64-bit integer limit.\nPlease try a smaller calculation.")
    else: #in case all if/elif statements fail
        print("That didn't work. Please reboot the app.") #code for the Number calculator
input("The program has finished. Press ENTER to close the app.") #in case the program used to run the code closes automatically when done
