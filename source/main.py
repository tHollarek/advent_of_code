from source.days.day1 import day_1
from source.days.day3 import day_3
from source.utils import print_result

if __name__ == '__main__':
    day1_result = day_1('source/input/day1.csv')
    print_result(day=1, result=day1_result)
    day3_result = day_3('source/input/day3.csv', verbose=True)
    print_result(day=3, result=day3_result)
