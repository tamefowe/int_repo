# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def printLL(head):
    cur = head
    while cur:
        print("%d ->" % cur.val, end=' ')  # Press Ctrl+F8 to toggle the breakpoint.
        cur = cur.next
    print('None')


def count_nodes(head):
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    return count


def find_intersection (head1, head2):
    count1 = count_nodes(head1)
    count2 = count_nodes(head2)
    if count1 > count2:
        return get_intersection(count1 - count2, head1, head2)
    else:
        return get_intersection(count2 - count1, head2, head1)


def get_intersection(count, head1, head2):
    cur1 = head1
    cur2 = head2
    for i in range(count):
        if not cur1:
            return -1
        cur1 = cur1.next
    while cur1 and cur2:
        if cur1 == cur2:
            return cur1.val
        cur1 = cur1.next
        cur2 = cur2.next
    return -1


def reverse(x):
        mult = -1 if x < 0 else 1
        res = 0
        x *= mult
        while x > 0:
            res *= 10
            rem = x % 10
            x -= rem
            x /= 10
            res += rem

        return int(res * mult)


def lengthOfLongestSubstring(s):
    if not s:
        return 0

    if len(s) == 1:
        return 1
    maxlen = 0
    lenword = 1
    elt = s[0]

    lenwords = {}

    for c in s[1:]:
        if c not in elt:
            elt += c
            lenword += 1
        else:
            lenwords[elt] = lenword
            maxlen = max(maxlen, lenword)
            elt = c
            lenword = 1

    print(f"{lenwords}")
    return maxlen


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #x = 120123
    #print(f"reverse({x}) = {reverse(x)}")
    s = 'pwwkew'
    print(f"{lengthOfLongestSubstring(s)}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
