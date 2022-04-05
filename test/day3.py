import unittest

from source.days.day3 import most_common_bits, decimal, least_common_bits, parse, find_oxygen_generator_value, \
    find_co2_scrubber_value

test_input = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]


class Day3Tests(unittest.TestCase):
    def test_gamma_rate(self):
        input_data = parse(test_input)
        binary_gamma_rate = most_common_bits(input_data)
        gamma_rate = decimal(binary_gamma_rate)
        self.assertEqual(['1', '0', '1', '1', '0'], binary_gamma_rate)
        self.assertEqual(22, gamma_rate)

    def test_epsilon_rate(self):
        input_data = parse(test_input)
        binary_epsilon_rate = least_common_bits(input_data)
        epsilon_rate = decimal(binary_epsilon_rate)
        self.assertEqual(['0', '1', '0', '0', '1'], binary_epsilon_rate)
        self.assertEqual(9, epsilon_rate)

    def test_oxygen_generator_rating(self):
        binary_oxygen_generator_rating = find_oxygen_generator_value(test_input)
        oxygen_generator_rating = decimal(binary_oxygen_generator_rating)
        self.assertEqual(['1', '0', '1', '1', '1'], binary_oxygen_generator_rating)
        self.assertEqual(23, oxygen_generator_rating)

    def test_co2_scrubber_rating(self):
        binary_co2_scrubber_rating = find_co2_scrubber_value(test_input)
        co2_scrubber_rating = decimal(binary_co2_scrubber_rating)
        self.assertEqual(['0', '1', '0', '1', '0'], binary_co2_scrubber_rating)
        self.assertEqual(10, co2_scrubber_rating)


if __name__ == '__main__':
    unittest.main()
