def sol(nums, k):
    s = set()
    for i, v in enumerate(nums):
        if v in s:
            return True

        s.add(v)
        if len(s) == k + 1:
            s.remove(nums[i - k])

    return False


def sol_1(nums, k):
    l = 0
    r = 0

    window = set()
    while r < len(nums):
        c = nums[r]
        r += 1
        if c in window: return True

        window.add(c)

        if len(window) == k + 1:
            window.remove(nums[l])
            l += 1
    return False


def slider(s, t):
    """
    - 什么时候扩大窗口, 如何更新窗口 * 不满足要求时候扩大
    - 什么时候缩小窗口, 如何更新窗口 * 满足要求后缩小
    - 结果是在扩大时更新, 还是缩小时更新 * 要的最小子串, 就在缩小窗口的时候更新
    """
    l = 0
    r = 0

    window = {}
    need = {}
    vaild = 0
    for i in t: need[i] = need.get(i, 0) + 1

    res = len(s) + 1
    start = 0

    # print(f"window {l}...{r}")

    while r < len(s):
        c = s[r]
        r += 1

        if need.get(c):
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                vaild += 1

        # while all([window.get(i, 0) >= need[i] for i in need]):  # 符合条件, 缩小窗口
        while vaild == len(need):  # 符合条件, 缩小窗口
            # 更新结果
            if r - l < res:
                start = l
                res = r - l

            d = s[l]

            if need.get(d):
                if window[d] == need[d]: vaild -= 1
                window[d] = window.get(d) - 1
                if window[d] == 0: window.pop(d)

            l += 1

    return "" if res == len(s) + 1 else s[start:start + res]


if __name__ == '__main__':
    # print(slider("ADOBECODEBANC", "ABC"))
    print(sol_1([1, 5, 2, 1, 3, 4], 2))
