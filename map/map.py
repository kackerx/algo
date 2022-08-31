def count():
    a = ["wo", "wo", "shi", "k", "b", "b", "b"]
    ret = {}
    for i in a:
        ret[i] = ret.get(i, 0) + 1

    print(ret)


if __name__ == '__main__':
    count()
