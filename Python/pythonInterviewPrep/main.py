# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict


def undirectedPath(edges, src, dst):
    queue = [src]
    graph = buildGraph(edges)
    while queue:
        current = queue.pop(0)
        if src == current:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


def buildGraph(edges):
    graph = defaultdict(list)
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]].append(edge[1])
        if edge[1] not in graph:
            graph[edge[1]].append(edge[0])
    return graph


def connectedComponentsCount(graph):
    visited = set()
    count = 0
    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, node, visited):
    if node in visited:
        return False
    visited.add(node)
    for neighbor in graph[node]:
        explore(graph, neighbor, visited)
    return True


def largestComponent(graph):
    visited = set()
    #biggest_size = 0
    biggest_size = float('inf')
    for node in graph:
        size = exploreSize(graph, node, visited)
        #if size > biggest_size:
        if size < biggest_size:
                biggest_size = size
    return biggest_size


def exploreSize(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    #size = node
    size = 1
    for neighbor in graph[node]:
        size += exploreSize(graph, neighbor, visited)
    return size


def shortestPath(edges, src, dst):
    graph = buildGraph(edges)
    queue = [[src, 0]]
    visited = set()
    visited.add(src)

    while queue:
        current, distance = queue.pop(1)
        if current == dst:
            return distance
        for node in graph[current]:
            if node not in visited:
                visited.add(node)
                queue.append([node, distance+1])
    return -1


def islandCount(grid):
    count = 0
    visited = set()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if exploreGrid(grid, r, c, visited):
                count += 1
    return count


def exploreGrid(grid, r, c, visited):
    r_inbound = r < 0 or r >= len(grid)
    c_inbound = c < 0 or c >= len(grid[0])
    if r_inbound or c_inbound:
        return False

    if (r, c) in visited:
        return False
    visited.add((r, c))

    if grid[r][c] == 'w':
        return False

    exploreGrid(grid, r-1, c, visited)
    exploreGrid(grid, r+1, c, visited)
    exploreGrid(grid, r, c-1, visited)
    exploreGrid(grid, r, c+1, visited)

    return True


def run():

    grid = [
        ['w', 'l', 'w', 'w', 'l', 'w'],
        ['l', 'l', 'w', 'w', 'l', 'w'],
        ['w', 'l', 'w', 'w', 'w', 'w'],
        ['w', 'w', 'w', 'l', 'l', 'w'],
        ['w', 'w', 'w', 'l', 'l', 'w'],
        ['l', 'w', 'w', 'l', 'w', 'w'],

    ]
    count = islandCount(grid)
    print(count)


def _main():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    size = largestComponent(graph)
    print(size)
    #count = connectedComponentsCount(graph)
    #print(count)


if __name__ == '__main__':
    run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
