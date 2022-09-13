def sort(array, l, r):
    """ 返回排序好的array """
    if l == r: return

    mid = (l + r) // 2

    sort(array, l, mid)
    sort(array, mid + 1, r)

    merge(array, l, mid, r)


def merge(arr, L, mid, R):
    temp = [None for i in arr]
    k = 0

    l = L
    r = mid + 1
    while l <= mid and r <= R:
        if arr[l] < arr[r]:
            temp[k] = arr[l]
            k += 1
            l += 1
        else:
            temp[k] = arr[r]
            k += 1
            r += 1

    while l <= mid:
        temp[k] = arr[l]
        k += 1
        l += 1

    while r <= R:
        temp[k] = arr[r]
        k += 1
        r += 1

    # arr[L:R+1] = temp[0:k]
    k = L
    while k <= R:
        arr[k] = temp[k-L]
        k += 1


# k == L
# while k <= R:
#     arr[k] = temp[k-L]
#     k += 1

if __name__ == '__main__':
    a = [0, 2, 9, 8, 7, 5, 10, 29, 3, 100, 1]
    sort(a, 0, len(a) - 1)
    print(a)
