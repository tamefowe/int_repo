
# Adjacency List representation in Python
from collections import defaultdict

class AdjNode(object):
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph(object):
    def __init__(self, num):
        self.V = num
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        if s >= self.V:
            raise IndexError('{} is beyond {}'.format(s, self.V))
        self.graph[s].append(d)

    def print_graph(self):
        for i in range(self.V):
            print('Vertex ' + str(i) + ':', end="")
            print(' '.join([str(j) for j in self.graph[i]]))

