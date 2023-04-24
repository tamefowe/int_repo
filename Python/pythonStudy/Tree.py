import copy

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def run_all_tree_paths():
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    e.right = h
    f.left = i

    # paths = []
    # path = []
    # _all_tree_paths(q, paths, path)
    paths = all_tree_paths(a)
    print(paths)


def all_tree_paths(root):
    stack = [root]
    path = []
    paths = []
    while stack:
        cur = stack.pop()
        path.append(cur.val)

        if not cur.left and not cur.right:
            paths.append(copy.deepcopy(path))
            path.pop()

        if cur.left:
            stack.append(cur.left)
            #path.pop()

        if cur.right:
            stack.append(cur.right)

            #path.pop()

    return paths


def _all_tree_paths(root, paths, path):
    if not root:
        return []

    path.append(root.val)

    if root.left is None and root.right is None:
        paths.append(copy.deepcopy(path))

    if root.left:
        _all_tree_paths(root.left, paths, path)

    if root.right:
        _all_tree_paths(root.right, paths, path)

    path.pop()


def run_bottom_right_value():
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    val = bottom_right_value(a)
    print(val)


def bottom_right_value(root):
    queue = [root]
    cur = None
    while queue:
        cur = queue.pop(0)

        if cur.left:
            queue.append(cur.left)

        if cur.right:
            queue.append(cur.right)

    return cur.val