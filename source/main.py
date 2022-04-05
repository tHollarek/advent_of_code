from source.days.day1 import day_1
from source.days.day3 import day_3_1
from source.utils import print_result

if __name__ == '__main__':
    #day_1('input/day1.csv')
    day3_result = day_3_1('source/input/day3.csv', verbose=True)
    print_result(day=3, part=1, result=day3_result[0])
    print_result(day=3, part=2, result=day3_result[1])
