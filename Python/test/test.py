

class Node:
    def __int__(self, node=None, value=None):
        self.nextNode = node
        self.value = value

    @property
    def getNode(self):
        return self.nextNode

    #@setNode.setter
    def setNode(self, node):
        self.nextNode = node


def partition(arr, l, r):
    x = arr[r-3]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def run_partition():
    arr = [12, 3, 5, 7, 4, 19, 26]
    n = len(arr)
    k = 3;
    pos = partition(arr, 0, n - 1)
    print('{} {}'.format(pos, arr))

def is_str_all_uniq_chars_data_struct(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c, n in d.items():
        if n > 1:
            return False
    return True


def is_str_all_uniq_chars(s):
    x = 0
    for c in s:
        v = ord(c) - ord('a')
        y = (1 << v)
        z = x & y
        print('{} - {} - {} - {}'.format(c, v, y, z))
        if z > 0:
            return False
        x = x | y
        print('{}'.format(x))
    return True

def run_is_str_all_uniq_chars():
    str = 'malgorithm'
    return is_str_all_uniq_chars(str)


def remove_duplicates(s):
    if s is None:
        return None
    if len(s) < 2:
        return s

    ss = s[0]
    tail = 1
    for i in range(1, len(s)):
        for j in range(0, tail):
            if s[i] == s[j]:
                break
        if j == tail:
            ss += s[i]
            tail += 1
        else:
            ss += s[i]
    return ss

def run_remove_duplicates():
    s = 'malgorithm'
    return remove_duplicates(s)


def is_anagram(s1, s2):
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False
    d = {}
    for c in s1:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s2:
        if c in d:
            d[c] -= 1
        else:
            return False
    for n in d.values():
        if n:
            return False
    return True


def is_palindrome(s):
    if  s is None or not s.isalnum():
        return False
    i,j = 0, len(s)-1
    while (i < j):
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def run_is_palindrome():
    s = 'writetirw'
    print('{} {} palindrome'.format(s, 'is' if is_palindrome(s) else 'is not'))


def run_is_anagram():
    s1 = 'write'
    s2 = 'etwi'
    print('{} {} {}'.format(s1, 'is' if is_anagram(s1, s2) else 'is not', s2))


def is_substring(ss, s):
    if s is None or ss is None:
        return False
    i = 0
    while i < len(ss):
        j = 0
        while j < len(ss):
            if s[i] != ss[j]:
                return False
            i += 1
            j += 1
        i = j
        print(i)
    return True

def is_rotation(s1, s2):
    s = s2 + s2
    if is_substring(s1, s):
        return True
    return False


def pair_sum(array, sum):
    if len(array) < 2:
        return None
    seen = set()
    output = set()
    for elt in array:
        target = sum - elt
        if target not in seen:
            seen.add(elt)
        else:
            output.add((min(elt, target), max(elt, target)))
    print('\n'.join(['{}'.format(x) for x in output]))


def multiply_matrices(A, B):
    if len(A) != len(B):
        raise Exception("no multiplication possible")
    C = [[] for i in range(len(A))]
    for i, row in enumerate(A):
        for j in range(len(B[0])):
            col = [row[j] for row in B]
            elt = sum([r*c for r, c in zip(row, col)])
            C[i].append(elt)
    return C


if __name__ == "__main__":
    A = [[1, 2, 3],
         [2, 4, 1],
         [5, 1, 1]]
    B = [[0, 1, 3, 2],
         [6, 0, 2, 4],
         [1, 2, 1, 1]]

    C = multiply_matrices(A, B)
    [print('{}'.format(row)) for row in C]
    #s = 'writer'
    #ss = 'iter'
    #print(is_substring(ss, s))
    #run_is_palindrome()
    #run_is_anagram()
    #print(run_remove_duplicates())