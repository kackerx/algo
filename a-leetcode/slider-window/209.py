def sol(nums, s):
    """ minimum size subarray

    """
    l = 0
    r = -1
    sum = 0
    res = len(nums) + 1  # 长度初始比全部数组长度大, 说明不存在子数组

    while l < len(nums):
        if sum < s and r + 1 < len(nums):
            r += 1
            sum += nums[r]
        else:
            sum -= nums[l]
            l += 1

        if sum >= s:
            res = min(res, r - l + 1)

    if res > len(nums): return 0

    return res


if __name__ == '__main__':
    print(sol([2, 3, 1, 2, 4, 3], 7))
