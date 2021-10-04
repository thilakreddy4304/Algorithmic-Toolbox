arr = [int(i) for i in input().split()]
search_seq = [int(i) for i in input().split()]
n = arr[0]
arr = arr[1:]


def binarysearch(arr, elt, r):
    l = 0
    while l <= r:
        m = (l+r)//2
        if elt > arr[m]:
            l = m + 1
        elif elt < arr[m]:
            r = m - 1
        else:
            return m
    return -1


soln = list()
for i in search_seq[1:]:
    ans = binarysearch(arr, i, n-1)
    soln.append(ans)
print(' '.join([str(i) for i in soln]))
