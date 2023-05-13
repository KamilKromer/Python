kwiatki, skok = [int(x) for x in input().split(sep=" ")]
sekwencja = input()

pozycja = 0
przesuniecie = 0

ilosc = 0

for i in range(kwiatki):
    if przesuniecie <= -skok:
        ilosc = -1
        break
    if pozycja + skok >= len(sekwencja) - 1:
        ilosc += 1
        break

    if sekwencja[pozycja + skok + przesuniecie] == "1":
        pozycja += skok + przesuniecie
        przesuniecie = 0
        ilosc += 1
    else:
        przesuniecie -= 1

print(ilosc)