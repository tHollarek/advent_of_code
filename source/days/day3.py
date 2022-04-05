from source.utils import read_csv, print_if_verbose
import numpy as np


def parse(string_list):
    single_bits = [list(line) for line in string_list]
    data = np.array(single_bits).T
    return data


def bits(input_data, comparison):
    common_bits = []
    for bits_row in input_data:
        bits_list = list(bits_row)
        count_of_ones = bits_list.count('1')
        if comparison(count_of_ones, len(bits_list) / 2):
            common_bit = '1'
        else:
            common_bit = '0'
        common_bits.append(common_bit)
    return common_bits


def most_common_bits(input_data):
    result = bits(input_data, lambda a, b: a > b)
    return result


def least_common_bits(input_data):
    result = bits(input_data, lambda a, b: a < b)
    return result


def decimal(binary_gamma_rate):
    binary_gamma_rate_string = ''.join(binary_gamma_rate)
    return int(binary_gamma_rate_string, 2)


def find_value(input_data, comparison):
    search_space = input_data
    for i in range(len(search_space[0])):
        most_common_bit = bits(parse(search_space), comparison)[i]
        search_space = [bit for bit in search_space if bit[i] == most_common_bit]
        if len(search_space) == 1:
            break
    return list(search_space[0])


def find_oxygen_generator_value(input_data):
    result = find_value(input_data, lambda a, b: a >= b)
    return result


def find_co2_scrubber_value(input_data):
    result = find_value(input_data, lambda a, b: a < b)
    return result


def day_3(input_path, verbose=False):
    raw_input = read_csv(input_path)
    input_data = parse(raw_input)
    print_if_verbose(f"Successfully parsed input data:\n{input_data}", verbose)

    binary_gamma_rate = most_common_bits(input_data)
    print_if_verbose(f"Binary gamma rate: {binary_gamma_rate}", verbose)
    gamma_rate = decimal(binary_gamma_rate)
    print_if_verbose(f"Gamma rate: {gamma_rate}", verbose)

    binary_epsilon_rate = least_common_bits(input_data)
    print_if_verbose(f"Binary epsilon rate: {binary_epsilon_rate}", verbose)
    epsilon_rate = decimal(binary_epsilon_rate)
    print_if_verbose(f"Epsilon rate: {epsilon_rate}", verbose)

    result_part_1 = gamma_rate * epsilon_rate

    binary_oxygen_generator_rating = find_oxygen_generator_value(raw_input)
    print_if_verbose(f"Binary oxygen generator rating: {binary_oxygen_generator_rating}", verbose)
    oxygen_generator_rating = decimal(binary_oxygen_generator_rating)
    print_if_verbose(f"oxygen generator rating: {oxygen_generator_rating}", verbose)
    binary_co2_scrubber_rating = find_co2_scrubber_value(raw_input)
    print_if_verbose(f"Binary CO2 scrubber rating: {binary_co2_scrubber_rating}", verbose)
    co2_scrubber_rating = decimal(binary_co2_scrubber_rating)
    print_if_verbose(f"CO2 scrubber rating: {co2_scrubber_rating}", verbose)

    result_part_2 = oxygen_generator_rating * co2_scrubber_rating
    return result_part_1, result_part_2
