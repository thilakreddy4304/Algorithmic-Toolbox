import math

paisa = int(input())
arr = [1, 3, 4]
minC = [0] + [math.inf]*paisa

for i in range(1, paisa+1):
    for j in arr:
        if i >= j:
            coins = minC[i-j]+1
            if coins < minC[i]:
                minC[i] = coins

print(minC[paisa])
