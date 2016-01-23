def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def capture(matrix):
    security = {0: 0}
    graph = {}
    length = len(matrix)
    for i in range(1, length):
        security[i] = matrix[i][i]
    r = [[j for j in range(length) if matrix[i][j] == 1 and i != j] for i in range(length)]

    for i in range(length):
        graph[i] = r[i]

    def value(array):
        return sum([security[i] for i in array])

    return max([min([value(i) for i in find_all_paths(graph, 0, i)]) for i in range(1, length)])


x = capture([[0, 1, 0, 1, 0, 1],
             [1, 8, 1, 0, 0, 0],
             [0, 1, 2, 0, 0, 1],
             [1, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 3, 1],
             [1, 0, 1, 0, 1, 2]])

print(x)

"""
# coding:utf-8
graph = {0: [1, 3, 5],
         1: [0, 2],
         2: [1, 5],
         3: [0, 4],
         4: [3, 5],
         5: [0, 2]}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        # ���node�ڵ�û���ʹ����͵ݹ飬�������for loop
        if node not in path:
            # �ݹ������ϵ����·��������ҵ�·�ˣ�start=end������һ·return
            # ����return none����������ͨ��for������node
            return find_path(graph, node, end, path)
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start] # ������һ��path��ԭpathֵδ�ı�
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)

            for newpath in newpaths:
                paths.append(newpath)
    print(paths)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


# print(find_path(graph, 0, 5))
# print(find_shortest_path(graph, 0, 2))
print(find_all_paths(graph, 0, 1))
"""
