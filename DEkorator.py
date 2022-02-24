import time


def decor(func):

    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_stop = time.time()
        delta = time_stop - time_start
        print(f'Result: {result}, time to execute: {delta}')
        return func

    return wrapper


@decor
def multiply(x, y):
    return x * y


if __name__ == '__main__':
    multiply(3, 5)

    multiply('Hello', 3)