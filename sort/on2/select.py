def select(arr):
    for i in range(len(arr) - 1):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]: max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

    print(arr)


def test(data):
    [print(i) for i in data]


if __name__ == '__main__':
    select([1, 3, 5, 2, 6, 9, 7, 10])
