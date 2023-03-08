n: int = int(input())  # Ilosc slow

for _ in range(n):
    word_ind = 0

    word = str(input())
    for letter in word:
        if word_ind == 0 or word_ind == 2:
            if letter == 'b' or letter == 'B':
                word_ind += 1
        else:
            if letter == 'a' or letter == 'A':
                word_ind += 1
        if word_ind == 4:
            break

    if word_ind == 4:
        print("Tak")
    else:
        print("Nie")
