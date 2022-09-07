class NumArray_303:
    """
    范围区间的和
    $ sum数组存nums前i位的和
    sum[0] = 0, sum[1] = nums[0...], sum[2] = nums[0...1], sum[3] = nums[0...2](nums前3个数)
    """

    def __init__(self, nums):
        sum_len = len(nums) + 1
        self.sum = [None for i in range(sum_len)]
        self.sum[0] = 0
        for i in range(1, self.sum):
            self.sum[i] = self.sum[i - 1] + nums[i - 1]

        self.sum_range(0, 2)

    def sum_range(self, i, j):
        return self.sum[j + 1] - self.sum[i]


if __name__ == '__main__':
    n = NumArray_303([-2, 0, 3, -5, 2, -1])
    res = n.sum_range(0, 2)
    print(res)
