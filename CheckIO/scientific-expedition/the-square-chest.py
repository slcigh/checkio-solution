def checkio(lines_list):
    """Return the quantity of squares"""
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix = matrix + list(zip(*matrix))
    up = [(i, i + 1) for i in range(1, 12) if i % 4] + [(i, i + 2) for i in range(8) if 1 <= i % 4 <= 2] + [(1, 4)]
    left = [(i, i + 4 * (j - i)) for i, j in up]
    down = [(j, j + int((j - i) / 4)) for i, j in left]
    right = [(j, j + 4 * (j - i)) for i, j in up]
    square = list(map(set, zip(up, left, down, right)))
    lines_list = map(sorted, lines_list)
    s1 = [(i, j) for i, j in lines_list if j - i == 1 or j - i == 4]
    s2 = [(i, j) for i, j in lines_list if j - i == 2 or j - i == 8]
    s3 = [(i, j) for i, j in lines_list if j - i == 3 or j - i == 12]
    t = [[] for _ in range(8)]
    for i in range(8):
        for x, y in s1:
            if x in matrix[i] and y in matrix[i]:
                t[i].append([x, y])
    for i in t:
        if len(i) == 3:
            s3.append((i[0][0], i[-1][-1]))
            s2.extend([(i[0][0], i[1][1]), (i[1][0], i[-1][-1])])
        elif len(i) == 2:
            if i[0][1] == i[1][0]:
                s2.append((i[0][0], i[-1][-1]))
    r = 0
    for i in square:
        if i <= set(s1) or i <= set(s2) or i <= set(s3):
            r += 1

    return r


checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
         [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
         [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]])

checkio([[1, 2], [1, 5], [2, 6], [5, 6]])

"""
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
"""
