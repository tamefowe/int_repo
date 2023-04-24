
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(3)
b = Node(5)
c = Node(2)
d = Node(6)
e = Node(2)
f = Node(0)
g = Node(4)
h = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
g.right = h

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print("%d " % root.val)
    inorder(root.right)

def count_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left_count, right_count = 0, 0
    if root.left:
        left_count = count_nodes(root.left)
    if root.right:
        right_count = count_nodes(root.right)
    return 1 + left_count + right_count

def sum_tree(root):
    if root is None:
        return 0
    left_sum, right_sum = 0, 0
    if root.left :
        left_sum = sum_tree(root.left)
    if root.right :
        right_sum = sum_tree(root.right)

    return root.val + left_sum + right_sum

def max_min_tree(root):
    if root is None:
        #return float('Inf')
        return float('-Inf')
    #lmn, rmn = float('Inf'), float('Inf')
    lmx, rmx = float('-Inf'), float('-Inf')
    if root.left is not None:
        #lmn = max_min_tree(root.left)
        lmx = max_min_tree(root.left)
    if root.right is not None:
        #rmn = max_min_tree(root.right)
        rmx = max_min_tree(root.right)
    #return min(root.val, lmn, rmn)
    return max(root.val, lmx, rmx)

def LCA(root, p, q):
    #if root is None:
    #    return None
    if root.val == p.val or root.val == q.val:
        return root
    if root.left is None and root.right is None:
        return None
    llca, rlca = None, None
    if root.left:
        llca = LCA(root.left, p, q)
    if root.right:
        rlca = LCA(root.right, p, q)
    if llca and rlca:
        return root
    if not rlca:
        return llca
    if not llca:
        return rlca

def max_min_path_sum(root):
    if root is None:
        return float('-Inf')
        #return float('Inf')
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(max_min_path_sum(root.left), max_min_path_sum(root.right))
    #return root.val + min(max_min_path_sum(root.left), max_min_path_sum(root.right))

def longest_path(root):
    if root is None:
        return []

    left_list = longest_path(root.left)
    right_list = longest_path(root.right)

    if len(left_list) >= len(right_list):
        left_list.append(root.val)
        return left_list

    if len(left_list) < len(right_list):
        right_list.append(root.val)
        return right_list

def sum_trees(root1, root2, op):
    if root2 is None:
        return root1
    if root1 is None:
        return root2
    root1.data = op(root1.data, root2.data)
    root1.left = sum_trees(root1.left, root2.left)
    root1.right = sum_trees(root1.right, root2.right)
    return root1

def is_BST(root):
    if not root:
        return True
    if root.left and root.left.val > root.val:
        return False
    if root.right and root.right.val < root.val:
        return False
    if not is_BST(root.left) or not is_BST(root.right):
        return False
    return True
def isBST(root):
    if is_BST(root):
        return 'Is BST!'
    else:
        return 'Is NOT BST!'

def treePathsSum(root):
    return treePathsSumUtils(root, 0)

def treePathsSumUtils(root, val):
    if not root:
        return 0
    val = (val * 10 + root.val)
    if not root.left and not root.right:
        return val
    return treePathsSumUtils(root.left, val) + treePathsSumUtils(root.right, val)

def allPathswithSum(root, sum):
    sum_so_far = 0
    path = []
    allPathswithSumUtil(root, sum, sum_so_far, path)

def allPathswithSumUtil(root, sum, sum_so_far, path):
    if not root:
        return
    sum_so_far += root.val
    path.append(root.val)
    print('Print Path:  %s' % path)
    if sum == sum_so_far:
        print('Path found: ', end=" ")
        for elt in path:
            print("%d " % elt, end=' ')
        print()

    if root.left:
        allPathswithSumUtil(root.left, sum, sum_so_far, path)
    if root.right:
        allPathswithSumUtil(root.right, sum, sum_so_far, path)

    path.pop()

def printAllBranchFromRoot(root):
    path, res = [], []
    printAllBranchFromRootUtil(root, path, res)
    return res

def printAllBranchFromRootUtil(root, path, res):
    if not root:
        return []

    path.append(root.val)

    if root.right is None and root.left is None:
        print('Print Path:  %s' % path)
        print()

    if root.left:
        printAllBranchFromRootUtil(root.left, path, res)
    if root.right:
        printAllBranchFromRootUtil(root.right, path, res)
    # remove elt (so to add nxt adj branch's elt)
    path.pop()

      #     /        \
      #   /  \      /  \
      # / \  / \  / \  / \


def construct_string_from_binary_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    res = []

    def preorder(root):
        if not root:
            return
        if not root.left and root.right:
            res.append("()")
        res.append('(')
        res.append(str(root.val))
        preorder(root.left)
        preorder(root.right)
        res.append(")")

    preorder(root)
    print(''.join(res)[1:-1])