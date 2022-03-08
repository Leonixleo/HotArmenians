def count_two(n):
    counter = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            counter = counter + 1
        else:
            return False, None
    return True, counter

if __name__ == '__main__':
    print('n count_two ', count_two(128))
