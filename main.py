import random

test_measures = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
random_test = random.sample(range(0, 1000), 10)


def read_csv(filename):
    with open(filename, newline='') as file:
        data = [int(i) for i in file.read().strip().split("\n")]
    return data


def count_increases(int_list):
    increases = 0
    for i in range(len(int_list)-1):
        if int_list[i] < int_list[i+1]:
            increases += 1
    return increases


def count_increases_sliding_window(int_list):
    increases = 0
    for i in range(len(int_list)-3):
        sum1 = int_list[i] + int_list[i+1] + int_list[i+2]
        sum2 = int_list[i+1] + int_list[i+2] + int_list[i+3]
        if sum1 < sum2:
            increases += 1
    return increases


def count_increases_sliding_window_alt(int_list):
    window_increases = [(measure1+measure2+measure3) < (measure2 + measure3 + measure4)
                        for measure1, measure2, measure3, measure4
                        in zip(int_list, int_list[1:], int_list[2:], int_list[3:])]
    return window_increases.count(True)


if __name__ == '__main__':
    # depth_measures = test_measures
    # depth_measures = random_test
    depth_measures = read_csv('input.csv')
    print(f"There are {len(depth_measures)} depth measures "
          f"starting with {depth_measures[0]} "
          f"and ending at {depth_measures[-1]}")
    num_increases = count_increases(depth_measures)
    print(f"There are {num_increases} increases in the depth measures")
    num_increases_sliding_window = count_increases_sliding_window(depth_measures)
    print(f"There are {num_increases_sliding_window} increases in the sliding window depth measures")
