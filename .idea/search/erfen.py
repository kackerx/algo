def erfen(arr, target):
    start = 0
    end = len(arr)
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def erfenDi(arr, target, start, end):
    if start > end: return -1
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return erfenDi(arr, target, start, mid - 1)
    else:
        return erfenDi(arr, target, mid + 1, end)


if __name__ == '__main__':
    print(erfenDi([1, 2, 4, 8, 9, 11], 90, 0, 5))
    # print(erfen([1, 2, 4, 8, 9, 11], 2))
