import numpy


def ans(s1, s2, n1, n2):

    arr = numpy.zeros((n1+1, n2+1))

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            if s1[i-1] != s2[j-1]:
                arr[i][j] = max(arr[i][j-1], arr[i-1][j])

    return (int(arr[n1][n2]), arr)


def ps(arr, s1, s2, i, j, seq):

    if i == 0 or j == 0:
        if seq == []:
            return None
        return ''.join(seq[::-1])

    if s1[i-1] == s2[j-1]:
        seq.append(s1[i-1])
        return ps(arr, s1, s2, i-1, j-1, seq)

    if Matrix[i-1][j] > Matrix[i][j-1]:
        return ps(arr, s1, s2, i-1, j, seq)
    else:
        return ps(arr, s1, s2, i, j-1, seq)


if __name__ == '__main__':
    n1, s1, n2, s2 = int(input()), input(), int(input()), input()

    LCS_length, Matrix = ans(s1, s2, n1, n2)
    sequence = ps(Matrix, s1, s2, n1, n2, [])
    print('Length of LCS:', LCS_length)
    print('LCS:', sequence)
