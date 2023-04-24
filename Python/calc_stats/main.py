from Graph import get_adj, graph, dbfs, bfs, hasPath_bfs, hasPath_dfs, \
    hasPath_undirectedcyclic, count_connected_cmps, largest_cmp, longest_path_graph, shortest_path, island_count, minimum_island, isCyclic
from Tree import count_nodes, sum_tree, max_min_tree, LCA, max_min_path_sum, longest_path, isBST, treePathsSum, allPathswithSum,printAllBranchFromRoot
from misc import max_subarray

def test_graph():
    #g = get_adj(graph)
    #src, dst = 'j', 'm'
    #if hasPath_undirectedcyclic(g, src, dst, isbfs=True):
    #    print('valid path from %s to %s' % (src, dst))
    #print()

    #count = count_connected_cmps()
    #print(count)

    #size = largest_cmp()
    #print(size)

    #src, dst = 'w', 'z'
    #sp = shortest_path(src, dst)
    #print(sp)

    #cnt = island_count()
    #print(cnt)

    #size = minimum_island()
    #print(size)

    #if isCyclic():
    #    print("Cycle exist")
    #else:
    #    print("Cycle does not exist")
    n1, d1 = longest_path_graph(0)
    n2, d2 = longest_path_graph(n1)
    print('Distance from %d to %d with value %d' % (n1, n2, d2))


def test_tree():
    from Tree import a, d, e, \
b, g, \
f, h
    root = a
    #res = LCA(root, f, h)
    #res = max_min_path_sum(root)
    #res = longest_path(root)
    #res = isBST(root)
    #res = treePathsSum(root)
    #allPathswithSum(root, 10)
    res = printAllBranchFromRoot(root)
    print(res)

def test_misc():
    #numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    #best_sum, best_start, best_end = max_subarray(numbers)
    #print('best_sum: %d, best_start: %d, best_end: %d' % (best_sum, best_start, best_end))

    #from misc import fibonacci

    #print(fibonacci(6))
    #print(fibonacci(7))
    #print(fibonacci(8))
    #print(fibonacci(50))

    #from misc import num_of_path_in_grid
    #mns = [[100, 110], [3, 3], [18, 18]]
    #for m, n in mns:
    #    cache = {}
    #    num_paths = num_of_path_in_grid(m, n, cache)
    #    print('There are %d paths from m: %d to n: %d' % (num_paths, m, n))

    # from misc import canSum
    # target_arrays = [
    #                 (7, [2, 3]),
    #                  (7, [5, 3, 4, 7]),
    #                  (7, [2, 4]),
    #                  (8, [2, 3, 5]),
    #                  (300, [7, 14])
    #   ]
    # for target, array in target_arrays:
    #     cache = {}
    #     ar = canSum(target, array, cache)
    #     print('sum %d in %s' % (target, ar))
        #if canSum(target, array):
       #     print('sum %d in %s' % (target, array))
        #else:
        #    print('sum %d NOT in %s' % (target, array))

    # from misc import bestSumMemoized
    # target_arrays = [
    #     (7, [5, 3, 4, 7]), (8, [2, 3, 5]), (8, [1, 4, 5]), (100, [1, 2, 5, 25])
    # ]
    #
    # for target, array in target_arrays:
    #     cache = {}
    #     ar = bestSumMemoized(target, array, cache)
    #     print('sum %d in %s' % (target, ar))

    from misc import canConstructMemoized, countConstruct, allConstruct, gridTraveler
    # target_word_words = [('purple', ['purp', 'p', 'ur', 'le', 'purpl']),
    #                      ('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']),
    #                      ('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']),
    #                      ('enterapotentpot',['a', 'p', 'ent', 'enter', 'ot', 'o', 't']),
    #                      ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e',
    #                                                                   'ee',
    #                                                                   'eee',
    #                                                                   'eeee',
    #                                                                   'eeeee',
    #                                                                   'eeeeee'])
    #                                              ]
    # for target_word, words in target_word_words:
    #     cache = {}
    #     #if canConstructMemoized(target_word, words, cache):
    #     #    print('target_word %s can be constructed from words in %s' % (target_word, words))
    #     #else:
    #     #    print('target_word %s can NOT be constructed from words in %s' % (target_word, words))
    #     #count = countConstruct(target_word, words, cache)
    #     #print('%d way(s) to construct target word: %s from array %s ' % (count, target_word, words))
    #     res = allConstruct(target_word, words, cache)
    #     print(res)

    # from misc import fib_tab
    # targets = [6, 7, 8, 50]
    # for target in targets:
    #     r = fib_tab(target)
    #     print('fib(%d) = %d' % (target, r))
    RCs = [
        #(1, 1),
        #(2, 3),
        #(3, 2),
        (3, 3),
        #(18, 18)
    ]
    for R, C in RCs:
        res = gridTraveler(R, C)
        print('(%d, %d) : %d' % (R, C, res))

def test():
    from misc import validParentheses
    words = [
        '()', '()[]{}', '(]', '([)]', '{([[[((({{[]}})))]]])}'
    ]
    for word in words:
        if validParentheses(word):
            print('%s is valid' % word)
        else:
            print('%s is NOT valid' % word)

def test_linkedlist():
    from linkedlist import create_list, add_lists, printLL
    arr1 = [2, 4, 3]  #[9] * 7
    arr2 = [5, 6, 4]  #[9] * 4
    l1 = create_list(arr1)
    l2 = create_list(arr2)
    printLL(l1)
    print('+              ')
    printLL(l2)
    res = add_lists(l1, l2)
    printLL(res)


