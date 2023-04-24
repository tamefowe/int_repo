class Stack(object):

    def __int__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def isEmpty(self):
        return self.list == []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if not self.list:
            return None
        return self.list.pop()


class QueueStack(object):

    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def __len__(self):
        return len(self.inStack) + len(self.outStack)

    def isEmpty(self):
        return self.inStack.isEmpty() and self.outStack.isEmpty()

    def enqueue(self, value):
        self.inStack.push(value)

    def dequeue(self):
        while not self.inStack.isEmpty():
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while not self.outStack.isEmpty():
            self.inStack.push(self.outStack.pop())
        return result


def checkRoute(self, startNode, endNode):
    # TODO
    q = [startNode]
    visited = [startNode]
    found = False
    while q:
        node = q.pop(0)
        for vNode in self.gdict[node]:
            if vNode not in visited:
                if vNode == endNode:
                    found = True
                    break
                else:
                    visited += [vNode]
                    q.append(vNode)
    return found


class BSTNode(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def minimalTree(sortedArray):
    # TODO
    if not sortedArray:
        return None
    if len(sortedArray) == 1:
        return BSTNode(data=sortedArray[0])
    mid = int((sortedArray[0] + sortedArray[-1]) / 2)
    bst = BSTNode(data=mid)
    bst.left = minimalTree(sortedArray[:mid])
    bst.right = minimalTree(sortedArray[mid + 1:])
    return bst


def treeToLinkedList(tree, custDict={}, d=None) -> object:
    if not tree or not d:
        return
    if d not in custDict:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    return custDict


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next is None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    if not tree:
        return 0
    return 1 + max(depth(tree.left), depth(tree.right))


def treeToLinkedList(tree, custDict={}, d=None):
    if not tree:
        return

    if not d:
        d = depth(tree)

    if d not in custDict:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left:
        custDict = treeToLinkedList(tree.left, custDict, d - 1)
    if tree.right:
        custDict = treeToLinkedList(tree.right, custDict, d - 1)
    return custDict


def move_zero_to_end(arr):
    n = len(arr)
    start = 0

    for a in arr:
        if a != 0:
            arr[start] = a
            start += 1
    for end in range(start, n):
        arr[end] = 0


if __name__ == '__main__':
    arr = [0, 0, 5, 0, 0, 0, 1, 0, 2, 0, 4, 0, 5, 0, 1, 0, 0, 0, 0]
    print(len(arr))
    move_zero_to_end(arr)
    print(len(arr))
    print(arr)
