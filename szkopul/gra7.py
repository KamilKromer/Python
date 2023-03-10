przedzial = input().split(' ')
przedzial = int(przedzial[0]), int(przedzial[1])

wynik = 0

for liczba in range(przedzial[0], przedzial[1]+1):
    if liczba % 7 == 0:
        wynik += 1
    suma = 0
    for lit in str(liczba):
        suma += int(lit)
    if suma % 7 == 0 and liczba != 7:
        wynik += 1

print(wynik)
