"""
合并双链表
"""


class Node:
    def __init__(self, data=-1):
        self.data = data
        self.next = None


def sol_888(node1, node2):
    p1 = node1.next
    p2 = node2.next

    dump_node = Node()
    p = dump_node

    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next

    while p1 != None:
        p.next = p1
        p1 = p1.next

    while p2 != None:
        p.next = p2
        p1 = p2.next

    print(dump_node)


if __name__ == '__main__':
    node1 = Node()
    node1.next = Node(1)
    node1.next.next = Node(3)
    node1.next.next.next = Node(7)

    node2 = Node()
    node2.next = Node(2)
    node2.next.next = Node(4)
    node2.next.next.next = Node(5)

    sol_888(node1, node2)
