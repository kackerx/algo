def sol(s: str):
    """ 最长不重复子串 & 滑动窗口
    """
    l = 0
    r = -1
    res = 0
    freq = [0 for i in range(256)]

    while l < len(s):
        if r + 1 < len(s) and freq[ord(s[r + 1])] == 0:
            r += 1
            freq[ord(s[r])] += 1
        else:
            freq[ord(s[l])] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


if __name__ == '__main__':
    print(sol("kackerkres"))
