class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sol(head):
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre


def sol_1(head):
    dump = ListNode()
    cur = head
    while cur:
        next = cur.next
        cur.next = dump.next
        dump.next = cur
        cur = next
    return dump.next


def __reverseList(node):
    if node.next is None:
        return node

    pre = __reverseList(node.next)
    pre.next = node
    node.next = None

    return node


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head.next is None:
        return head

    node = reverseList(head.next)
    head.next.next = head
    head.next = None

    return node


if __name__ == '__main__':
    head = ListNode()
    head.next = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    res = reverseList(head)
    print(res)
