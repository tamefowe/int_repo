class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def add_two_numbers(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l2

    res = cur = None
    cur1 = l1
    cur2 = l2
    sum, carry = 0, 0
    while cur1 and cur2:
        val = cur1.val + cur2.val + carry
        sum = val % 10
        carry = val // 10
        tmp = Node(sum)
        if not cur:
            res = cur = tmp
        else:
            cur.next = tmp
            cur = cur.next
        cur1 = cur1.next
        cur2 = cur2.next

    while cur1:
        val = cur1.val + carry
        sum = val % 10
        carry = val // 10
        cur.next = Node(sum)
        cur = cur.next
        cur1 = cur1.next

    while cur2:
        val = cur2.val + carry
        sum = val % 10
        carry = val // 10
        cur.next = Node(sum)
        cur = cur.next
        cur2 = cur2.next

    if carry:
        cur.next = Node(carry)

    return res

if __name__ == "__main__":
    pass