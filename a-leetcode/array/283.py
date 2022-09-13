def sol_283(nums):
    new_nums = []

    for i in nums:
        if i != 0: new_nums.append(i)

    for i, v in enumerate(new_nums):
        nums[i] = new_nums[i]

    for i in range(len(new_nums), len(nums)):
        nums[i] = 0

    print(nums)


def sol_1(nums):
    """ k: 保存当前遍历过的非0元素, [0, k) """
    k = 0
    for i in nums:
        if i != 0:
            nums[k] = i
            k += 1

    for i in range(k, len(nums)):
        nums[i] = 0

    print(nums)


def sol_2(nums):
    """ 发生交换的时候, k永远指向0 """
    k = 0
    for i, v in enumerate(nums):
        if v != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1

    print(nums)

if __name__ == '__main__':
    sol_2([0, 2, 0, 1, 0, 3, 4, 5, 0])
