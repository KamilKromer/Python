from string_parser import *


def result(res):
    print(f'Wynik to: {res}')


def main():
    rw = input('Wpisz działanie: ')
    parsed = parse_string(rw)#[2]
    print(parsed)
    #print((len(parsed) > 0) and (parsed[len(parsed) - 2] in klucz))
    if parsed == False:
        print('An error occured!')
        return

    sequence = check_operation_order(parsed)

    #calculate(parsed, sequence)
    print(sequence)
    main()


def calculate(parsed: list, operations: list):
    for o_index in range(len(operations)):
        if type(operations[o_index]) == list:
            sequence = check_operation_order(parsed[o_index])
            calculate(parsed[o_index], sequence) # Calculate expressions in brackets

        # For this operations we take left and right number, then store them and replace them with & character
        # -1 is left, 1 is right (Direction)

        if parsed[o_index] == '*':
            left = Get_num(parsed, -1, o_index)
            right = Get_num(parsed, 1, o_index)

            parsed[o_index] = left * right
        
        if parsed[o_index] == '/':
            left = Get_num(parsed, -1, o_index)
            right = Get_num(parsed, 1, o_index)

            parsed[o_index] = left / right

        if parsed[o_index] == '+':
            left = Get_num(parsed, -1, o_index)
            right = Get_num(parsed, 1, o_index)

            parsed[o_index] = left + right

        if parsed[o_index] == '-':
            left = Get_num(parsed, -1, o_index)
            right = Get_num(parsed, 1, o_index)

            parsed[o_index] = left - right
        
        if parsed[o_index] == '^':
            left = Get_num(parsed, -1, o_index)
            right = Get_num(parsed, 1, o_index)

            parsed[o_index] = left ** right


def Get_num(parsed: list, direction: int, start: int):
    if parsed[start + 1 * direction] == '&':
        return Get_num(parsed, direction, start + 1 * direction)
    
    val = parsed[start + 1 * direction]
    parsed[start + 1 * direction] = '&'
    return val


main()
