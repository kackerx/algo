def sol(nums, target):
    """ two sum & O(nlogn)
    有序数组, 用二分查找,
    """
    for i, v in enumerate(nums):
        target_index = erfen(nums[i + 1:], target - v)
        if target_index == -1:
            continue
        else:
            return i, target_index + 1 + i


def erfen(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def sol_1(nums, target):
    """two sum & O(n)
    双指针对撞
    """
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return i, j
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    return None


if __name__ == '__main__':
    print(sol_1([2, 7, 11, 15], 10))
