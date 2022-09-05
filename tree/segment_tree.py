from copy import copy


class SegmentTree:
    def __init__(self, arr):
        self.data = copy(arr)
        self.tree = []

        self.build_segment_tree(0, 0, self.size() - 1)

    def build_segment_tree(self, tree_index, l, r):
        """ 在tree_index位置创建表示区间[l...r]的线段树 """
        if l == r:
            self.tree[tree_index] = self.data[l]
            return



    def size(self):
        return len(self.data)

    def get(self, index):
        if 0 > index >= self.size(): raise Exception("index is error")
        return self.data[index]

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return index * 2 + 2


