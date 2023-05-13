n = int(input())

def main():
    wyraz, ciag = input().split(sep=' ')

    licznik = {}
    for let in ciag:
        licznik[let] = 0
    keys = list(licznik.keys())
    for let in wyraz:
        if let in keys:
            licznik[let] += 1

    st = licznik[keys[0]]
    nd = licznik[keys[1]]

    if st == nd:
        print('=')
    elif st > nd:
        print(keys[0])
    elif st < nd:
        print(keys[1])



for _ in range(n):
    main()