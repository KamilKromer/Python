from math import gcd

max_x, max_y, x, y = [int(i) for i in input().split(sep=' ')]

divisor = gcd(x, y)
x /= divisor
y /= divisor


print(int(min(max_x//x, max_y//y)))
    