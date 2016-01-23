def recall_password(grille, password):
    matrix_p = [list(i) for i in password]
    m0 = [list(i) for i in grille]
    m1 = list(zip(*m0[::-1]))  # right
    m2 = [i[::-1] for i in m0[::-1]]  # upside down
    m3 = list(zip(*m0))[::-1]  # left
    r = ""
    for x in [m0, m1, m2, m3]:
        for i in range(4):
            for j in range(4):
                if x[i][j] == "X":
                    r += matrix_p[i][j]
    return r


z = recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi'))


print(z)