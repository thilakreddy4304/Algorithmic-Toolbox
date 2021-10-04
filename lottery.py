arr = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    arr.append((a, 'l'))
    arr.append((b, 'r'))

points = input().split()
for i in points:
    arr.append((int(i), 'p'))

arr.sort()

sc = 0
psm = dict()
for i in arr:
    if i[1] == 'l':
        sc += 1
    elif i[1] == 'r':
        sc -= 1
    else:
        psm[i[0]] = sc

temp = ''
for i in points:
    temp += str(psm[int(i)]) + ' '
print(temp[:-1])
