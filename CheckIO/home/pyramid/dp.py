def count_gold(pyramid):
    pyramid = [list(i) for i in pyramid]
    l = len(pyramid)
    for i in range(1, l):
        for j in range(i + 1):
            if j == 0:
                pyramid[i][j] += pyramid[i - 1][j]
            elif j == i:
                pyramid[i][j] += pyramid[i - 1][j - 1]
            else:
                pyramid[i][j] += max(pyramid[i - 1][j], pyramid[i - 1][j - 1])
    return max(pyramid[-1])


def count_gold2(pyramid):
    py = [list(i) for i in pyramid]
    for i in reversed(range(len(py) - 1)):
        for j in range(i + 1):
            py[i][j] += (max(py[i + 1][j], py[i + 1][j + 1]))
    return py[0][0]
