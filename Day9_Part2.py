import unittest
import functools

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input: list[str] = file.read().split('\n')

input_cleaned: list[list[int]] = [[int(val) for val in val.split(' ')] for val in input]


def get_difference(seq: list[int]) -> list[int]:
    '''
    Return a list containing the differences in value between each element
    of a given sequence.
    '''

    diff_seq: list[int] = []

    for ind, num in enumerate(seq):
        if ind < len(seq) - 1:
            diff_seq.append(seq[ind + 1] - num)

    return diff_seq


def get_nxt_val(diff_hist: list[int]) -> int:
    '''
    Return a new value at the beginning of a sequence based on a given pattern of
    differences between values.
   
    '''

    return functools.reduce(lambda a, b: b - a, reversed(diff_hist))


nxt_vals: list[int] = []

for val in input_cleaned:

    history: list[int] = [val[0]]

    diff: list[int] = get_difference(val)
    history.append(diff[0])

    while not all(val == 0 for val in diff):
        diff = get_difference(diff)
        history.append(diff[0])

    nxt_vals.append(get_nxt_val(history))

answer: int = sum(nxt_vals)
print(answer)


class TestSolution(unittest.TestCase):

    def test_get_difference(self):
        self.assertEqual(get_difference([0, 3, 6, 9, 12, 15]), [3, 3, 3, 3, 3])

    def test_get_nxt_val(self):
        self.assertEqual(get_nxt_val([10, 3, 0, 2, 0]), 5)

unittest.main()
