n, L, a = input().split(sep=" ")
n, L, a = int(n), int(L), int(a)

klienci = {}
aktualny_czas = 0
suma_przerw = 0


for _ in range(n):
    kiedy, czas = input().split(sep=" ")
    kiedy, czas = int(kiedy), int(czas)
    klienci[kiedy] = czas

id_ = 0
while(aktualny_czas < L): # Dla każdego klienta
    try:
        kiedy = list(klienci.keys())[id_]
        id_ += 1
        ile = klienci[kiedy]

        if aktualny_czas + a <= kiedy:
            while (aktualny_czas + a <= kiedy):
                suma_przerw += 1
                aktualny_czas += a
        else:
            aktualny_czas += ile

    except IndexError: # Koniec klientów, obliczaj ile przerw do konca zmiany
        if aktualny_czas + a <= L:
            aktualny_czas += a
            suma_przerw += 1
            continue
        else:
            break


print(suma_przerw)
