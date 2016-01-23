from collections import defaultdict


def checkio(str):
    graph = defaultdict(set)
    for n1, n2 in [list(i) for i in str.split(",")]:
        graph[n1].add(n2)
        graph[n2].add(n1)
    q = [['1', '1']]
    while q:
        start, path = q.pop(0)
        for adja in graph[start]:
            if adja == '1' and len(set(path)) == 8:
                return path + adja
            try:
                past = path[-2]
            except IndexError:
                past = None
            if adja != past:
                q.append([adja, path + adja])


def checkio2(teleports_string):
    connects = set(teleports_string.split(','))
    print(connects)
    stack = [('1', connects)]
    while stack:
        route, connects = stack.pop()
        if len(set(route)) == 8 and route.endswith('1'):
            return route
        connected_paths = [c for c in connects if route[-1] in c]
        for p in connected_paths:
            stack.append((route + p.strip(route[-1]), connects - {p}))


s = "12,28,87,71,13,14,34,35,45,46,63,65"
s2 = "12,23,34,45,56,67,78,81"
print(checkio(s))
print(checkio2(s))

# This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True


    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
