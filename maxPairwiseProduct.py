def ans(arr):
    a = max(arr)
    arr.remove(a)
    b = max(arr)
    return a*b


n = int(input())
arr = list(map(int, input().split()))
print(ans(arr))
