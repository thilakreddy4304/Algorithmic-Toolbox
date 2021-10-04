n = int(input())
count = 0
for i in [10, 5, 1]:
    if n >= i:
        a = n//i
        count += a
        n = n % i
        if n == 0:
            print(count)
            exit
