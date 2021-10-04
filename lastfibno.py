n = int(input())


def fibo(n):
    if(n <= 1):
        return n
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        c %= 10
        b, a = c, b
    return c


print(fibo(n))
