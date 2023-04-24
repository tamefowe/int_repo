def angleClock(hour, minutes):
    minAngle = minutes * 6  # 360 deg/hr for the min hand. 60 mins/hr. 360/60 = 6 deg
    hrAngle = (hour * 30) - (minutes * 0.5) # 12 hrs for 360 deg. 30 deg/hr. 30 deg/hr. 60 mins/hr. 30/60 deg/ min
    angle = abs(minAngle - hrAngle)
    return min(360-angle, angle)


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_data(self, data):
        self.head = Node(data[0])
        node = self.head
        for i in data[1:]:
            node.next = Node(i)
            node = node.next

    def printll(self):
        tmp = self.head
        s = ''
        while tmp is not None:
            s += '%d -> ' % tmp.value
            tmp = tmp.next
        s += 'None'
        print(s)


def mergeLists(head1, head2):

    curr = Node(0)  # store the result

    tail = curr  # store last node

    while True:

        if not head1:
            tail.next = head2
            break
        if not head2:
            tail.next = head1
            break

        if head1.value < head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    return curr.next




def reverse_ll(ll):

    prev = None
    curr = ll.head

    while curr is not None:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    ll.head = prev


def binary_search(data, target):
    start = 0
    end = len(data)-1
    while start < end:
        mid = (end + start) // 2
        x = data[mid]
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start += 1
        else:
            end += 1
    return -1

def count(ll):
    temp = ll
    cnt = 0
    while temp is not None:
        temp = temp.next
        cnt += 1
    return cnt


def padding(ll, n):
    for i in range(n):
        node = Node(0)
        node.next = ll
        ll = node
    return ll


def add(l1, l2):
    carry, sum = 0, 0
    head = Node(0)
    curr = head

    while l1 is not None or l2 is not None or sum > 0:
        if l1 is not None:
            sum += l1.value
            l1 = l1.next

        if l2 is not None:
            sum += l2.value
            l2 = l2.next

        # compute carry & sum
        carry = sum // 10
        sum = sum % 10

        # add sum to result and move/update curr
        curr.next = Node(sum)
        curr = curr.next

        # reset sum & carry
        sum = carry
        carry = 0

    return head.next


import math


def is_prime(a, b):
    for num in range(a, b+1):
        sqnum = int(math.sqrt(num))
        if all(num % i != 0 for i in range(2, sqnum + 1)):
            print(num)


def first_Not_Repeating_Char(word):
    counts = 26*[0]

    for c in word:
        idx = ord(c)-ord('a')
        counts[idx] += 1

    for c in word:
        idx = ord(c)-ord('a')
        if counts[idx] == 1:
            return c

    return 'No 1st repeating char'


def first_not_repeating_char(word):
    for c in word:
        if word.index(c) == word.rindex(c):
            return c
    return 'NRC'

from collections import defaultdict

def firstDuplicate(l):
    out = defaultdict(list)
    id = None
    c = None
    for i, e in enumerate(l):
        out[e].append(i)

    for k, v in out.items():
        if len(v) > 1:
            if not id:
                id = v[-1]
                c = k
                continue
            if id > v[-1]:
                id = v[-1]
                c = k
    return c if c else -1


def rotateMatrix (m):
    # transpose matrix
    N = len(m)

    for i in range(N):
        for j in range(i, N):
            if i != j:
                tmp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = tmp

    print(m)

    # flip horizontally
    for i in range(N):
        for j in range(N//2):
            tmp = m[i][j]
            m[i][j] = m[i][N-1-j]
            m[i][N-1-j] = tmp

    print(m)

def test():
    data1 = [4, 7, 1, 3]
    data2 = [5, 9, 1, 7]

    ll1 = LinkedList()
    ll1.add_data(data1)
    ll1.printll()

    ll2 = LinkedList()
    ll2.add_data(data2)
    ll2.printll()

    ll = LinkedList()
    ll.head = add(ll1.head, ll2.head)
    ll.printll()

    #ll1.head = mergeLists(ll1.head, ll2.head)
    #ll1.printll()


if __name__ == '__main__':
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    rotateMatrix(m)
    #l = [1,4,5,6,7,8]
    #for i in range(len(l)-1,0,-2):
    #    print(i)
    #ans = first_not_repeating_char(word='aaabcccdeeeef')
    #l = [1,2, 1,2,3,3]
    #ans = firstDuplicate(l)
    #print(ans)
