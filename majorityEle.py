n = int(input())
arr = [int(i) for i in input().split()]


def ans(arr, l, r):
    if l+1 == r:
        return arr[l]
    elif l+2 == r:
        return arr[l]
    m = (l+r)//2
    left = ans(arr, l, m)
    right = ans(arr, m, r)

    c1, c2 = 0, 0
    for i in arr[l:r]:
        if i == left:
            c1 += 1
        elif i == right:
            c2 += 1
    if c1 > (r-l)//2 and left != -1:
        return left
    elif c2 > (r-l)//2 and right != -1:
        return right
    else:
        return -1


print(int(ans(arr, 0, n) != -1))
