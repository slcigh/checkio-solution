from collections import defaultdict


def checkio(numbers):
    d = defaultdict(list)
    for i in numbers:
        for j in numbers:
            if is_ladder(i, j):
                d[i].append(j)
    # print(d)
    start, goal = numbers[0], numbers[-1]
    q = [[start, [start], set()]]
    while q:
        cur, path, visited = q.pop(0)
        for i in d[cur]:
            if i == goal:
                return path + [i]
            if i not in visited:
                visited.add(i)
                q.append([i, path + [i], visited])


def is_ladder(n1, n2):
    r = 0
    n1, n2 = str(n1), str(n2)
    for i in range(3):
        if n1[i] == n2[i]:
            r += 1
    return r == 2


t1 = checkio([123, 991, 323, 321, 329, 121, 921, 125, 999])
print(t1)
