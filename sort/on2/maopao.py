def maopao(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)


def maopao_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


if __name__ == "__main__":
    maopao_sort([1, 8, 7, 6, 4, 9, 10, 3])
