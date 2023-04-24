

# Adjacency Matrix representation in Python

class Graph(object):

    def __init__(self, row_size, col_size):
        self.adjMatrix = []
        for i in range(row_size):
            self.adjMatrix.append([0 for i in range(col_size)])
        self.row_size = row_size
        self.col_size = col_size

    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        #self.adjMatrix[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            return

        self.adjMatrix[v1][v2] = 0
        #self.adjMatrix[v2][v2] = 0

    def __len__(self):
        return self.row_size * self.col_size

    def print_matrix(self):
        for row in self.adjMatrix:
            print(' '. join([str(r) for r in row]))
