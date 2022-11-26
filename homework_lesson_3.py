def maximum(num_1, num_2):
    return max(num_1, num_2)


def minimum(num_1, num_2, num_3):
    return min(num_1, num_2, num_3)


def absolute_value(num_abs):
    return abs(num_abs)


def summarize(num_1, num_2):
    print(num_1 + num_2)


def number_symbol(num):
    if num > 0:
        print('This number is positive')
    elif num == 0:
        print('This number equal to zero')
    else:
        print('This number is negative')


if __name__ == '__main__':
    NUMBER_1 = 5
    NUMBER_2 = 10
    NUMBER_3 = 1
    NUMBER_ABS = -7.088

    print(maximum(NUMBER_1, NUMBER_2))
    print(minimum(NUMBER_1, NUMBER_2, NUMBER_3))
    print(absolute_value(NUMBER_ABS))
    summarize(NUMBER_1, NUMBER_2)
    number_symbol(NUMBER_ABS)
