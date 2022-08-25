class MyArray:
    INIT_CAPA = 10

    def __init__(self):
        self.data = [None for i in range(self.INIT_CAPA)]
        # 容量cap
        self.size = 0

    def is_element_index(self, index):
        return 0 <= index < self.size

    def is_position_index(self, index):
        return 0 <= index <= self.size

    def check_element_index(self, index):
        """是否可以存储元素"""
        if not self.is_element_index(index): raise f"{index}: {self.size}, index exception"

    def check_position_index(self, index):
        """是否可以添加元素"""
        if not self.is_position_index(index): raise f"{index}: {self.size}, index exception"

    def is_empty(self):
        return self.size == 0

    def add_last(self, e):
        """末尾添加元素"""
        self.data[self.size] = e
        self.size += 1

    def remove_last(self):
        if self.is_empty(): raise "data is empty"
        remove_ele = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return remove_ele

    def get(self, index):
        self.check_element_index(index)
        return self.data[index]

    def set(self, index, e):
        self.check_element_index(index)
        old_e = self.data[index]
        self.data[index] = e
        return old_e

    def add(self, index, e):
        # 数据搬移
        self.data[index + 1:] = self.data[index:]
        # 赋值
        self.data[index] = e
        self.size += 1

    def remove(self, index):
        self.data[index:] = self.data[index + 1:]
        self.data[self.size - 1] = None
        self.size -= 1

    def resize(self, cap: int):
        """扩容"""
        ...

    def __str__(self):
        s = ""
        for i in self.data:
            if i == 0:
                s += f"{i}"
            else:
                s += f"->{i}"
        return s


if __name__ == "__main__":
    a = MyArray()
    a.add_last(0)
    a.add_last(1)
    a.add_last(2)
    a.add_last(3)
    a.add_last(5)
    a.add(4, 4)
    a.add(4, 7)
    print(a)
    a.remove(4)

    print(a)
    ...
