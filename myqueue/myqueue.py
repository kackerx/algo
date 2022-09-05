class MyQueue:
    INIT_CAPA = 10

    def __init__(self, capacity=INIT_CAPA):
        self.front = 0
        self.rear = 0
        self.array = [None for i in range(capacity)]

    def enqueue(self, e):
        if (self.rear + 1) % len(self.array) == self.front: raise "queue is full"  # 队尾 + 1 % 数组长度 == 队首

        self.array[self.rear] = e
        self.rear = (self.rear + 1) % len(self.array)

    def dequeue(self):
        if self.front == self.rear: raise "queue is empty"  # 头尾相等为空队

        dequeue_element = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        return dequeue_element

    def is_empty(self):
        return self.rear == self.front

    def show(self):
        i = self.front
        while i != self.rear:
            print(self.array[i])
            i = (i + 1) % len(self.array)


if __name__ == '__main__':
    q = MyQueue()
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.dequeue()
    q.dequeue()
    q.show()
