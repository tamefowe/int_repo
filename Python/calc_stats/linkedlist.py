class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def printLL(head):
    cur = head
    while cur:
        print('%d ->' % cur.val, end=' ')
        cur = cur.next
    print('None')

def reverse(head):
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def count_nodes(head):
    cur = head
    count = 0
    while cur:
        cur = cur.next
        count += 1
    return count

def get_first_connecting_node(head1, head2):
    #if not head:
    #    return None
    d1 = count_nodes(head1)
    d2 = count_nodes(head2)

    if d1 > d2:
        return getintersection(d1-d2, head1, head2)
    else:
        return getintersection(d2-d1, head2, head1)

def getintersection(d, head1, head2):

    cur1 = head1
    cur2 = head2

    for i in range(d):
        if not cur1:
            return -1
        cur1 = cur1.next
    while cur1 and cur2:
        if cur1 == cur2:
            return cur1.val
        cur1 = cur1.next
        cur2 = cur2.next
    return -1

def isCycle(head):
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print('Cycle exists at %d' % slow.val)
            return True
    return False


def create_list(arr):
    cur, head = None, None
    for a in arr:
        if cur is None:
            head = cur = Node(a)
        else:
            tmp = Node(a)
            cur.next = tmp
            cur = tmp
    return head

def add_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    cur1, cur2, = l1, l2
    sum, carry = 0, 0
    result, cur = None, None
    while cur1 is not None and cur2 is not None:
        val = cur1.val + cur2.val + carry
        sum = val % 10
        carry = val // 10
        tmp = Node(sum)
        if result is None:
            cur = result = tmp

        else:
            cur.next = tmp
            cur = tmp
        cur1 = cur1.next
        cur2 = cur2.next

    while cur1 is not None:
        val = cur1.val + carry
        sum = val % 10
        carry = val // 10
        tmp = Node(sum)
        cur.next = tmp
        cur = tmp
        cur1 = cur1.next

    while cur2 is not None:
        val = cur2.val + carry
        sum = val % 10
        carry = val // 10
        tmp = Node(sum)
        cur.next = tmp
        cur = tmp
        cur2 = cur2.next

    if carry:
        tmp = Node(carry)
        cur.next = tmp

    return result
