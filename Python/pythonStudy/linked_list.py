class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_ll(head):
    cur = head
    while cur:
        print(f"{cur.val}", end=' -> ')
        cur = cur.next
    print('None')


def linked_list_cycle(head):
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def run_longest_streak():
    a = Node(5)
    b = Node(5)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    longest_streak(a)
    print()


def run_remove_node():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    insert_node(a, 'v', 3)
    print_ll(c)


def run_add_lists():
    a1 = Node(9)
    a2 = Node(9)
    a3 = Node(9)
    a1.next = a2
    a2.next = a3
    # 9 -> 9 -> 9

    b1 = Node(6)
    l = add_lists(a1, b1)
    print_ll(l)


def add_lists(head_1, head_2):
    cur_1, cur_2 = head_1, head_2
    carry = 0
    head = tail = None

    while cur_1 and cur_2:
        sum = cur_1.val + cur_2.val + carry
        carry = sum // 10
        tmp = Node(sum % 10)
        if not head and not tail:
            head = tail = tmp
        else:
            tail.next = tmp
            tail = tail.next

        cur_1 = cur_1.next
        cur_2 = cur_2.next

    if cur_1:
        while cur_1:
            sum = cur_1.val + carry
            carry = sum // 10
            val = sum % 10
            tail.next = Node(val)
            tail = tail.next
            cur_1 = cur_1.next

        if carry:
            tail.next = Node(carry)
            carry = 0

    if cur_2:
        while cur_2:
            sum = cur_2.val + carry
            carry = sum // 10
            val = sum % 10
            tail.next = Node(val)
            tail = tail.next
            cur_2 = cur_2.next

        if carry:
            tail.next = Node(carry)
            carry = 0

    if carry:
        tail.next = Node(carry)

    return head


def run_create_linked_list():
    values = ["h", "e", "y"]
    head = create_linked_list(values)
    print_ll(head)


def create_linked_list(values):
    head = tail = None
    for i,v in enumerate(values):
        if i == 0:
            head = tail = Node(v)
        else:
            tail.next = Node(v)
            tail = tail.next
    return head


def run_insert_node():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    insert_node(a, 'x', 2)


def insert_node(head, value, index, count = 0):
    if not head:
        return
    if index == 0:
        tmp = Node(value)
        tmp.next = head
        return tmp
    if count == index - 1:
        tmp = head.next
        head.next = Node(value)
        head.next.next = tmp
        return
    insert_node(head.next, value, index, count+1)

    return head


def remove_node(head, target_val):
    start = cur = head
    prev = None

    while cur:
        if cur.val == target_val:
            if not prev:
                cur = cur.next
                start = cur
            else:
                prev.next = prev.next.next
            return start
        else:
            prev = cur
            cur = cur.next

    return start


def longest_streak(head):
    cur = head
    s = cur.val
    cur = cur.next
    occurs = []
    occur = 1
    while cur:
        if s == cur.val:
            occur += 1
        else:
            occurs.append((s, occur))
            s = cur.val
            occur = 1
        if not cur.next:
            occurs.append((cur.val, occur))
        cur = cur.next
    tmp = sorted(occurs, key=lambda x: x[1])

    if tmp:
        return tmp[-1][0]


def run_zipper_lists():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    head = zipper_lists(a, x)
    head = merge_lists(a, x)
    print_ll(head)


def run_merge_lists():
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t

    head = merge_lists(a, q)
    print_ll(head)


def merge_lists(head_1, head_2):
    if not head_1:
        return head_2

    if not head_2:
        return head_1

    head = tail = Node(-1)
    cur_1 = head_1
    cur_2 = head_2

    while cur_1 and cur_2:
        if cur_1.val < cur_2.val:
            tail.next = cur_1
            tail = cur_1
            cur_1 = cur_1.next
        else:
            tail.next = cur_2
            tail = cur_2
            cur_2 = cur_2.next

    if cur_1:
        tail.next = cur_1

    if cur_2:
        tail.next = cur_2

    head = head.next
    return head


def zipper_lists(head_1, head_2):
    if not head_1:
        return head_2
    if not head_2:
        return head_1
    head = tail = head_1
    head_1 = head_1.next
    n = 1

    while head_1 and head_2:
        if n % 2:
            tail.next = head_2
            tail = head_2
            head_2 = head_2.next
        else:
            tail.next = head_1
            tail = head_1
            head_1 = head_1.next
        n += 1

    if head_1:
        tail.next = head_1

    if head_2:
        tail.next = head_2

    return head
