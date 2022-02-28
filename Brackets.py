

def is_proper_brackets_v2(some_string):
    """
    complexity 0(n)
    """

    if not some_string:
        return 1

    stack_like_list = []
    for char in some_string:
        if char in LEFTS.keys():
            stack_like_list.append(char)
        elif char in RIGHTS.keys():
            if not stack_like_list:
                return 1
            pair = stack_like_list.pop(-1)
            if pair != RIGHTS[char]:
                return 1
            else:
                continue

    if __name__ == '__main__':
        for pattern in PATTERNS:
            print(not is_proper_brackets_v2(pattern))