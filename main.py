from string_parser import *


def result(res):
    print(f'Wynik to: {res}')


def main():
    rw = input('Wpisz działanie: ')
    parsed = parse_string(rw)
    print(parsed)
    main()


def define_operations(list):
    for sym in list:
        if sym == '-': # * -1
            print("l")


main()
