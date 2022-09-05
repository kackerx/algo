from myarray.myarray import MyArray


class MaxHeap:
    """
    二叉堆事一个完全二叉树
    数组从1开始, 0空, 所以: 数学归纳法
    parent(i) = i / 2 || (i - 1) / 2
    left(i) = 2 * i || 2 * i + 1
    right(i) = 2 * i + 1 ||  2 * i + 2
    """

    def __init__(self, array=None):
        if array:
            self.data = MyArray(array)
            self.heapify()
            return

        self.data = MyArray()

    def size(self):
        return self.data.size

    def is_empty(self):
        return self.data.is_empty()

    def get_front(self):
        return self.data.get(0)

    def parent(self, index):
        """ 父亲节点索引 """
        if index == 0: raise Exception("root node no parent")
        return int((index - 1) / 2)

    def left_child(self, index):
        return index * 2 + 1

    def right_child(self, index):
        return index * 2 + 2

    def add(self, e):
        self.data.add_last(e)
        self.sift_up(self.data.size - 1)

    def sift_up(self, k):
        """ 添加元素到末尾, 然后通过sift up上浮到合适位置 """
        # k位置的值大于他父亲节点的值, 上浮, 直接交换数组索引值
        while k > 0 and self.data.get(k) > self.data.get(self.parent(k)):
            # self.data[k], self.data[self.parent(k)] = self.data.get(self.parent(k)), self.data.get(k)
            self.data.swap(k, self.parent(k))
            k = self.parent(k)

    def extract_max(self):
        """ 返回堆顶, 交换堆尾到顶, 顶部下沉 """
        ret = self.data.get(0)
        self.data.swap(0, self.data.size - 1)
        self.data.remove_last()

        self.sift_down(0)
        return ret

    def sift_down(self, k):
        while self.left_child(k) < self.data.size:  # 如果左右孩子不越界
            j = self.left_child(k)
            if j + 1 < self.data.size and self.data.get(j + 1) > self.data.get(j):  # 如果有右孩子, 且右孩子的值大于左孩子, j为其中较大值的下标
                j = j + 1
            if self.data.get(k) > self.data.get(j): break  # k比两个孩子大

            self.data.swap(k, j)
            k = j

    def replace(self, e):
        """ 取出最大元素, 放入新元素 """
        ret = self.data.get(0)

        self.data.data[0] = e
        self.sift_down(0)

        return ret

    def heapify(self):
        """
        给定任意一个数组, 维护成堆
        - 从最后一个非叶子节点(parent(size - 1))向前遍历, 分别执行sift down操作, 每个节点就落到了该在的位置
        - 最后一个非叶子节点: 最后一个节点的父亲节点
        """
        k = self.parent(self.data.size - 1)
        while k >= 0:
            self.sift_down(k)
            k = k - 1




if __name__ == '__main__':
    array = [0, 5, 2, 7, 18, 8, 10, 9]
    max_heap = MaxHeap(array)
    # max_heap.add(0)
    # max_heap.add(5)
    # max_heap.add(2)
    # max_heap.add(7)
    # max_heap.add(18)
    # max_heap.add(8)
    # max_heap.add(10)
    # max_heap.add(9)


    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
    print(max_heap.extract_max())
