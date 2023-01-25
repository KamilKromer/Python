key = ['+', '*', '/', 'R', '^'] #Recognized keywords
key_INDEX_ERROR = ['+', '*', '/', ')'] #Keywords that cannot exist as a first element, for example *8 + 10
minus_multiply_operations = ['(', 'R'] #Operations that can be multiplied by -1, for example -(9) = -1 * (9), only one symbol equations!
self_multiply = ['bracket'] #Operations that can multiply without usage of the "*" symbol, for example (9)(8) = (9) * (8)
self_multiply_disable_after = ['+', '-', '/', '*', 'R', '^'] #Operations that cannot have a multiply sign after them, for example R * (10 - 9)
# This is checked in the second object, not the first!
high_order = ['^', 'R'] #Objects that have a higher priority than multiplying

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
        #print(f'Current letter is: {letter}')
        #print(f"Parsed is: {parsed}")
        #print(double_mode)
        if letter == ' ' and not double_mode:
            #print('Minus multiply set to false!')
            minus_multiply = False
            cur_ind = -1
            continue
        elif (letter in minus_multiply_operations and minus_multiply) or len(parsed) == 1 and parsed[0] == '-': # checking for a situation where the minus is in front of the whole equation, like - 9 * 8
            #print("Replacing minus for multiplication!")
            parsed.pop() # Remove the minus
            parsed.append("-1")
            parsed.append("*")
            cur_ind = -1 #Minus activates cur_ind, so when we remove it we need to disable it for numeric numbers not to append to this index
            minus_multiply = False #This too.
        # Start bracket parse
        if letter == ')':
            if recursion_index > 0: #if recursion index is greater than 0, skip
                print(f'Recursion index: {recursion_index}')
                recursion_index -= 1
                double_parse += letter
                print(f"Double parse is: {double_parse}")
                continue

            elif double_mode:
                double_mode = False
                parsed_string = parse_string(double_parse)
                if not parsed_string: #Check for potential errors
                    return False
                
                print(f"Parsing for double parse: {double_parse}")
                print(f"Parsed double parse: {parsed_string}")
                parsed.append(parsed_string)
                double_parse = ""
                continue
            elif not double_mode:
                print('\033[91mSyntax Error!\033[0m')
                return False

        if double_mode:
            if letter == '(':
                #print('Recursion in double mode!')
                recursion_index += 1
                
            double_parse += letter
            print(f"Double parse is: {double_parse}")
            continue

        if letter == '(':  # Enable double parse
            double_mode = True
            #print("Double mode enabled")
            continue
        #End bracket parse
        elif letter == '-':
            if minus_multiply or (len(parsed) > 0 and parsed[-1] in key): # Situation where there are two minuses together, or an example situation 10 * - 2
                print("\033[91mSyntax Error!\033[0m")
                return False
            #print('minus multiply set to true!')
            minus_multiply = True
            parsed.append('-')
            #print(parsed)
            #print(parsed[-1])
            cur_ind = len(parsed) - 1
            #print('Cur index is ' + str(cur_ind))

        elif CheckNumeric(letter):
            #print("After checknumeric parse " + str(parsed))
            if minus_multiply:
                #print("Numeric called, minus is online")
                minus_multiply = False
            if cur_ind > -1:
                parsed[cur_ind] += letter
                continue
            else:
                parsed.append(letter)
                cur_ind = len(parsed) - 1
                #print(cur_ind)
                continue
        elif letter in key or letter == '-': #This letter is in key, we can't add minus to the key directly
            cur_ind = -1
            if (letter in key_INDEX_ERROR and len(parsed) <= 0) or ( (len(parsed) > 0) and (parsed[-1] in key or parsed[-1] == '-') ): #Second statements checks if there isnt a situation  like this: 3 */ 2
                print('\033[91mSyntax Error!\033[0m')
                return False
            else:
                parsed.append(letter)
                continue
        else:
            print(f'\033[91mSyntax Error, {letter} is not defined!\033[0m')
            return False
    if double_mode:
        print('\033[91mSyntax Error, no closing bracket!\033[0m')
        return False
    if not CheckForErrors(parsed):
        return False
    parsed = InsertMultiplication(parsed)
    parsed = convert_to_float(parsed)
    return parsed


def check_operation_order(parsed: list):
    sequence = []
    for operation_ind in range(len(parsed)):
        operation = parsed[operation_ind]
        if type(operation) == list:
            sequence.append(operation_ind)

    for operation_ind in range(len(parsed)):
        operation = parsed[operation_ind]
        if operation in high_order:
            sequence.append(operation_ind)

    for operation_ind in range(len(parsed)):
        operation = parsed[operation_ind]
        if operation == '*' or operation == '/':
            sequence.append(operation_ind) #everything else -> go from left to right

    for operation_ind in range(len(parsed)):
        operation = parsed[operation_ind]
        if operation == '+' or operation == '-':
            sequence.append(operation_ind)

    return sequence


def convert_to_float(val: list):
    for index in range(len(val)):
        if type(val[index]) == list:
            continue
        if CheckNumeric(val[index]):
            val[index] = float(val[index])  # Change to float, always
    return val

def CheckNumeric(val):
    try:
        float(val)
        return True
    except:
        return False

def CheckForErrors(val: list):
    last_letter_was_numeric = False
    for letter in val:
        if CheckNumeric(letter) and last_letter_was_numeric:
            print("\033[91mSyntax Error!\033[0m")
            return False
        last_letter_was_numeric = CheckNumeric(letter)
    return True

def InsertMultiplication(val: list): #Inserts multiplication, for example (9)(8) = (9) * (8)
    for index in range(len(val)):
        letter = val[index]
        if (type(letter) == list or letter in self_multiply) and index >= 1 and not val[index - 1] in self_multiply_disable_after:
            val.insert(index, '*')
    return val