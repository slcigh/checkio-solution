from timeit import timeit

graph = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]]

graph2 = [(1, 4), (3, 6), (5, 8), (1, 2), (1, 8), (2, 3), (1, 7), (2, 5), (6, 7), (2, 6), (2, 7), (1, 5), (5, 7),
          (4, 8), (3, 5), (3, 4), (2, 8), (3, 8), (4, 7), (2, 4), (3, 7), (4, 5), (7, 8), (4, 6), (1, 6), (6, 8),
          (1, 3), (5, 6)]

graph3 = [(6, 8), (3, 8), (3, 4), (3, 5), (2, 8), (3, 9), (2, 7), (4, 7), (5, 8), (5, 10), (7, 9), (2, 6),
          (5, 6), (7, 8), (6, 7), (1, 3), (9, 10), (1, 10), (3, 6), (4, 10), (6, 9), (2, 3), (3, 10), (1, 5),
          (1, 7), (4, 5), (2, 4), (8, 9), (2, 9), (4, 8), (2, 10), (2, 5), (8, 10), (1, 6)]


def find_cycle(connections):
    nodes_set = set()
    cycles = []
    nodes_dict = {}
    for i in connections:
        nodes_set = nodes_set | set(i)
    for i in nodes_set:
        nodes_dict[i] = [list(set(j) - {i})[0] for j in connections if i in j]

    # print(nodes_dict)

    def find_circles(path):
        start = path[0]
        for adj in nodes_dict[start]:
            if adj not in path:
                find_circles([adj] + path)
            elif len(path) > 2 and adj == path[-1]:
                if len(path) == len(nodes_set):
                    return path + [path[0]]
                if set(path) not in [set(c) for c in cycles]:
                    cycles.append(path)

    for n in nodes_set:
        find_circles([n])

        # print(cycles)
        #   m = max(cycles, key=len)
        # return m+[m[0]]
    return cycles


from collections import defaultdict


def find_cycle2(connections):
    graph = defaultdict(set)
    for n1, n2 in connections:
        graph[n1].add(n2)
        graph[n2].add(n1)
    result = []
    for node in graph.keys():
        stack = [(node, [node])]
        while stack:
            n, path = stack.pop()
            for neighbor in graph[n]:
                if neighbor == node:
                    if len(path) > 2 and len(path) >= len(result):
                        result = path + [node]
                elif neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
    return result


find_cycle2(graph3)

print(timeit('find_cycle2(graph3)', setup='from __main__ import find_cycle2, graph3', number=1))
