def read_csv(filename):
    with open(filename, newline='') as file:
        data = [line.strip() for line in file]
    return data


def print_result(day, result):
    print(f"The result for day {day}, part 1 is: {result[0]}")
    print(f"The result for day {day}, part 2 is: {result[1]}")


def print_if_verbose(text, verbose):
    if verbose:
        print(text)

