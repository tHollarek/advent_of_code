def read_csv(filename):
    with open(filename, newline='') as file:
        data = [line for line in file]
    return data


def print_result(day, part, result):
    print(f"The result for day {day}, part {part} is:  {result}")


def print_if_verbose(text, verbose):
    if verbose:
        print(text)

