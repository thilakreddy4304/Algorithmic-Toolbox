a, b = [int(i) for i in input().split()]


def ans(a, b):
    if b == 0:
        return a
    c = a % b
    return ans(b, c)


if a > b:
    gcd = ans(a, b)
else:
    gcd = ans(b, a)

print(a*b//gcd)
