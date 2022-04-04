from source.utils import read_csv
import numpy as np

def parse(input):
    data = np.array(input)
    print(data)


def day_3(input_path, verbose=False):
    raw_input = read_csv(input_path)
    input_data = parse(raw_input)
    print("success: input parsed", verbose)
    binary_gamma_rate = most_common_bits(input_data)
    gamma_rate = decimal(binary_gamma_rate)

    binary_epsilon_rate = least_common_bits(input_data)
    epsilon_rate = decimal(binary_epsilon_rate)

    result = gamma_rate * epsilon_rate

