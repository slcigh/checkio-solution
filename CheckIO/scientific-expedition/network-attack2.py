def capture(matrix):
    free = list(range(1, len(matrix)))
    infected = [0]
    t = 0
    while free:
        t += 1
        underattack = []
        for i in infected:
            for j in free:
                if matrix[i][j] == 1 and j not in underattack:
                    underattack.append(j)
        for j in underattack:
            matrix[j][j] -= 1
            if matrix[j][j] == 0:
                free.remove(j)
                infected.append(j)
    return t
