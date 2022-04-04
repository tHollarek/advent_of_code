
import unittest

from source.days.day1 import count_increases, count_increases_sliding_window

test_measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


class Day1Tests(unittest.TestCase):

    def test_increases(self):
        result = count_increases(test_measures)
        self.assertEqual(result, 7)

    def test_increases_sliding_window(self):
        result = count_increases_sliding_window(test_measures)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
