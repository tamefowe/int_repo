from collections import defaultdict
from math import sqrt, ceil


def get_adjacency_list(graph_nodes, graph_from, graph_to):
    graph = defaultdict(list)
    for i, j in zip(graph_from, graph_to):
        graph[i].append(j)
        graph[j].append(i)

    for i in range(1, graph_nodes):
        if i not in graph:
            graph[i] = []


def explore_nodes(graph, node, visited):
    if node in visited:
        return 0

    visited.add(node)

    size = 1
    for neighbor in graph[node]:
        size += explore_nodes(graph, node, visited)

    return size


def connectedSum(graph_nodes, graph_from, graph_to):
    # Write your code here
    result = 0
    graph = get_adjacency_list(graph_nodes, graph_from, graph_to)
    visited = set()

    if not graph:
        return 0

    for node in graph:
        size = explore_nodes(graph, node, visited)
        result += ceil(sqrt(size))
    return result


def roman_to_integer(name):
    romans = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    roman = name.split()[1]
    sum = 0
    for i in range(len(roman) - 1, -1, -1):
        n = romans[roman[i]]
        sum = (sum - n) if (3 * n) < sum else (sum + n)
        return sum


def sortRoman(names):
    # Write your code here
    return sorted(names, key=lambda x: (x, roman_to_integer(x)))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    names = ['Ste XL', 'Ste XVI', 'Dav IX', 'MA XV', 'MA XIII', 'MA XX']
    f = sortRoman(names)
    print()
