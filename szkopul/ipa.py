ilosc = int(input())
wzrosty = list(input().split(sep=' '))


TOL = 9
pary = 0

for Wind in range(len(wzrosty)):
    wz = int(wzrosty[Wind])

    for swind in range(Wind + 1, len(wzrosty)):
        wz2 = int(wzrosty[swind])
        if wz == wz2:
            pary += 1
        elif wz < wz2 and wz + TOL >= wz2:
            pary += 1
        elif wz > wz2 and wz - TOL <= wz2:
            pary += 1

print(pary)
