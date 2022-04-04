from source.utils import read_csv, print_result, print_if_verbose


def count_increases(int_list):
    increases = 0
    for i in range(len(int_list) - 1):
        if int_list[i] < int_list[i + 1]:
            increases += 1
    return increases


def count_increases_sliding_window(int_list):
    increases = 0
    for i in range(len(int_list) - 3):
        sum1 = int_list[i] + int_list[i + 1] + int_list[i + 2]
        sum2 = int_list[i + 1] + int_list[i + 2] + int_list[i + 3]
        if sum1 < sum2:
            increases += 1
    return increases


def count_increases_sliding_window_alt(int_list):
    window_increases = [(measure1 + measure2 + measure3) < (measure2 + measure3 + measure4)
                        for measure1, measure2, measure3, measure4
                        in zip(int_list, int_list[1:], int_list[2:], int_list[3:])]
    return window_increases.count(True)


def parse(input):
    data = [int(i) for i in input.read().strip().split("\n")]
    return


def day_1(input_path, verbose=False):
    raw_input = read_csv(input_path)
    depth_measures = parse(raw_input)
    print_if_verbose(f"There are {len(depth_measures)} depth measures "
                     f"starting with {depth_measures[0]} "
                     f"and ending at {depth_measures[-1]}",
                     verbose)

    num_increases = count_increases(depth_measures)
    print_if_verbose(f"There are {num_increases} increases in the depth measures", verbose)

    num_increases_sliding_window = count_increases_sliding_window(depth_measures)
    print_if_verbose(f"There are {num_increases_sliding_window} increases in the sliding window depth measures", verbose)
    print_result(day=1, part=1, result=num_increases)
    print_result(day=1, part=2, result=num_increases_sliding_window)
