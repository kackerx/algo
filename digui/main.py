def sum(array):
    if len(array) == 1: return array[0]

    return array[0] + sum(array[1:])


if __name__ == '__main__':
    res = sum([1, 2, 3, 2, 4])
    print(res)

