# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def isValid(s: str) -> bool:
        stck = []
        parentheses = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in parentheses:
                if stck and parentheses[c] == stck[-1]:
                    stck.pop()
                else:
                    return False
            else:
                stck.append(c)
        return not stck

graph = {
    'a' : ['b','c'],
    'b' : ['d'],
    'c' : ['e'],
    'd' : ['f'],
    'e' : [],
    'f' : []
}

def depth1Print(graph, source):
    stack = [source]
    visited = set()
    while stack:
        current = stack.pop()
        print(f"{current}")
        for neighbor in graph[current]:
            #if neighbor not in visited:
                stack.append(neighbor)
                #visited.add(neighbor)

def explore(graph, node, visited):
    if node in visited:
        return 0
    visited.add(node)
    size = 1
    for neighbor in graph[node]:
        size += explore(graph, neighbor, visited)
    return size



def largest_component(graph):
    maxsize = 0
    visited = set()
    for node in graph:
        size = explore(graph, node, visited)
        maxsize = max(size, maxsize)
    return maxsize

def minimum_path(graph, start, end):
    queue = [(start, 0)]
    visited = set()
    visited.add(start)
    while queue:
        current = queue.pop(0)
        if current[0] == end:
            return current[1]
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, current[1] + 1))
                visited.add(neighbor)
    return -1


def minimum_island(grid, row, col):
    visited = set()
    minsize = float("Inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSize(grid, r, c, visited)
            minsize = min(minsize, size)
    return minsize

def exploreSize(grid, r, c, visited):
    if r < 0 or r > len(grid) or c < 0 or c > len(grid[0]):
        return 0
    if grid[r][c] == 'W':
        return 0
    if (r, c) in visited:
        return 0
    visited.add((r, c))

    size = 1
    size += exploreSize(grid, r-1, c, visited)
    size += exploreSize(grid, r+1, c, visited)
    size += exploreSize(grid, r, c-1, visited)
    size += exploreSize(grid, r, c+1, visited)
    return size


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


t = Tree(5)
t.left = Tree(11)
t.right = Tree(3)
t.left.left = Tree(4)
t.left.right = Tree(15)
t.right.right = Tree(12)

u = Tree(5)
u.left = Tree(11)
u.right = Tree(3)
u.left.left = Tree(4)
u.left.right = Tree(15)
u.right.right = Tree(12)


def _isSameTree(p, q) -> bool:
    if not p and not q:
        return True
    if not p and q:
        return False
    if p and not q:
        return False
    return p.val == q.val and _isSameTree(p.left, q.left) and _isSameTree(p.right, q.right)


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p and q:
        return False
    if p and not q:
        return False
    pq = [p]
    qq = [q]
    while pq and qq:
        pc = pq.pop()
        qc = qq.pop()
        if pc.val != qc.val:
            return False
        if pc.left and qc.left:
            pq.append(pc.left)
            qq.append(qc.left)
        if pc.right and qc.right:
            pq.append(pc.right)
            qq.append(qc.right)
        if (pc.left and not qc.left) or (not pc.left and qc.left) or (pc.right and not qc.right) or (not pc.right and qc.right):
            return False
    return True


def printLeaves(tree):
    leaves = []
    printHelper(tree, leaves)
    return leaves


def printHelper(tree, leaves):
    if not tree:
        return
    if not tree.left and not tree.right:
        leaves.append(tree.val)
    printHelper(tree.left, leaves)
    printHelper(tree.right, leaves)
from collections import defaultdict


ttt = Tree(1)
ttt.left = Tree(2)
ttt.right = Tree(3)
ttt.left.left = Tree(4)
ttt.left.right = Tree(5)
ttt.right.left = Tree(6)
ttt.right.right = Tree(7)


def print_by_level(tree):
    if not tree:
        print('Empty tree')
        return
    l = []
    nodes = defaultdict(list)
    print_by_level_helper(tree, nodes, height=1)
    for _, v in nodes.items():
        l.extend(v + ['#'])
    return l


def rightSideView(root):
    if not root:
        return []
    return [root.val] + rightSideView(root.right)


def print_by_level_helper(tree, nodes, height):
    if not tree:
        return
    nodes[height].append(tree.val)
    print_by_level_helper(tree.left, nodes, height+1)
    print_by_level_helper(tree.right, nodes, height+1)
    height -= 1


def height_tree(tree):
    if not tree:
        return 0
    return 1 + max(height_tree(tree.left), height_tree(tree.right))


def _depthFirstValues(root):
    if not root:
        return
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.val)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)


