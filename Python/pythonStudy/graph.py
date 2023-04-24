from collections import defaultdict


def graph_search():
    graph = dict(
        a=['b', 'c'],
        b=['d'],
        c=['e'],
        d=['f'],
        e=[],
        f=[]
    )
    source = 'a'

    def depth_first_search_util_1(graph, source):
        stack = [source]
        seen = {source}
        while stack:
            current = stack.pop()
            print(current)
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

    def depth_first_search_util_2(graph, source, seen=set()):
        print(source)
        seen.add(source)
        for neighbor in graph[source]:
            if neighbor not in seen:
                seen.add(neighbor)
                depth_first_search_util_2(graph, neighbor, seen)

    def breadth_first_search(graph, source):
        queue = [source]
        seen = {source}
        while queue:
            current = queue.pop(0)
            print(current)
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

    depth_first_search_util_1(graph, source)
    print('-'*20)
    depth_first_search_util_2(graph, source)
    print('-'*20)
    breadth_first_search(graph, source)


def has_path():
    graph = dict(
        a=['g', 'i'],
        g=['h'],
        h=[],
        i=['g', 'k'],
        j=['i'],
        k=[]
    )
    src, dst = 'j', 'h'

    def has_path_dfs(graph, src, dst, seen):
        if src == dst:
            return True
        if src in seen:
            return False
        seen.add(src)
        for neighbor in graph[src]:
            if has_path_dfs(graph, neighbor, dst, seen):
                return True
        return False

    def has_path_bfs(graph, src, dst, seen):
        queue = [src]
        seen.add(src)
        while queue:
            current = queue.pop(0)
            if current == dst:
                return True
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return False

    print(f"{has_path_dfs(graph, src, dst)}")
    print('*'*20)
    print(f"{has_path_bfs(graph, src, dst)}")


def construct_graph(edges):
    edges_ = [
        ['i', 'j'],
        ['k', 'i'],
        ['m', 'k'],
        ['k', 'l'],
        ['o', 'n']
    ]
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def connected_components_count():
    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }

    def explore(graph, node, seen):
        if node in seen:
            return False
        seen.add(node)
        for neighbor in graph[node]:
            explore(graph, neighbor, seen)
        return True

    def connected_components_count_utils(graph):
        count = 0
        seen = set()
        for node in graph:
            if explore(graph, node, seen):
                count += 1
        return count

    print(f"number of connected components: {connected_components_count_utils(graph)}")


def largest_component():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    def explore(graph, node, seen):
        size = 1
        if node in seen:
            return 0
        seen.add(node)
        for neighbor in graph[node]:
            size += explore(graph, neighbor, seen)
        return size

    def largest_component_util(graph):
        seen = set()
        largest_size = float('-Inf')

        for node in graph:
            size = explore(graph, node, seen)
            largest_size = max(largest_size, size)
        return largest_size

    print(f"Largest component: {largest_component_util(graph)}")


def shortest_path():
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]

    graph = construct_graph(edges)
    start, end = 'w', 'z'

    def shortest_path_util(graph, start, end):
        queue = [(start, 0)]
        seen = {start}
        while queue:
            (current, distance) = queue.pop(0)
            if current == end:
                return distance
            for neighbor in graph[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance+1))
        return -1

    print(f"Length of shortest path: {shortest_path_util(graph, start, end)}")


def island_count():
    islands = [
        ['w', 'l', 'w', 'w', 'l', 'w'],
        ['l', 'l', 'w', 'w', 'l', 'w'],
        ['w', 'l', 'w', 'w', 'w', 'w'],
        ['w', 'w', 'w', 'l', 'l', 'w'],
        ['w', 'l', 'w', 'l', 'l', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w'],
    ]

    def explore(islands, row, col, visited):

        if row < 0 or row >= len(islands) or col < 0 or col >= len(islands[0]):
            return False

        if islands[row][col] == 'w':
            return False

        if (row, col) in visited:
            return False
        visited.add((row, col))

        explore(islands, row+1, col, visited)
        explore(islands, row, col+1, visited)
        explore(islands, row-1, col, visited)
        explore(islands, row, col-1, visited)

        return True

    def island_count_util(islands):
        num_islands = 0
        visited = set()
        for row in range(len(islands)):
            for col in range(len(islands[0])):
                if explore(islands, row, col, visited):
                    num_islands += 1
        return num_islands

    print(f"Numbers of islands: {island_count_util(islands)}")


def minimum_island():
    islands = [
        ['w', 'l', 'w', 'w', 'l', 'w'],
        ['l', 'l', 'w', 'w', 'l', 'w'],
        ['w', 'l', 'w', 'w', 'w', 'w'],
        ['w', 'w', 'w', 'l', 'l', 'w'],
        ['w', 'l', 'w', 'l', 'l', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w'],
    ]

    def explore(islands, row, col, visited):
        if row < 0 or row >= len(islands) or col < 0 or col >= len(islands[0]):
            return 0
        if islands[row][col] == 'w':
            return 0
        if (row, col) in visited:
            return 0
        visited.add((row, col))
        size = 1
        size += explore(islands, row-1, col, visited)
        size += explore(islands, row+1, col, visited)
        size += explore(islands, row, col-1, visited)
        size += explore(islands, row, col+1, visited)
        return size

    def minimum_island_util(islands):
        minimum_size = float('Inf')
        visited = set()
        for row in range(len(islands)):
            for col in range(len(islands[0])):
                size = explore(islands, row, col, visited)
                if size > 0:
                    minimum_size = min(minimum_size, size)
        return minimum_size

    print(f"Minimum island size: {minimum_island_util(islands)}")


def course_schedule():
    numCourses = 2
    prerequisites = [[1, 0]] #, [0, 1]]

    def is_cyclic(graph, node, visited):
        if node in visited:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if is_cyclic(graph, neighbor, visited):
                return True
        return False

    def make_graph(numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)
        return graph

    def course_schedule_util(numCourses, prerequisites):
        graph = make_graph(numCourses, prerequisites)
        visited = set()
        for node in graph:
            if is_cyclic(graph, node, visited):
                return False
        return True

    print(f"{'possible' if course_schedule_util(numCourses, prerequisites) else 'impossible'}")
