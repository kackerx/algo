def sol_357(s):
    res: list = [0 for i in range(26)]

    for i in s:
        res[ord(i) - 97] += 1

    for i in s:
        if res[ord(i) - 97] == 1:
            print(i)

    # for i, v in enumerate(res):
    #     if v == 1:
    #         return chr(i + 97)


if __name__ == '__main__':
    print(sol_357("aalleetcode"))
