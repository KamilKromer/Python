from string_parser import *
from math import sqrt

default_message = [
    "\033[95mEquation calculator, list of operations:",
    "+    -> add",
    "-    -> substract",
    "*    -> multiply",
    "/    -> divide",
    "^    -> raise to the power",
    "R    -> square root",
    "Brackets ( ) are supported, order of operations applies!",
    "Remember to insert spaces properly when using the - (minus) symbol, - 9 * 8 is not equal (codewise) to -9 * 8\033[0m"
]

message_lock = False


def main():
    global message_lock
    if not message_lock:
        message_lock = True
        for message in default_message:
            print(message)

    raw = input('\033[92mWaiting for input: \033[0m')

    parsed = parse_string(raw)
    if parsed == False:
        main()
    print(f"\033[93mMAIN: Parsed string: {parsed}\033[0m")

    sequence = check_operation_order(parsed)
    print(f"\033[93mMAIN: Sequence is: {sequence}\033[0m")

    result = 0
    try:
        result = calculate(parsed, sequence)
    except:
        print("An error occured while calculating!")
    print(f"\033[92mResult: {result}\033[0m")

    main()




#Calculation
def calculate(parsed: list, operations: list):
    #print(parsed)
    for o_index in range(len(operations)):
        #print("Operation check!")
        if type(parsed[operations[o_index]]) == list:
            #print("Operation checked true")
            sequence = check_operation_order(parsed[operations[o_index]])
            #print(sequence)
            calculate(parsed[operations[o_index]], sequence) # Calculate expressions in brackets, self recurring code

        for letter_ind in range(len(parsed)):
                    letter = parsed[letter_ind]
                    if type(letter) == list:
                        not_fill_obj = 0
                        number = 0
                        for am in parsed[letter_ind]:
                            if am == '&':
                                continue
                            else:
                                not_fill_obj += 1
                                number = am
                        if not_fill_obj == 1: #Theres only one object, which means that this has been calculated and waits to be collapsed into parsed
                            parsed[letter_ind] = number


         #For this operations we take left and right number, then store them and replace them with & character
         #-1 is left, 1 is right (Direction)

        index = operations[o_index]
        #print("Current operation index is " + str(index) + " in parsed equal to ")
        #print(parsed)
        if parsed[index] == '*':
            left = Get_num(parsed, -1, index)
            right = Get_num(parsed, 1, index)
            #print("Left: " + str(left))
            #print("Right: " + str(right))
            parsed[index] = left * right
            #print("Parsed od index: " + str(parsed[index]))
            #print(parsed)

        if parsed[index] == '/':
            left = Get_num(parsed, -1, index)
            right = Get_num(parsed, 1, index)

            parsed[index] = left / right

        if parsed[index] == '+':
            left = Get_num(parsed, -1, index)
            right = Get_num(parsed, 1, index)

            parsed[index] = left + right
        if parsed[index] == '-':
            left = Get_num(parsed, -1, index)
            right = Get_num(parsed, 1, index)
            #print("Left: " + str(left))
            #print("Right: " + str(right))
            parsed[index] = left - right
            #print("Parsed od index: " + str(parsed[index]))
        if parsed[index] == '^':
            left = Get_num(parsed, -1, index)
            right = Get_num(parsed, 1, index)

            parsed[index] = left ** right
        if parsed[index] == 'R':
            right = Get_num(parsed, 1, index)

            parsed[index] = sqrt(right)

    count = 0
    num = 0
    for am in parsed:
        if am == '&':
            continue
        else:
            count += 1
            num = am
    #print(f"Count is {count}")
    if count == 1: #Theres only one object, which means that this has been calculated and waits to be collapsed into final result
        parsed = num #End, return the result
    return parsed


def Get_num(parsed: list, direction: int, start: int):
    if parsed[start + 1 * direction] == '&':
        return Get_num(parsed, direction, start + 1 * direction)
    
    val = parsed[start + 1 * direction]
    parsed[start + 1 * direction] = '&'
    return val


main()
