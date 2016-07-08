"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def validate(input_list):
    output_list = []
    try:
        output_variable = int(input_list[1])
        output_list.append(output_variable)
    except:
        return False
    if len(input_list) == 3:
        try:
            output_variable = int(input_list[2])
            output_list.append(output_variable)
        except:
            return False        
    return output_list

input_string = None

while input_string != "q":
    input_string = raw_input(">> ").lower().rstrip()
    tokens = input_string.split(" ")

    if tokens[0] == "q":
        print "Goodbye!"
    elif validate(tokens) == False:
        print "Invalid input. Try again."

    else:
        valid_input = validate(tokens)
        if tokens[0] == "+":
            print add(valid_input[0],valid_input[1])
        elif tokens[0] == "-":
            print subtract(valid_input[0],valid_input[1])
        elif tokens[0] == "*":
            print multiply(valid_input[0], valid_input[1])
        elif tokens[0] == "/": 
            if valid_input[1] == 0:
                print "Cannot divide by zero."
            else:
                print divide(valid_input[0], valid_input[1])
        elif tokens[0] == "square":
            print square(valid_input[0])
        elif tokens[0] == "cube":
            print cube(valid_input[0])
        elif tokens[0] == "pow":
            print power(valid_input[0], valid_input[1])
        elif tokens[0] == "mod":
            print mod(valid_input[0], valid_input[1])
        else:
            print "Not a valid argument."





# print validate([1, "abc", "abc"])

# validation function:
# check :
#     q OR
#     len = 2 or 3
#     if len 2 = index 2 can be converted to int, if True convert to int and continue
#     if len 3 = indices 2 and 3 can be converted to int, if True convert to int and continue
#     else False = invalid input


# Your code goes here
