from itertools import combinations
from collections import defaultdict


def checkio(cakes):
    r = []
    d = defaultdict(set)
    result = 0
    for x, y in combinations(cakes, 2):
        if y[0] == x[0]:
            k = None
            b = y[0]
        else:
            k = (y[1] - x[1]) / (y[0] - x[0])
            b = k * x[0] - x[1]
        r.append([(k, b), str(x)])
        r.append([(k, b), str(y)])
    for i, j in r:
        d[i].add(j)
    for i in d.values():
        if len(i) >= 3:
            result += 1
    return result


def collinear(x, y, z):  # Checks if three points are collinear
    return (y[0] - x[0]) * (z[1] - x[1]) == (y[1] - x[1]) * (z[0] - x[0])


def checkio2(cakes):
    rows = set()
    for p, q in combinations(cakes, 2):
        colinear = frozenset(tuple(r) for r in cakes if collinear(p, q, r))
        if len(colinear) > 2:
            rows.add(colinear)
    return len(rows)


s1 = [[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]
s2 = [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
      [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]

print(checkio(s2))

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
            [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
             [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
