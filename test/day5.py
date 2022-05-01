import unittest

from source.days.day5 import day_5


class Day5Tests(unittest.TestCase):
    def test_end_to_end(self):
        day5_result = day_5('test_input/day5_test.csv', True)
        self.assertEqual(5, day5_result[0])  # add assertion here


if __name__ == '__main__':
    unittest.main()
