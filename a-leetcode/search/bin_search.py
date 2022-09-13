def bin_search(arr, target):
    l = 0
    r = len(arr) - 1  # 确认边界问题, 要搜索的范围是[l...r], 覆盖整个arr
    while l <= r:  # 查询条件的边界, 如果l == r, 搜索区间依然有效
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            r = mid - 1  # 查询条件的边界[l..mid - 1]
        else:
            l = mid + 1
    return -1


def r_bin_search(arr, l, r, target):
    if l > r: return -1

    mid = (l + r) // 2
    if arr[mid] == target: return mid

    if arr[mid] > target:
        return r_bin_search(arr, l, mid - 1, target)
    else:
        return r_bin_search(arr, mid + 1, r, target)


if __name__ == '__main__':
    res = r_bin_search([0, 1, 2, 3, 4, 5], 0, 5, 7)
    print(res)
