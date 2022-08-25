a = [
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [2, 0, 1],
]

b = [[], [0, 1, 2]]
b[1][2] = 1


if __name__ == '__main__':
    print(b)

    exit(0)
    for i in a:
        for j in i:
            print(j, end=" ")
        print("\n", end="")

