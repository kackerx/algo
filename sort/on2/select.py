def select(arr):
    for i in range(len(arr) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]: max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    print(arr)


def select_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


if __name__ == '__main__':
    select_sort([1, 8, 7, 5, 6, 10, 9, 12])
