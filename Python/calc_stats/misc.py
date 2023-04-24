def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    best_sum = 0  # or: float('-inf')
    best_start = best_end = 0  # or: None
    current_sum, current_start = 0, 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            # Start a new sequence at the current element
            current_start = current_end
            current_sum = x
        else:
            # Extend the existing sequence with the current element
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = current_end #+ 1  # the +1 is to make 'best_end' exclusive

    return best_sum, best_start, best_end

# dynamic programming

def fibonacci(n, cache):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    #return fibonacci(n-1) + fibonacci(n-2)
    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]

# start top left  corner, how many paths to get to right bottom with down and right moves
# put it into a tree
#                   (m, n)
#          down   /       \ right
#           (m-1, n)       (m, n-1)
#       ..............................


def num_of_path_in_grid(m, n, cache): # From 2^m+n to m*n time complexity, m+n space
    if (m, n) in cache:
        return cache[(m, n)]

    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    cache[(m, n)] = num_of_path_in_grid(m-1, n, cache) + num_of_path_in_grid(m, n-1, cache)
    return cache[(m, n)]

def canSum(target, array):
    if target < 0:
        return False
    if target == 0:
        return True
    for elt in array:
        if elt <= target:
            new_target = target - elt
            if canSum(new_target, [a for a in array if a <= new_target]):
               return True
    return False

# brute force
# m = target sum
# n = array  length
# tree with target sum m as the root and n elts of array as edges. O(n^m)
# with appending to array of results m times (can be worse case 1+1+..+1 m times)
# so O(n^m*m) time complexity
# space complexity O(m)

def howSumBrutForce(target, array ):

    if target < 0:
        return None
    if target == 0:
        return []
    for elt in array:
        new_target = target - elt
        new_target_res = howSumBrutForce(new_target, array)
        if new_target_res is not None:
            return new_target_res + [elt]
    return None
# memoization
# time complexity O(n*m*m)
# space complexity O(m*m)

def howSumMemoized(target, array, cache):
    if target in cache:
        return cache[target]

    if target < 0:
        #return False
        return None
    if target == 0:
        return []
        #return True
    for elt in array:
        #if elt <= target:
        #    new_target = target - elt
        #    if canSum(new_target, [a for a in array if a <= new_target]):
        #       return True
        new_target = target - elt
        new_target_result = howSumMemoized(new_target, array, cache)
        if new_target_result is not None:
            cache[target] = new_target_result + [elt]
            return cache[target]
    cache[target] = None
    return None
    #return False

# sum with includes the least amount of elts in array
# m = target sum
# n = array  length
# time complexity O(n^m*m)
# space complexity O(m^2)
def bestSum(target, array):
    if target < 0:
        return None
    if target == 0:
        return []
    shortestcomb = None
    for elt in array:
        new_target = target - elt
        new_target_res = bestSum(new_target, array)
        if new_target_res is not None:
            comb = new_target_res + [elt]
            if shortestcomb is None or len(comb) < len(shortestcomb):
                shortestcomb = comb

    return shortestcomb

def bestSumMemoized(target, array, cache):
    if target in cache:
        return cache[target]

    if target < 0:
        return None
    if target == 0:
        return []

    shortestcomb = None
    for elt in array:
        new_target = target - elt
        new_target_res = bestSumMemoized(new_target, array, cache)
        if new_target_res is not None:
            comb = new_target_res + [elt]
            if shortestcomb is None or len(comb) < len(shortestcomb):
                shortestcomb = comb
    cache[target] = shortestcomb
    return shortestcomb

# time O(n^m*m)
# height of the tree O(m)
def canConstruct(targetWord, words):
    if targetWord == '':
        return True
    for prefix in words:
        if targetWord.find(prefix) == 0:
            suffix = targetWord.replace(prefix, '', 1)
            if canConstruct(suffix, words):
                return True
    return False

def canConstructMemoized(targetWord, words, cache):
    if targetWord in cache:
        return cache[targetWord]

    if targetWord == '':
        return True
    for prefix in words:
        if targetWord.find(prefix) == 0:
            suffix = targetWord.replace(prefix, '', 1)
            if canConstructMemoized(suffix, words, cache):
                cache[targetWord] = True
                return True
    cache[targetWord] = False
    return False
#  Brute force  ---> Memoized
# time O(n^m*m) ---> O(n*m*m)
# space O(m^2)  ---> O(m*m)
def countConstruct(target, words, cache):
    if target in cache:
        return cache[target]
    if target == '':
        return 1
    total_count = 0
    for word in words:
        if target.find(word) == 0:
            suffix = target.replace(word, '', 1)
            num_ways_target = countConstruct(suffix, words, cache)
            total_count += num_ways_target
    cache[target] = total_count
    return total_count
# time O(n^m)
# space O(m)

def allConstruct(target, words, cache):
    if target in cache:
        return cache[target]

    if target == '':
        return [[]]
    res = []
    for word in words:
        if target.find(word) == 0:
            suffix = target.replace(word, '', 1)
            suffix_res = allConstruct(suffix, words, cache)
            target_res = [[word] + s for s in suffix_res]
            res += [s for s in target_res]
    cache[target] = res
    return res


# Tabulation
def fib_tab(n):
    arr = [0] * (n+1)
    # for i, elt in enumerate(arr):
    #     if i == 1:
    #         arr[i] = 1
    #     if i > 1:
    #         arr[i] += arr[i-1]
    #         if (i+1) <= n:
    #             arr[i+1] += arr[i-1]
    # return arr[-1]
    arr[1] = 1
    for i in range(n + 1):
        if (i+1) <= n:
            arr[i + 1] += arr[i]
        if (i+2) <= n:
            arr[i + 2] += arr[i]
    return arr[n]

def gridTraveler(R, C):
    grid = []
    for r in range(R+1):
        tmp = [0] * (C+1)
        grid.append(tmp)

    grid[1][1] = 1
    for r in range(R + 1):
        for c in range(C + 1):
            if (r + 1) <= R:
                grid[r + 1][c] += grid[r][c]
            if (c + 1) <= C:
                grid[r][c + 1] += grid[r][c]
    return grid[R][C]

def validParentheses(word):
    if len(word) % 2:
        return False
    stack = []
    for c in word:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        elif c == ')' and stack and stack[-1] == '(':
            stack.pop()
        elif c == '}' and stack and stack[-1] == '{':
            stack.pop()
        elif c == ']' and stack and stack[-1] == '[':
            stack.pop()
    return not stack

def removeParantheses(word):

    stack = []
    for i, c in enumerate(word):
        if c == '(':
            stack.append((c, i))
        elif c == ')':
            if stack and stack[-1][0] == '(':
                stack.pop()
            if not stack:
                return word[:i] + '' + word[i+1:]
    if stack:
        return word.replace(stack[-1], '')
    else:
        return word


