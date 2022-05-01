from source.days.day1 import day_1
from source.days.day3 import day_3
from source.days.day4 import day_4
from source.days.day5 import day_5
from source.utils import print_result


if __name__ == '__main__':
    day1_result = day_1('source/input/day1.csv')
    print_result(day=1, result=day1_result)
    day3_result = day_3('source/input/day3.csv')
    print_result(day=3, result=day3_result)
    day4_result = day_4('source/input/day4.csv')
    print_result(day=4, result=day4_result)
    day5_result = day_5('source/input/day5.csv')
    print_result(day=5, result=day5_result)
