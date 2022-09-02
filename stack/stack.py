class Stack:
    def __init__(self):
        self.array = []

    def push(self, e):
        self.array.append(e)

    def pop(self):
        if self.isEmpty(): raise Exception("stack is empty")
        return self.array.pop(-1)

    def peek(self):
        print(self.array[-1])

    def size(self):
        return len(self.array)

    def isEmpty(self):
        return self.size() == 0


if __name__ == '__main__':
    s = Stack()

    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
