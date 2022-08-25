def maopao(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]: arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)


if __name__ == '__main__':
    maopao([1, 3, 5, 2, 6, 9, 7, 10])
