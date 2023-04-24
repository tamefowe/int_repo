# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import adjacency_list as al
import adjacency_matrix as am


def get_matrix(g):
    g.add_edge(0, 0)    # Entry
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 4)
    g.add_edge(0, 5)
    g.add_edge(0, 6)

    g.add_edge(1, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(1, 6)

    g.add_edge(2, 0)
    g.add_edge(2, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    g.add_edge(3, 0)
    g.add_edge(3, 1)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)

    g.add_edge(4, 1)
    g.add_edge(4, 3)
    g.add_edge(4, 4)    # Exit
    g.add_edge(4, 6)
    return g


def get_adj_matrix():
    row_size, col_size = 5, 7
    g = am.Graph(row_size, col_size)
    g = get_matrix(g)
    g.print_matrix()


def get_adj_list():
    num = 5
    g = al.Graph(num)
    g = get_matrix(g)
    g.print_graph()


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
    while len(rq) > 0:
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


def loccate_card(cards, query):
    lo, hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        if mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
        else:
            return mid
    return -1


def print_dirs(pth):
    for d in os.listdir(pth):
        cpth = os.path.join(pth, d)
        if os.path.isdir(cpth):
            print_dirs(cpth)
        else:
            print(cpth)

from functools import wraps

def makebold(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapped

def makeitalic(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapped

@makebold
@makeitalic
def hello():
    return "hello world"

@makebold
@makeitalic
def log(s):
    return s







if __name__ == '__main__':
    #get_adj_list()
    #get_adj_matrix()
    squares = []
    for x in range(5):
        squares.append(lambda y: y**2)

    #print(squares[2](2))
    #print(squares[4](4))
    list = ['a', 'b', 'c', 'd', 'e']
    print( list[10:])
    #print( hello() ) # returns "<b><i>hello world</i></b>"
    #print( hello.__name__)  # with functools.wraps() this returns "hello"
    #print( log('hello'))

    #import os
    #d = r'C:\Users\Trader\Documents\docs\C++\C++ Refresher\Design'
    #print_dirs(d)

    #print('=====================================')
    #_ = [print(d) for d in os.walk(d)]
    #BFS()
