

def buble_sort(arr=None):
    if not arr:
        return list()

    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    l = [56, 78, 2, 34, 54]
    print(buble_sort(l))
    print(buble_sort())