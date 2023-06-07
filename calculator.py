"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
'' ''''repeat forever:
    read input
    tokenize input
        if the first token is "q":
            quit
        else:
            (decide which math function to call based on first token)
            if the first token is 'pow':
                  call the power function with the other two tokens

            (...etc.) '''''''''


while True:
    operator_input = input("Please enter your equation: ")
    tokens = operator_input.split (' ')
    #print(tokens)
    equation = None
    print ("Enter q to quit")

    if operator_input == "q":
        
        break

    elif tokens[0] == '+':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        equation = add(num1, num2)
        print (equation)

    elif tokens[0] == '-':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        equation = subtract(num1, num2)
        print (equation)
        
    elif tokens[0] == '*':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        equation = multiply(num1, num2)
        print (equation)

    elif tokens[0] == '/':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        equation = divide(num1, num2)
        print (equation)

    elif tokens[0] == 'square':
        num1 = float(tokens[1])
        equation = square(num1)
        print (equation)
      
    elif tokens[0] == 'cube':
        num1 = float(tokens[1])
        equation = cube(num1)
        print (equation)

    elif tokens[0] == 'pow':
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        equation = power(num1, num2)
        print (equation)