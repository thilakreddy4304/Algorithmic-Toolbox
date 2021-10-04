import numpy


def mG(W, n, items):

    arr = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):

            arr[i][j] = arr[i][j-1]
            if items[j-1] <= i:

                temp = arr[i-items[j-1]][j-1] + items[j-1]

                if temp > arr[i][j]:
                    arr[i][j] = temp

    return (int(arr[W][n]), arr)


def pI(ans, items, i, j, arr):

    if i == 0 and j == 0:
        arr.reverse()
        return arr
    if ans[i][j] == ans[i][j-1]:
        arr.append(0)
        return pI(ans, items, i, j-1, arr)
    else:
        arr.append(1)
        return pI(ans, items, i-items[j-1], j-1, arr)


if __name__ == '__main__':
    W, n = [int(i) for i in input().split()]
    item_weights = [int(i) for i in input().split()]
    max_weight, Matrix = mG(W, n, item_weights)
    bv = pI(Matrix, item_weights, W, n, [])
    optimal = [str(j) for i, j in enumerate(item_weights) if bv[i]]
    print(f"Weights in knapsack of capacity {W}: {' '.join(optimal)}")
