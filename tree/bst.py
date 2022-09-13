from myqueue.myqueue import MyQueue
from stack.stack import Stack


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    """
    bin search tree: 二分搜索树
    """

    def __init__(self, node=None):
        self.root = node
        self.size = 0

    def add(self, e):
        """添加操作"""
        self.root = self.add_node(self.root, e)

    def add_node(self, node, e):
        """
        函数的意义: 返回添加了这个e的node为根节点的子树
        """
        if node is None:
            self.size += 1
            return Node(e)
        if node.data == e: return  # 重复的值去除

        if e < node.data:
            node.left = self.add_node(node.left, e)  # 递归操作和终止条件结合完成函数的意义
        elif e > node.data:
            node.right = self.add_node(node.right, e)

        return node

    def pre_search(self, e):
        return self.pre_search_node(self.root, e)

    def pre_search_node(self, node, e):
        """node为根的二叉树是否包含e"""
        if not node: return False  # 遍历结束
        if node.data == e: return True  # 找到目标

        return self.pre_search_node(node.left, e) or self.pre_search_node(node.right, e)

    def pre_order_traveral(self, node):
        if not node: return
        print(node.data)
        self.pre_order_traveral(node.left)
        self.pre_order_traveral(node.right)  # 每个节点, 三个点, 前中后, 访问三次, node.left为空, return回来又访问该node状态的函数栈, right同理

    def infix_order_traveral(self, node):
        if not node: return
        self.infix_order_traveral(node.left)
        print(node.data)
        self.infix_order_traveral(node.right)

    def post_order_traveral(self, node):
        if not node: return
        self.post_order_traveral(node.left)
        self.post_order_traveral(node.right)
        print(node.data)

    def pre_order_nr(self):
        """非递归前序遍历"""
        s = Stack()
        s.push(self.root)
        while not s.isEmpty():
            node = s.pop()
            print(node.data)  # 先访问该节点, 然后左右孩子入栈
            if node.right: s.push(node.right)
            if node.left: s.push(node.left)

    def level_order(self):
        q = MyQueue()
        q.enqueue(self.root)
        while not q.is_empty():
            node = q.dequeue()
            print(node.data)
            if node.left: q.enqueue(node.left)
            if node.right: q.enqueue(node.right)

    def del_min(self):
        ret = self.min_node_search(self.root)  # 首先找到最小节点, 后返回
        self.root = self.del_min_node(self.root)
        return ret

    def del_min_node(self, node):
        """函数定义: 删除以node为根节点的最小的节点, 返回删除后新的根"""
        if node.left is None:
            self.size -= 1
            right_node = node.right
            node.right = None
            return right_node

        node.left = self.del_min_node(node.left)
        return node

    def del_any(self, e):
        self.root = self.del_any_node(self.root, e)

    def del_any_node(self, node, e):
        """删除node为根的树中的e节点, 返回删除后的根"""

        if node is None: return None

        # 要删除的节点小于当前节点, 左递归, 大于, 右递归
        if e < node.data:
            node.left = self.del_any_node(node.left, e)
            return node

        if e > node.data:
            node.right = self.del_any_node(node.right, e)
            return node

        # 等于当前节点, 左边为空返回右树, 右边为空, 返回左树
        if node.left is None:
            self.size -= 1
            right_node = node.right
            node.right = None
            return right_node

        if node.right is None:
            self.size -= 1
            left_node = node.left
            node.left = None
            return left_node

        # 要删除的当前节点, 左右子树都不为空
        successor = self.min_node_search(node.right)
        successor.right = self.del_min_node(node.right)
        successor.left = node.left

        node.left = node.right = None
        return successor

    def min_node(self):
        """获取最小节点"""
        return self.min_node_search(self.root)

    def min_node_search(self, node):
        if node.left is None: return node
        return self.min_node_search(node.left)

    def max_node(self):
        """获取最大节点"""
        return self.max_node_search(self.root)

    def max_node_search(self, node):
        if node.right is None: return node
        return self.max_node_search(node.right)

    def invert_tree(self, node):
        if node is None: return

        # 翻转左子树, 右子树, 交换翻转后的左右子树
        self.invert_tree(node.left)
        self.invert_tree(node.right)
        node.left, node.right = node.right, node.left

    def is_symmetric(self, node):
        if node is None: return

        if node.left.data == node.right.data:
            if self.is_symmetric(node.left) and self.is_symmetric(node.right):
                return True
        else:
            return False

    def path_sum(self, node, target):
        if node is None: return False

        if node.left is None and node.right is None: return node.data == target  # 如果是叶子节点的话, 叶子节点的值要等于target

        return self.path_sum(node.left, target - node.data) or self.path_sum(node.right, target - node.data)  # 递归判断左右子树

    def max_deep(self):
        return self.__max_deep(self.root)

    def __max_deep(self, node):
        if node is None: return 0

        return max(self.__max_deep(node.left), self.__max_deep(node.right)) + 1

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    # root = Node(1)
    # node2 = Node(2)
    # node3 = Node(3)
    # node4 = Node(4)
    # node5 = Node(5)
    # node6 = Node(6)

    t = BST()
    t.add(3)
    t.add(1)
    t.add(2)
    t.add(4)
    t.add(5)
    t.add(6)

    # t.pre_order_traveral(t.root)
    # t.pre_order_nr()
    t.level_order()
    print(t.max_deep())
