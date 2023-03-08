n = int(input())
if n == 1:
    b = int(input())
    if b == 15:
        print("DOWN")

    elif b == 0:
        print("UP")

    else:
        print("UNKNOWN")

else:
    stan = [int(x) for x in input().split()]

    if stan[n-1] == 15:
        print("DOWN")
    elif stan[n-1] == 0:
        print("UP")
    elif stan[n-2] > stan[n-1]:  # e.g. [2, 1]
        print("DOWN")
    else:
        print("UP")
