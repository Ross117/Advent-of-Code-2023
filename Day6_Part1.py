import functools
import unittest
import doctest

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [[int(val) for val in val.split(' ') if val.isdigit()] for val in input]

def beats_record(hold_time, race_time, distance):
    '''Usage examples:
    >>> beats_record(10, 20, 10)
    True
    >>> beats_record(1, 20, 80)
    False
    '''


    if hold_time * (race_time - hold_time) > distance:
        return True

    return False

ways = []

for ind, race_time in enumerate(input_cleaned[0]):

    beats_record_counter = 0
    distance = input_cleaned[1][ind]

    for hold_time in range(1, race_time):
        if beats_record(hold_time, race_time, distance):
            beats_record_counter += 1

    ways.append(beats_record_counter)

print(functools.reduce(lambda a, b: a*b, ways))

class TestBeatsRecord(unittest.TestCase):

    def test_beats_record(self):
        self.assertTrue(beats_record(10, 20, 10), 'Should be True')
        self.assertFalse(beats_record(1, 20, 80), 'Should be False')


unittest.main()
