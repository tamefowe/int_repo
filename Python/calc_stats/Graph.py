from collections import defaultdict

graph = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]
_graph = [
    ['f', 'g'], #['g', 'f'] <--- add cycle
    ['f', 'i'],
    ['g', 'h'],
    ['i', 'g'],
    ['i', 'k'],
    ['j', 'i'],
    ['h', None],
    ['k', None]
]


def get_adj(graph):
    adj = defaultdict(list)
    for a, b in graph:
        if a not in adj:
            adj[a] = []
        elif b not in adj:
            adj[b] = []

        adj[a].append(b)
        adj[b].append(a)
    return adj

# acyclic directed graph traversal implementation
def dbfs(graph, src):
    stack = [src]
    while len(stack) > 0:
        cur = stack.pop()
        print(cur + ' ')
        for neighbor in graph[cur]:
            stack.append(neighbor)
def bfs(graph, src):
    queue = [src]
    while len(queue) > 0:
        cur = queue.pop(0)
        print(cur + ' ')
        for neighbor in graph[cur]:
            queue.append(neighbor)

def hasPath_dfs(graph, src, dst):
    if src == dst:
        return True
    for neighbor in graph[src]:
        if hasPath_dfs(graph, neighbor, dst):
            return True
    return False

def hasPath_bfs(graph, src, dst):
    queue = [src]
    while len(queue) > 0:
        cur = queue.pop(0)
        if cur == dst:
            return True
        for neighbor in graph[cur]:
            queue.append(neighbor)
    return False

# cyclic undirected graph traversal implementation

def hasPath_undirectedcyclic(graph, src, dst, isbfs):
    seen = set()
    if isbfs:
        return hasPath_bfs_undirectedcyclic(graph, seen, src, dst)
    else:
        return hasPath_dfs_undirectedcyclic(graph, seen, src, dst)

def hasPath_dfs_undirectedcyclic(graph, seen, src, dst):
    if src == dst:
        return True
    if src in seen:
        return False
    seen.add(src)
    for neighbor in graph[src]:
        if hasPath_dfs_undirectedcyclic(graph, seen, neighbor, dst):
            return True
    return False

def hasPath_bfs_undirectedcyclic(graph, seen, src, dst):
    queue = [src]
    while len(queue) > 0:
        cur = queue.pop(0)
        if cur == dst:
            return True
        if cur not in seen:
            seen.add(cur)
        for neighbor in graph[cur]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False

def count_connected_cmps():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    seen = set()
    num_cmps = 0
    for node in graph:
        if explore_node(graph, seen, node):
            num_cmps += 1
    return num_cmps

def explore_node(graph, seen, node):
    if node in seen:
        return False
    seen.add(node)
    for neighbor in graph[node]:
        explore_node(graph, seen, neighbor)
    return True


def largest_cmp():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
    }
    seen = set()
    #largest_size = 0
    smallest_size = float('Inf')
    for node in graph:
        size = lc_explore_node(graph, seen, node)
        #largest_size = max(size, largest_size)
        if size > 0:
            smallest_size = min(size, smallest_size)
    #return largest_size
    return smallest_size

def lc_explore_node(graph, seen, node):
    if node in seen:
        return 0
    seen.add(node)
    size = 1
    for neighbor in graph[node]:
        size += lc_explore_node(graph, seen, neighbor)
    return size

def shortest_path(src, dst):
    edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
    graph = get_adj(edges)
    seen = {src}
    queue = [(src, 0)]
    while len(queue) > 0:
        (node, distance) = queue.pop(0)
        if node == dst:
            return distance
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    return -1

def longest_path_graph(node):
    edges = [
        [0, 1],
        [1, 2],
        [2, 3],
        [2, 9],
        [2, 4],
        [4, 5],
        [1, 6],
        [6, 7],
        [6, 8]
    ]
    graph = get_adj(edges)
    #if not node:
    #    return None

    queue = [(node, 0)]
    seen = {node}
    mx_dist = 0
    mx_node = None
    while queue:
        cur, distance = queue.pop(0)
        if mx_dist < distance:
            mx_dist = distance
            mx_node = cur
        for neighbor in graph[cur]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, distance+1))
    return mx_node, mx_dist

def island_count():
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    R, C = len(grid), len(grid[0])
    seen = set()
    count = 0
    for r in range(R):
        for c in range(C):
            if ic_explore_node(grid, r, c, R, C, seen):
                count += 1

    return count

def ic_explore_node(grid, r, c, R, C, seen):
    is_outbound = r < 0 or r >= R or c < 0 or c >= C
    if is_outbound:
        return False
    if grid[r][c] == 'W':
        return False
    if (r, c) in seen:
        return False
    seen.add((r, c))

    ic_explore_node(grid, r+1, c, R, C, seen)
    ic_explore_node(grid, r-1, c, R, C, seen)
    ic_explore_node(grid, r, c+1, R, C, seen)
    ic_explore_node(grid, r, c-1, R, C, seen)

    return True


def minimum_island():
    grid = [
        ['W', 'L', 'W', 'L', 'W'],
        ['L', 'L', 'W', 'L', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['W', 'W', 'L', 'W', 'W'],
    ]
    R, C = len(grid), len(grid[0])
    seen = set()
    min_size = float('Inf')
    for r in range(R):
        for c in range(C):
            size = explore(grid, r, c, R, C, seen)
            if size > 0:
                min_size = min(min_size, size)
    return min_size

def explore(grid, r, c, R, C, seen):
    is_outbound = r < 0 or r >= R or c < 0 or c >= C
    if is_outbound:
        return 0
    if grid[r][c] == 'W':
        return 0
    if (r, c) in seen:
        return 0
    seen.add((r, c))

    size = 1
    size += explore(grid, r-1, c, R, C, seen)
    size += explore(grid, r+1, c, R, C, seen)
    size += explore(grid, r, c-1, R, C, seen)
    size += explore(grid, r, c+1, R, C, seen)

    return size



def isCyclic():
    _graph = [
    ['g', 'f'],
    ['f', 'i'],
    ['g', 'h'],
    ['i', 'g'],
    ['i', 'k'],
    ['j', 'i'],
    ['h', None],
    ['k', None]
    ]
    src = 'i'
    graph = get_adj(_graph)
    seen = set()
    for node in graph:
        if is_cyclic_explore(graph, node, seen):
            return True
    return False

def is_cyclic_explore(graph, node, seen):
    if node in seen:
        return True
    seen.add(node)

    for neighbor in graph[node]:
        if is_cyclic_explore(graph, neighbor, seen):
            return True
    return False








