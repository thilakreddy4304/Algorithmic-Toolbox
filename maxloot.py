n, W = [int(i) for i in input().split()]
arr = []

if W == 0:
    print(0)
    quit()

for _ in range(n):
    v, w = [int(i) for i in input().split()]
    if v == 0:
        continue
    arr.append((v, w))

arr.sort(key=lambda x: x[0]/x[1], reverse=True)

ans = 0

for v, w in arr:
    if W == 0:
        print(ans)
        quit()
    amount = min(w, W)
    ans += amount*v/w
    W -= amount

print(ans)
