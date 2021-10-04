import numpy


def ED(s1, s2):

    ln_s1 = len(s1)
    ln_s2 = len(s2)

    Matrix = numpy.zeros((ln_s1+1, ln_s2+1))
    for i in range(ln_s2+1):
        Matrix[0][i] = i

    for i in range(ln_s1+1):
        Matrix[i][0] = i

    for i in range(1, ln_s1+1):
        for j in range(1, ln_s2+1):
            insertion = Matrix[i][j-1] + 1
            deletion = Matrix[i-1][j] + 1
            mismatch = Matrix[i-1][j-1] + 1
            match = Matrix[i-1][j-1]
            if s1[i-1] == s2[j-1]:
                Matrix[i][j] = min(insertion, deletion, match)
            if s1[i-1] != s2[j-1]:
                Matrix[i][j] = min(insertion, deletion, mismatch)

    return (int(Matrix[ln_s1][ln_s2]), Matrix)


def OA(Matrix, s1, s2, top, bottom, i, j):

    if i == 0 and j == 0:
        return (' '.join(top[::-1]), ' '.join(bottom[::-1]))

    if i > 0 and Matrix[i][j] == Matrix[i-1][j] + 1:
        top.append(f'|{s1[i-1]}|')
        bottom.append('|-|')
        return OA(Matrix, s1, s2, top, bottom, i-1, j)

    elif j > 0 and Matrix[i][j] == Matrix[i][j-1] + 1:
        bottom.append(f'|{s2[j-1]}|')
        top.append('|-|')
        return OA(Matrix, s1, s2, top, bottom, i, j-1)

    else:
        top.append(f'|{s1[i-1]}|')
        bottom.append(f'|{s2[j-1]}|')
        return OA(Matrix, s1, s2, top, bottom, i-1, j-1)


if __name__ == '__main__':
    s1, s2 = input(), input()
    edit_distance, Matrix = ED(s1, s2)
    top, bottom = OA(Matrix, s1, s2, [], [], len(s1), len(s2))

    print(edit_distance)
