# Alfabetyczna Gra - Kamil Kusiak | Szkopuł 2023

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

s = input()

for k in range(len(s)):
    l, r = k, k
    moves = 0
    start = s[l]
    ind = 0
    for letter in s[0:l]:
        if ALPHABET.index(letter) < ALPHABET.index(start):
            l = ind
            moves += 1
            break
        ind += 1

    if moves % 2 == 0:
        print("K")
    else:
        print("B")
       
    