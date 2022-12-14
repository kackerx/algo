class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    head = Node()

    def __str__(self):
        ret = "L"
        temp = self.head
        while temp.next:
            ret += "->" + str(temp.next.data)
            temp = temp.next
        return ret

    def reversed_r(self):
        self.head.next = self.__reversed_r(self.head.next)

    def __reversed_r(self, node):
        """返回该节点翻转后的链表"""
        if node.next is None: return node

        node.next = self.__reversed_r(node.next)
        return node

    def reverse(self):
        """
        1, reverseHead = Node()
        2, 遍历原链表, 每个节点放到reverseHead的next
        3, head.next = reverseHead.next
        """
        new_head = Node()
        cur = self.head.next
        next = None

        while cur:
            # 保存下一个节点
            next = cur.next

            # cur的下一个节点指向新链表最前端
            cur.next = new_head.next

            new_head.next = cur

            # cur后移
            cur = next

        self.head.next = new_head.next


if __name__ == '__main__':
    n0 = Node(data=0)
    n1 = Node(data=1)
    n2 = Node(data=2)
    n3 = Node(data=3)

    n0.next = n1
    n1.next = n2
    n2.next = n3

    l = Linkedlist()
    l.head.next = n0
    print(l)

    # l.reverse()
    # print(l)

    l.reversed_r()
    print(l)
