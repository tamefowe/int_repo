# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def reverse_words_order_and_swap_cases(sentence):
    def test(sentence):
        words = sentence.split()[::-1]
        out = []
        for w in words:
            tw = ''
            for l in w:
                if l.isupper():
                    tw += l.lower()
                else:
                    tw += l.upper()
            out += [tw]
        return ' '.join(out)
    sentence = 'aWESOME is cODING'
    return test(sentence)


def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {v: i for i, v in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1

    return swaps


def test_minimunSwaps(numbers):
    def test(numbers):
        len_ = len(numbers)
        swap = 0
        for i in range(len_):
            if i+1 != numbers[i]:
                t = i
                while numbers[t] != i+1:
                    t = t+1
                numbers[i], numbers[t] = numbers[t], numbers[i]
                swap += 1
        return swap
    numbers = [7, 1, 3, 2, 4, 5, 6]
    swap = test(numbers)
    print(swap)

def arrayManipulation(n, queries):
    # Write your code here
    elts = [0]*n
    mx = 0
    for query in queries:
        for i in range(query[0]-1, query[1]):
            elts[i] +=  query[-1]
            if mx < elts[i]:
                mx = elts[i]
    return mx


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 10
    queries = [[1,5,3], [4,8,7], [6,9,1]]
    mx = arrayManipulation(n, queries)
    print(mx)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
