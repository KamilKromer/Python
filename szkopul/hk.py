_ = int(input())
ksiazki = list(input().split(sep=' '))

d_ksiazki = {}

for ind in range(len(ksiazki)):
    ksiazki[ind] = int(ksiazki[ind]) # Konwertuj wszystko na int

for book in ksiazki:
    try:
        _ = d_ksiazki[book]  # Jezeli nie jest to bląd

        d_ksiazki[book] += 1 # Znalezlismy tą samą ksiązke
    except KeyError:
        d_ksiazki[book] = 1


# Mamy ksiazki w słowniku

klucze = d_ksiazki.keys()
war_l = 0, 0
for k in klucze:
    war = d_ksiazki[k], k
    if war[0] > war_l[0]:
        war_l = war
    elif war[0] == war_l[0]: # Są ksiązki o tych samych rozmiarach, i tej samej ilości
        if war[1] > war_l[1]:
            war_l = war

print(war_l[1])

