class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SingleLinkedList:
    head = Node(None)

    def __init__(self):
        self.size = 0

    def get(self, index):
        temp = self.head.next
        for i in range(index):
            temp = temp.next
        return temp.data

    def add_first(self, e):
        ...

    def add_last(self, e):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(e)

    def add(self, index, e):
        temp = self.head

        for i in range(index):
            temp = temp.next

        next = temp.next
        new_node = Node(e)
        temp.next = new_node
        new_node.next = next

    def remove(self, index):
        ...

    def reversed(self):
        cur = self.head.next
        new_head = Node(None)

        while cur:
            next = cur.next
            cur.next = new_head.next
            new_head.next = cur
            cur = next

        self.head.next = new_head.next

    def show(self):
        temp = self.head.next
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    l = SingleLinkedList()
    l.add_last(0)
    l.add_last(1)
    l.add_last(2)
    l.add_last(3)
    l.add_last(4)
    l.show()
    l.reversed()
    print("===")
    l.show()
