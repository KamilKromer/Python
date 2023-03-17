import math

ilosc = int(input())
wzrosty = list(input().split(sep=' '))


tol = 100
pary = 0

for ind in range(len(wzrosty)): # To rework
    wzrost = int(wzrosty[ind])
    for ind2 in range(ind+1, len(wzrosty)):
        wzrost2 = int(wzrosty[ind2])

        tol_w = math.fabs(wzrost - wzrost2)
    if tol_w < tol:
        tol = tol_w


print(tol)


for Wind in range(len(wzrosty)):
    wz = int(wzrosty[Wind])

    for swind in range(Wind + 1, len(wzrosty)):
        wz2 = int(wzrosty[swind])
        if wz == wz2:
            pary += 1
        elif wz < wz2 and wz + tol >= wz2:
            pary += 1
        elif wz > wz2 and wz - tol <= wz2:
            pary += 1

print(pary)
