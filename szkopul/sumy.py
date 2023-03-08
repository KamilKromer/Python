
n = int(input())

for _ in range(n):

    sumy = int(input())
    pow_ind = 0
    suma = 0
    potega = 1
    for op in range(sumy):
        liczba = op + 1
        if liczba == potega:
            pow_ind += 1
            potega = 2 ** pow_ind
            suma -= liczba
        else:
            suma += liczba
        print("p")


    print(suma)


