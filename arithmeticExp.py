import math


def cal(a, b, op):

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        return a * b


def MM(M, m, i, j, operators):

    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = cal(M[i][k], M[k+1][j], operators[k])
        b = cal(M[i][k], m[k+1][j], operators[k])
        c = cal(m[i][k], M[k+1][j], operators[k])
        d = cal(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def ans(operands, operators):

    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        m[i][i] = operands[i]
        M[i][i] = operands[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MM(M, m, i, j, operators)

    return M[0][n-1]


if __name__ == "__main__":
    exp = input()
    opert, operd = [], []

    for i in exp:
        if i in ['+', '-', '*']:
            opert.append(i)
        else:
            operd.append(int(i))

    print(ans(operd, opert))
