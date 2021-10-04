a, b = [int(i) for i in input().split()]


def ans(a, b):
    while(b):
        a, b = b, a % b

    return a


print(ans(a, b))
