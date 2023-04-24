from collections import deque


def explore_neighbors(r, c, R, C, dr, dc, nodes_in_next_layer,rq, cq, visited, m):
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]

        # Skip out of bounds locations
        if rr < 0 or cc < 0 or rr >= R or cc >= C:
            continue

        # Skip visited locations or blocked cells
        if visited[rr][cc] or m[rr][cc] == '#':
            continue

        rq.append(rr)
        cq.append(cc)
        visited[rr][cc] = True
        nodes_in_next_layer += 1
        return nodes_in_next_layer


def BFS():
    # R = number of rows, C = number of columns
    R, C = 5, 7

    # Input character matrix of size R x C
    m = [
        ['S', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.', '.'],
        ['#', '.', '#', 'E', '.', '#', '.'],
    ]

    # 'S' symbol row and column values
    sr, sc = 0, 0

    # Empty Row Queue (RQ) and Column Queue (CQ)
    rq, cq = deque(), deque()

    # Variable used to track the number of steps taken
    move_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0

    # Variable used to track whether the 'E' character ever gets reached during the BFS
    reach_end = False

    # R x C matrix of false values used to track whether the node at position (i, j) has been visited
    visited = [
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
    ]

    # North, south, east, west direction vectors
    dr = [-1, +1, 0, 0]
    dc = [0, 0, +1, -1]

    rq.append(sr)
    cq.append(sc)
    visited[sr][sc] = True
    while rq.count() > 0:
        r = rq.popleft()
        c = cq.popleft()
        if m[r][c] == 'E':
            reach_end = True
            break
        nodes_in_next_layer = explore_neighbors(r, c, R, C, dr, dc, nodes_in_next_layer, rq, cq, visited, m)
        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            move_count += 1
        if reach_end:
            return move_count
        return -1

