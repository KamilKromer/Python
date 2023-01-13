klucz = ['+', '*', '/']
klucz_INDEX_ERROR = ['+', '*', '/', ')']


def parse_string(val):
    recursion_index: int = 0
    double_mode = False
    minus_multiply = False
    # double_parsed_ind = []
    parsed = []
    double_parse = ""
    cur_ind: int = -1
    for index in range(len(val)):
        letter = val[index]
        if letter == ' ' and not double_mode:
            print('Minus multiply set to 0!')
            minus_multiply = False
            cur_ind = -1
            continue

        # Start bracket parse
        elif letter == ')':
            if recursion_index > 0: #if recursion index is greater than 0, skip
                print('Recursion index: ' + str(recursion_index))
                recursion_index -= 1
                double_parse += letter
                print(f"Double parse is: {double_parse}")
                continue

            elif double_mode:
                double_mode == False
                parsed.append(parse_string(double_parse))
                double_parse = ""
                continue
            elif not double_mode:
                print('Syntax error!')
                return False

        elif double_mode:
            if letter == '(':
                print('Recursion in double mode!')
                recursion_index += 1
                
            double_parse += letter
            print(f"Double parse is: {double_parse}")
            continue

        elif letter == '(':  # Enable double parse
            double_mode = True
            print("Double mode enabled")
            continue
        #End bracket parse
        elif letter == '-':
            if minus_multiply:
                print("Syntax error!")
                return False
            
            print('minus multiply set to true!')
            minus_multiply = True
            parsed.append('-')
            print(parsed)
            print(parsed[-1])
            cur_ind = len(parsed) - 1
            print('Cur index is ' + str(cur_ind))

        elif letter.isnumeric():
            if minus_multiply:
                print("Numeric called, minus is online")
                minus_multiply = False
            if cur_ind > -1:
                parsed[cur_ind] += letter
                continue
            else:
                parsed.append(letter)
                cur_ind = len(parsed) - 1
                continue
        
        elif letter in klucz: #This letter is in klucz
            cur_ind = -1
            if (letter in klucz_INDEX_ERROR and len(parsed) <= 0) or ( (len(parsed) > 0) and (parsed[-1] in klucz) ): #Second statements checks if there isnt a situation  like this: 3 */ 2
                print('Syntax error!')
                return False
            else:
                parsed.append(letter)
                continue
        else:
            print('Syntax error!')
            return False
    parsed = convert_to_float(parsed)
    return parsed


def check_operation_order(parsed: list):
    sequence = []
    for operation in parsed:
        if type(operation) == list:
            sequence.append(parsed.index(operation)) #Make a list in a list
    for operation in parsed:
        if operation == '^' or operation == 'root':
            sequence.append(parsed.index(operation))
    for operation in parsed:
        if operation == '*' or operation == '/':
            sequence.append(parsed.index(operation)) #everything else -> go from left to right
    return sequence


def convert_to_float(val: list):
    for index in range(len(val)):
        if val[index].isnumeric():
            val[index] = float(val[index])  # Change to float, always
    return val

