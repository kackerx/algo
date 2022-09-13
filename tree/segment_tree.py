from copy import copy


class SegmentTree:
    def __init__(self, arr):
        self.data = copy(arr)
        self.tree = [None for i in range(len(arr) * 4)]

        self.build_segment_tree(0, 0, self.size() - 1)

    def build_segment_tree(self, tree_index, l, r):
        """ 在tree_index位置创建表示区间[l...r]的线段树, 给该index赋值 """
        if l == r:
            self.tree[tree_index] = self.data[l]
            return

        left_tree_index = self.left_child(tree_index)
        right_tree_index = self.right_child(tree_index)
        mid = (l + r) // 2

        self.build_segment_tree(left_tree_index, l, mid)
        self.build_segment_tree(right_tree_index, mid + 1, r)

        # self.tree[tree_index] = self.merge(self.tree[left_tree_index], self.tree[right_tree_index], lambda a, b: a + b)  # 节点的左右孩子的值确定了,  处理方式是
        self.tree[tree_index] = self.tree[left_tree_index] + self.tree[right_tree_index]

    def query(self, query_l, query_r):
        return self.__query(0, 0, self.size() - 1, query_l, query_r)

    def __query(self, tree_index, l, r, query_l, query_r):
        """ 节点index的线段树在[l...r]范围内的区间[query_r...query_r]的值 """
        if l == query_l and r == query_r: return self.tree[tree_index]

        left_tree_index = self.left_child(tree_index)
        right_tree_index = self.right_child(tree_index)
        mid = (l + r) // 2

        if query_l >= mid + 1: return self.__query(right_tree_index, mid + 1, r, query_l, query_r)
        if query_r <= mid: return self.__query(left_tree_index, l, mid, query_l, query_r)

        left_res = self.__query(left_tree_index, l, mid, query_l, mid)
        right_res = self.__query(right_tree_index, mid + 1, r, mid + 1, query_r)
        return left_res + right_res

    def size(self):
        return len(self.data)

    def get(self, index):
        if 0 > index >= self.size(): raise Exception("index is error")
        return self.data[index]

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return index * 2 + 2

    def merge(self, a, b, f):
        return f(a, b)


if __name__ == '__main__':
    s = SegmentTree([-2, 0, 3, -5, 2, -1])
    res = s.query(0, 5)
    print(res)
    ...
