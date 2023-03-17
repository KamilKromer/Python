
n = int(input())

for _ in range(n):

    liczba = int(input())
    
    suma = int( ( liczba * (liczba + 1) ) / 2 )
    pow = 0

    while 2**pow <= liczba:
        pow += 1
    
    suma -= ( (2**pow) - 1 )*2
    print(suma)

