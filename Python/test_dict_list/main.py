
from collections import defaultdict
from functools import reduce
class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return '(%d, %d)' % (self._x, self._y)

    def __add__(self, other):
        x = self._x + other.x()
        y = self._y + other.y()
        return Point(x, y)


def calc(func, d, value):
    return func([k for k, v in d.items() if v == value])

def calc_(func, d, d2, key):
    return func([k for k, v in d.items() if d[k] == d2[key]])

def printResult(func, d, value):
    print("The %s key for value %s is %s" % (func.__name__, str(value), calc(func, d, value)))

import heapq
# n+ k(log(n))

class HeapSolution():
    def find_kth_smallest(self, input: [int], k: int) ->int:
        heapq.heapify(input)
        for _ in range(k-1):
            heapq.heappop(input)
        return input[0]

    def find_kth_largest(self, input: [int], k: int) -> int:
        # heapify all the nums, save in max-heap
        # python only support min-heap, so put negative value to save in max - heap
        heap = [-x for x in input]
        heapq.heapify(heap)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

    def test(self):
        input = [12, 25, 19, 100, -10, 15, -3, -8, 9, 23, 8, 43, 59, 10, -34, 54]
        sinput = sorted(input)
        rinput = sorted(input, reverse=True)
        z, w = sinput[6], rinput[6]
        k = 7
        x = self.find_kth_smallest(input, k)
        y = self.find_kth_largest(input, k)
        print('%dth smallest/largest elts = (%d, %d)' % (k, x, y))
        print()

class BinarySearchSolution:
    # binary search
    # O(n)
    def dfs(self, matrix: [[int]], mid: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        col = m - 1
        sum = 0
        for row in range(n):
            elt = matrix[row][col]
            while col >= 0 and elt > mid:
                col -= 1

            sum += (col + 1)

        return sum

    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        left = matrix[0][0]
        right = matrix[n - 1][m - 1]
        ans = -1

        # O(max-min) time
        while left <= right:
            mid = (left + right) // 2
            val = self.dfs(matrix, mid)
            if val >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def test(self):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        k = 8
        ans = self.kthSmallest(matrix, k)
        print(ans)

    # O(log(len(A)) + log(len(B)) time
    def kth_elt_2_sorted_arrays(self, A, B, k):
        def func(l1, r1, l2, r2, k):
            if l1 > r1:
                return B[l2 + k - 1]
            if l2 > r2:
                return A[l1 + k - 1]

            m1 = (r1 + l1) // 2
            m2 = (r2 + l2) // 2
            kc = (m1 - l1 + 1) + (m2 - l2 + 1)
            if kc <= k:  # increase kc
                if A[m1] < B[m2]:  #ans not in  A[l1: m1+1]
                    l1 = m1 + 1
                    k = k - (m1 - l1 + 1)
                    return func(l1, r1, l2, r2, k)
                else:  # ans not in B[l2: m2+1]
                    l2 = m2 + 1
                    k = k - (m2 - l2 + 1)
                    return func(l1, r1, l2, r2, k)
            else:   # decrease kc
                if A[m1] < B[m2]:  #ans not in B[m2: r2+1]
                    r2 = m2 - 1
                    return func(l1, r1, l2, r2, k)
                    # don't decrease k
                else:  # ans not in A[m1: r1+1]
                    r1 = m1 - 1
                    # don't decrease k
                    return func(l1, r1, l2, r2, k)

        return func(0, len(A)-1, 0, len(B)-1, k)

    def test_(self):
        arr1 = [100, 112, 256, 349, 770]
        arr2 = [72, 86, 113, 119, 265, 445, 892]
        k = 7
        ans = self.kth_elt_2_sorted_arrays(arr1, arr2, k)
        print('%d' % ans)

def trans(word):
    s = ''
    letter = None
    for c in word:
        if not c.isdigit():
            letter = [c]
        if c.isdigit():
            s += ''.join(letter * int(c))
    return s

def invtrans(word):
    cur = word[0]
    cnt = 1
    s = ''
    for i, c in enumerate(word):
        if i != 0:
            if c == cur:
                cnt += 1
            else:
                s += (cur + str(cnt))
                cur = c
                cnt = 1
    return s + cur + str(cnt)

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
def visitGrap(src, func):
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

    seen = set()
    queue = [src]

    while queue:
        cur = queue.pop(0)
        seen.add(cur)
        for node in graph[cur]:
            if node not in seen:
                queue.append(node)
                seen.add(cur)

    l = list(seen)
    res = list(filter(func, l))
    #res = reduce(func,l)
    res = visitGrap(src=0, func=lambda x: x % 2 == 0)
    return res

def get_groups(arr):
    arr.sort() # nlogn Time
    min_ = arr[0]
    n_groups = 1
    i, n = 1, len(arr)
    while i < n:
        if min_ > arr[i] or arr[i] > (min_ + 4):
            min_ = arr[i]
            n_groups += 1
        i += 1

    return n_groups


def getmax(arr, x):
    mx = arr[x]
    mx_i = 0

    for i in range(x, len(arr)):
        e = arr[i]
        if mx < e:
            mx = e
            mx_i = i

    tmp = arr[x]
    arr[x] = mx
    arr[mx_i] = tmp
    return arr


def largestPermutation(k, arr):
    # Write your code here
    arr = getmax(arr, 0)

    if k < 2:
        return arr
    else:
        while k > 1:
            arr = getmax(arr, k - 1)
            k -= 1
    return arr

def count_comps():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2],
        9 : []
    }
    seen = set()
    count = 0
    for node in graph:
        if explore_nodes(graph, node, seen):
            count += 1
    return count

def explore_nodes(graph, node,seen):
    if node in seen:
        return False
    seen.add(node)

    for neighbor in graph[node]:
        if neighbor not in seen:
            explore_nodes(graph, neighbor, seen)
    return True


if __name__ == '__main__':
    #k = 2
    #arr = [1,2,3,4]
    #ngs = largestPermutation(k, arr)
    ngs = count_comps()

    print(ngs)