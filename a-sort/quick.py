def quick(array):
    if len(array) < 1: return array

    left = []
    right = []
    target = array[0]
    for i in array[1:]:
        if i < target:
            left.append(i)
        else:
            right.append(i)

    return quick(left) + [target] + quick(right)


if __name__ == '__main__':
    a = [0, 2, 9, 8, 7, 5, 10, 29, 3, 100, 1]
    print(quick(a))

    # quicksort(a)
    # print(a)
