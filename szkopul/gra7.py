przedzial = input().split(' ')
przedzial = int(przedzial[0]), int(przedzial[1])

wynik = 0

for liczba in range(przedzial[0], przedzial[1]+1):
    if len(str(liczba)) == 1 and str(liczba)[0] == '7':
        pass
    else:
        if liczba % 7 == 0:
            wynik += 1

        sum = 0
        for lit in str(liczba):
             sum += int(lit)
        if sum % 7 == 0:
            wynik += 1

print(wynik)
