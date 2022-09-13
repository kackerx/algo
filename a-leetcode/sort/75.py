def sol(nums):
    """ sort color: [0000111222]
    三路排序
    """
    zero = -1  # [0..zero]
    two = len(nums)  # [two..len-1], 初始两个集中元素数都应为零, 所以范围肯定是不合法

    i = 0
    while i < two:
        if nums[i] == 1:
            i += 1
        elif nums[i] == 2:
            two -= 1
            nums[i], nums[two] = nums[two], nums[i]
        else:
            zero += 1
            nums[zero], nums[i] = nums[i], nums[zero]
            i += 1

    print(nums)

if __name__ == '__main__':
    sol([0, 2, 1, 1, 2, 0, 0, 2, 2, 1, 1])

