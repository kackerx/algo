def merge(array, l, r):
    """ 返回排序好的array """
    if l == r: return array

    mid = (l + r) // 2
    left = merge(array, l, mid)
    right = merge(array, mid + 1, r)

    return left + right