def depthFirstValues(root):
    if not root:
        return
    print(root.val)
    depthFirstValues(root.left)
    depthFirstValues(root.right)


def hasValues(root, v):
    if not root:
        return False
    return (root.val == v) or hasValues(root.left, v) or hasValues(root.right, v)


def minimumTree(root):
    if not root:
        return float('-Inf')
    return max(root.val, minimumTree(root.left), minimumTree(root.right))


def hasPathSum(root, targetSum):
    if not root:
        return False
    targetSum -= root.val
    if not root.left and not root.rigth:
        return targetSum == 0

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)


tt = Tree(5)
tt.left = Tree(4)
tt.right = Tree(8)
tt.left.left = Tree(11)
tt.left.left.left = Tree(7)
tt.left.left.right = Tree(2)
tt.right.left = Tree(13)
tt.right.right = Tree(4)
tt.right.right.left = Tree(5)
tt.right.right.right = Tree(1)


def pathSum(root, targetSum):
    r = []
    rs = []
    getPathSum(root, targetSum, r, rs)
    return rs


from copy import deepcopy
def getPathSum(root, targetSum, r, rs):
    if not root:
        return []
    targetSum -= root.val
    r.append(root.val)
    if not root.left and not root.right:
        if targetSum == 0:
            rs.append(deepcopy(r))
    getPathSum(root.left, targetSum, r, rs)
    getPathSum(root.right, targetSum, r, rs)
    targetSum += root.val
    r.remove(root.val)

sum = 0
def sum_root_to_leaf_numbers():
    root = Tree(4)
    root.left = Tree(9)
    root.right = Tree(0)
    root.left.left = Tree(5)
    root.left.right = Tree(1)
    numb = 0
    getSum_root_to_leaf_numbers(root, numb)
    return sum


def getSum_root_to_leaf_numbers(root, numb):
    global sum
    if not root:
        return 0
    numb *= 10
    numb += root.val
    if not root.left and not root.right:
        sum += numb
    getSum_root_to_leaf_numbers(root.left, numb)
    getSum_root_to_leaf_numbers(root.right, numb)
    numb -= root.val
    numb /= 10


def isSymmetric(root):
    if not root:
        return True
    return isSymmetricHelper(root.left, root.right)


def isSymmetricHelper(root1, root2):
    if not root1 and not root2:
        return True
    if ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    return isSymmetricHelper(root1.left, root2.right) and isSymmetricHelper(root1.right, root2.left)




    # Press the green button in the gutter to run the script.


def kth_smallest(root, k):
    if not root:
        return -1
    elts = visit(root)
    sortedelts = sorted(elts)
    return sortedelts[k - 1]


def visit(root):
    if not root:
        return []
    return [root.val] + visit(root.left) + visit(root.right)


def sumOfLeftLeaves(root):
        num = 0
        if not root:
            return num

        if root.left and not root.left.left and not root.left.right:
            num = root.left.val
        return num + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)

tr = Tree(10)

numb = 0
def run_pathSum():
    targetSum=3
    root = Tree(10)
    root.left = Tree(5)
    root.left.left = Tree(3)
    root.left.left.left = Tree(3)
    root.left.left.right = Tree(-2)
    root.left.right = Tree(2)
    root.left.right.right = Tree(1)
    root.right = Tree(-3)
    root.right.right = Tree(11)
    pathSum(root, targetSum)
    return numb


def _pathSum(root, targetSum):
    global numb
    if not root:
        return 0
    if targetSum > root.val:
        targetSum -= root.val
        print(f"{targetSum} - {root.val}")
    if targetSum == 0:
        numb += 1
    _pathSum(root.left, targetSum)
    _pathSum(root.right, targetSum)
    if targetSum > root.val:
        targetSum += root.val
    print(f"targetSum = {targetSum}")

if __name__ == '__main__':
    print(f"{run_pathSum()}")
    #print(f"{sumOfLeftLeaves(tt)}")
    #print(f"{kth_smallest(tt, 5)}")
    #print(f"{sum_root_to_leaf_numbers()}")
    #targetSum = 22
    #print(f"{pathSum(tt, targetSum)}")
    #print(f"{isSameTree(t, u)}")
    #print(f"{rightSideView(ttt)}")
    #print(f"{print_by_level(ttt)}")
