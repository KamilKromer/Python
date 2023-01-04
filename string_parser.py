klucz = ['+', '-', '*', '/']
klucz_INDEX_ERROR = ['+', '*', '/', ')']


def parse_string(val):
    double_mode = False
    double_parsed_ind = []
    parsed = []
    double_parse = ""
    cur_ind: int = -1
    for index in range(len(val)):
        letter = val[index]
        if letter == ')':
            if double_mode:
                double_mode == False
                parsed.append(double_parse)
                double_parse = ""
            elif not double_mode:
                return False, 'Syntax error', []
        elif double_mode:
            double_parse += letter
            print(f"Double parse is: {double_parse}")
        elif letter == '(':  # Enable double parse
            double_mode = True
            print("Double mode enabled")
        elif letter.isnumeric():
            if cur_ind > -1:
                parsed[cur_ind] += letter
            else:
                parsed.append(letter)
                cur_ind = parsed.index(letter)
        else:
            cur_ind = -1
            if letter in klucz_INDEX_ERROR and len(parsed) <= 0:
                return False, 'Syntax error', parsed
            else:
                parsed.append(letter)
    for index_1 in range(parsed.count(' ')):
        parsed.remove(' ')

    return True, 'Input parsed!', parsed



