def merge(left, right):
    i, j, ic = 0, 0, 0
    arr = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            ic += len(left) - i
            j += 1

    arr += left[i:]
    arr += right[j:]

    return arr, ic


def mergesort(arr):
    global count
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sa, temp = merge(left, right)
    count += temp

    return sa


count = 0
n = int(input())
seq = [int(i) for i in input().split()]
mergesort(seq)
print(count)
