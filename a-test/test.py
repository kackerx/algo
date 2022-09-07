def count(array):
    res = {}
    for i in array:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    print(res)


if __name__ == '__main__':
    count(["a", "a", "b", "c", "d", "b", "d", "d"])
