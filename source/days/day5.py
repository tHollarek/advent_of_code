from collections import Counter
from itertools import islice

from source.utils import read_csv, print_if_verbose


def parse_to_coordinates(raw_input):
    coordinates_list = []
    for line in raw_input:
        (start_string, end_string) = line.split(' -> ')
        start = start_string.split(',')
        end = end_string.split(',')
        coordinates_list.append((
            dict(x1=int(start[0]),
                 y1=int(start[1]),
                 x2=int(end[0]),
                 y2=int(end[1]))
        ))
    return coordinates_list


def day_5(input_path, verbose=False):
    raw_input = read_csv(input_path)
    vent_lines = parse_to_coordinates(raw_input)
    print_if_verbose(f"line coordinates with start and end: \n {vent_lines}", verbose)
    horizontal_cloud_positions, all_cloud_positions = find_cloud_positions(vent_lines, verbose)
    print_if_verbose(f"horizontal_cloud_positions: \n {horizontal_cloud_positions}", verbose)
    print_if_verbose(f"all_cloud_positions: \n {all_cloud_positions}", verbose)

    part_1_result = count_toxic_positions(horizontal_cloud_positions, verbose)
    part_2_result = count_toxic_positions(all_cloud_positions, verbose)

    return part_1_result, part_2_result


def find_cloud_positions(vent_lines, verbose):
    horizontal_cloud_positions = []
    all_cloud_positions = []
    for line in vent_lines:
        print_if_verbose(f"current line: {line}", verbose)
        x1 = line['x1']
        y1 = line['y1']
        x2 = line['x2']
        y2 = line['y2']
        # this is a given condition for part1
        if x1 == x2 or y1 == y2:
            print_if_verbose("line is horizontal! Processing...", verbose)
            x_step = 1 if x1 <= x2 else -1
            y_step = 1 if y1 <= y2 else -1
            for x in range(x1, x2 + x_step, x_step):
                for y in range(y1, y2 + y_step, y_step):
                    print_if_verbose(f"x={x}, y={y}", verbose)
                    horizontal_cloud_positions.append((x, y))
                    all_cloud_positions.append((x, y))
        else:
            print_if_verbose("line is diagonal! Processing...", verbose)
            x_step = 1 if x1 <= x2 else -1
            y_step = 1 if y1 <= y2 else -1
            x = x1
            y = y1
            for i in range(abs(x1 - x2) + 1):
                print_if_verbose(f"x={x}, y={y}", verbose)
                all_cloud_positions.append((x, y))
                x += x_step
                y += y_step
    return horizontal_cloud_positions, all_cloud_positions


def count_toxic_positions(all_cloud_positions, verbose):
    cloud_positions_summed = Counter(all_cloud_positions)
    print_if_verbose(f"first 10 summed cloud positions: {list(cloud_positions_summed.items())[:9]}", verbose)
    toxic_cloud_positions = {key: value for key, value in cloud_positions_summed.items() if value > 1}
    print_if_verbose(f"first 10 toxic cloud positions:  {list(toxic_cloud_positions.items())[-9:]}", verbose)
    return toxic_cloud_positions.__len__()
