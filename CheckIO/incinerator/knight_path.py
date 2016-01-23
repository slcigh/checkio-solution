def possible_moves(s):
    direction = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    pm = []
    for i in [chr(ord(s[0]) + x) + str(int(s[1]) + y) for x, y in direction]:
        if "a" <= i[0] <= "h" and "1" <= i[1] <= "8":
            pm.append(i)
    return pm


def checkio(cells):
    """str -> int
    Number of moves in the shortest path of knight
    """
    shortest_moves = 100
    start, goal = cells.split("-")
    q = [(start, 0, {start})]
    while q:
        s, m, v = q.pop(0)
        for moves in possible_moves(s):
            if moves == goal:
                if m + 1 < shortest_moves:
                    shortest_moves = m + 1
            elif moves not in v:
                v.add(moves)
                q.append((moves, m + 1, v))
    return shortest_moves


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("b1-d5") == 2, "1st example"
    assert checkio("a6-b8") == 1, "2nd example"
    assert checkio("h1-g2") == 4, "3rd example"
    assert checkio("h8-d7") == 3, "4th example"
    assert checkio("a1-h8") == 6, "5th example"
