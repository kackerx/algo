def sol_349(nums1, nums2):
    s = set(nums1)

    res = set()
    for i in nums2:
        if i in s:
            res.add(i)

    return list(res)


def sol_350(nums1, nums2):
    s = set()
    l = []

    for i in nums1:
        if i in nums2:
            l.append(i)
            nums2.remove(i)

    return l


def sol_350_2(nums1, nums2):
    count = {}
    for i in nums1: count[i] = count.get(i, 0) + 1

    l = []
    for i in nums2:
        if i in count:
            l.append(i)
            count[i] = count[i] - 1
            if count[i] == 0:
                count.pop(i)

    return l


if __name__ == '__main__':
    sol_350_2([4, 9, 5, 4], [9, 4, 9, 8, 4, 4])
