from heap.max_heap import MaxHeap


class PriorityQueue:
    def __init__(self):
        self.max_heap = MaxHeap()

    def size(self):
        return self.max_heap.size()

    def is_empty(self):
        return self.max_heap.is_empty()

    def get_front(self):
        return self.max_heap.get_front()

    def enqueue(self, e):
        self.max_heap.add(e)

    def dequeue(self):
        return self.max_heap.extract_max()
