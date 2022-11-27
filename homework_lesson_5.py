import random


def retry(attempts=5, desired_value=None):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            nonlocal attempts
            nonlocal desired_value
            result = func(*args, **kwargs)
            if not result == desired_value:
                attempts = attempts - 1
                if attempts > 0:
                    inner_wrapper(*args, **kwargs)
                else:
                    print("The desired value wasn't found")
            else: 
                return result

        return inner_wrapper

    return wrapper


@retry(desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value_2():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values_2(choices, size=2):
    return random.choices(choices, k=size)


def print_a_rows(side, amount):
    row = '*' + ' '*(side-2) + '*'
    print(row)
    amount = amount - 1
    if not amount == 0:
        print_a_rows(side, amount)


def print_square(side):
    if side == 1:
        print("*")
    elif side == 2:
        print("**")
        print("**")
    else:
        print('*'*side)
        print_a_rows(side, side-2)
        print('*'*side)


if __name__ == '__main__':
    get_random_value()
    get_random_value_2()
    get_random_values([1, 2, 3, 4])
    get_random_values_2([1, 2, 3, 4], 3)
    get_random_values([1, 2, 3, 4], size=1)
    print_square(4)
