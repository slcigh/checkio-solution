from collections import deque


def can_pass(matrix, first, second):
    q, v = deque([first]), set()
    while q:
        x, y = q.popleft()
        v.add((x, y))
        while (x, y) == second:
            return True
        direction = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for i, j in direction:
            try:
                if matrix[i][j] == matrix[x][y] and (i, j) not in v:
                    q.append([i, j])
            except IndexError:
                pass
    return False