def get_ric_with_no_year_code(ric):
    last_digit_str = ric[-1]
    if last_digit_str.isdigit():
        return ric.replace(last_digit_str, '')
    return ric


def get_ric_with_no_month_code(ric):
    last_char = ric[-1]
    if last_char.isalpha() and last_char.isupper():
        return ric.replace(last_char, '')
    return ric


def extractRoot(ric):
    if len(ric) < 3:
        return ric

    if ric[-2:].isdigit() and ric[-3].isalpha() and ric[-3].isupper():
        return ric[:-3]

    if ric[-1].isdigit() and ric[-2].isalpha() and ric[-2].isupper():
        return ric[:-2]
    return ric

def minion_game(string):
    vowels = ['A','E','I','O','U']
    kevin_results = {}
    stuart_results = {}
    for i,s in enumerate(string):
        word = string[i:]
        l = len(word)
        if s in vowels:
            for j in range(l):
                w =word[:(j+1)]
                kevin_results[w] = get_count(string,w)
        if s not in vowels:
            for j in range(l):
                w =word[:(j+1)]
                stuart_results[w] = get_count(string, w)
    print(kevin_results)
    Kevin_score = sum(kevin_results.values())
    Stuart_score = sum(stuart_results.values())
    if Kevin_score > Stuart_score:
        print(f"Kevin {Kevin_score}")
    else:
        print(f"Stuart {Stuart_score}")


def get_count(str, pattern):
    count = 0
    flag = True
    start = 0
    while flag:
        a = str.find(pattern, start)  # find() returns -1 if the word is not found,
        # start i the starting index from the search starts(default value is 0)
        if a == -1:  # if pattern not found set flag to False
            flag = False
        else:  # if word is found increase count and set starting index to a+1
            count += 1
            start = a + 1
    return count

from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    start = 0
    end = k
    while start < n:
        word = string[start:end]
        print("".join(OrderedDict.fromkeys(word)))
        print(word)
        start += k
        end += k

def t(s):
    l = 1
    c = s[0]
    res = ''
    for n in s[1:]:
        if c == n:
            l += 1
        if c != n:
            res += f"({l}, {c}) "
            l = 1
            c = n
    res += f"({l}, {c})"
    return res

def get_occur(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    res = sorted(d.items(), key=lambda x: x[0]) #, reverse=True)
    res = sorted(res, key=lambda x: x[1], reverse=True)
    for x in res[:3]:
        print(f"{x[0]} {x[1]}")

def triangle_quest(n):
    for i in range(1,int(n)+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
        from itertools import chain
        m = int(''.join([str(k) for k in chain(range(1, i), range(i, i+1), reversed(range(1, i)))]))
        if isinstance(m, int):
            print(f"{m} is int")


def prob_to_find_char_in_K_elts_from_N_elts(s,  K):
    from itertools import product
    N = len(s)
    idx = [i for i, c in enumerate(s) if 'a' == c]
    # All Possible unique K size combinations till N
    tmp = list(product(range(N), repeat=K))
    d = {}
    for tup in tmp:
        d[tuple(sorted(tup))] = 0
    d = list(d.keys())
    prob = len([t for t in d for i in idx if i in t]) / len(d)


import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        self.real += no.real
        self.imaginary += no.imaginary
        return Complex(self.real, self.imaginary)

    def __sub__(self, no):
        self.real -= no.real
        self.imaginary -= no.imaginary
        return Complex(self.real, self.imaginary)

    def __mul__(self, no):
        # (a + ib) (c + id) = (ac - bd) + i(ad + bc)
        self.real = self.real * no.real - self.imaginary * no.imaginary
        self.imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(self.real, self.imaginary)

    def __truediv__(self, no):
        real_dividend = self.real * no.real + self.imaginary * no.imaginary
        imag_dividend = no.real * self.imaginary - self.real * no.imaginary
        divisor = no.real * no.real + no.imaginary * no.imaginary
        self.real = real_dividend / divisor
        self.imaginary = imag_dividend / divisor
        return Complex(self.real, self.imaginary)

    def mod(self):
        return Complex(math.sqrt(self.real * self.real + self.imaginary * self.imaginary), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


def validate_credit_card_numbers():
    credit_card_numbers = [
        '4253625879615786',
        '4424424424442444',
        '5122-2368-7954-3214',
        '42536258796157867',  # 17 digits in card number → Invalid
        '4424444424442444',  # Consecutive digits are repeating 4 or more times → Invalid
        '5122-2368-7954 - 3214',  # Separators other than '-' are used → Invalid
        '44244x4424442444',  # Contains non digit characters → Invalid
        '0525362587961578'

    ]
    return [number for number in credit_card_numbers if validate(number)]


def validate(number):
    import re
    patterns = [
        r'^\d{4}-\d{4}-\d{4}-\d{4}$',   # may have digits in groups of 4 separated by hyphen "-"
        r'\d{16}',                      # contains exactly 16 digits. Just digits [0-9]
        r'^(4|5|6).*$',                 # first digit should be 4,5,6
        r'^.*(\d)\1\1\1+.*$'            # must NOT have 4 or more consecutively repeated digits
    ]
    compiled_patterns = [re.compile(pat) for pat in patterns]
    if not re.match(compiled_patterns[2], number) or re.search(compiled_patterns[-1], number):
        return False
    if not re.match(compiled_patterns[0], number) and not re.match(compiled_patterns[1], number):
        return False
    return True

def main():
    c = map(float, '2 1'.split())
    d = map(float, '5 6'.split())
    x = Complex(*c)
    y = Complex(*d)
    z = x+y

    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None





if __name__ == '__main__':
    construct_string_from_binary_tree()
