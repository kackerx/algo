from myqueue.myqueue import MyQueue
from stack.stack import Stack


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # 节点默认高度1


class AVL:
    """
    bin search tree: 二分搜索树
    """

    def __init__(self, node=None):
        self.root = node
        self.size = 0

    def add(self, key, value):
        """添加操作"""
        self.root = self.__add(self.root, key, value)

    def __add(self, node, key, value):
        """
        : 返回添加了这个e的node为根节点的子树
        """
        if node is None:
            self.size += 1
            return Node(key, value)
        if node.key == key: return  # 重复的值去除

        if key < node.key:
            node.left = self.__add(node.left, key, value)  # 递归操作和终止条件结合完成函数的意义
        elif key > node.key:
            node.right = self.__add(node.right, key, value)

        # 维护节点高度: 左右子树高度较大者加1
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        # 计算平衡因子: 左右子树高度差大于1的话

        # if abs(self.get_balance_factor(node)) > 1: print("失衡")

        # 维护平衡
        # LL
        if self.get_balance_factor(node) > 1 and self.get_balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # LR: Y的X的的右子树更高, 先左旋, 后右旋
        if self.get_balance_factor(node) > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RR
        if self.get_balance_factor(node) < -1 and self.get_balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # RL: Y的X的的右子树更高, 先左旋, 后右旋
        if self.get_balance_factor(node) < -1 and self.get_balance_factor(node.left) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, y: Node):
        """
                y                             x
               / \                          /  \
              x   t4                       z    y
            /  \        --------->        / \  / \
           z   t3                       t1  t2 t3 t4
          / \
        t1   t2
        """
        x = y.right
        t3 = x.left

        x.left = y
        y.right = t3

        # 维护节点高度, t1234子节点不变, 高度不变
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def right_rotate(self, y: Node):
        """
                y                             x
               / \                          /  \
              x   t4                       z    y
            /  \        --------->        / \  / \
           z   t3                       t1  t2 t3 t4
          / \
        t1   t2
        """
        x = y.left
        t3 = x.right

        x.right = y
        y.left = t3

        # 维护节点高度, t1234子节点不变, 高度不变
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    def get_height(self, node):
        if node is None: return 0
        return node.height

    def get_balance_factor(self, node):
        """ 平衡因子: 左右子树的高度差 """
        if node is None: return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def is_bst(self):
        keys = []
        for i in range(1, len(keys)):
            if keys[i - 1] > keys[i]: return False
        return True

    def in_order(self, node, keys):
        if node is None: return
        self.in_order(self.left)
        keys.append(node.key)
        self.in_order(self.right)

    def is_balanced(self):
        return self.__is_balanced(self.root)

    def __is_balanced(self, node):
        if node is None: return True

        if abs(self.get_balance_factor(node)) > 1: return False

        return self.__is_balanced(self.left) and self.__is_balanced(self.right)

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
        self.root = self.__del_min(self.root)
        return ret

    def __del_min(self, node):
        """函数定义: 删除以node为根节点的最小的节点, 返回删除后新的根"""
        if node.left is None:
            self.size -= 1
            right_node = node.right
            node.right = None
            return right_node

        node.left = self.__del_min(node.left)
        return node

    def remove(self, e):
        self.root = self.__remove(self.root, e)

    def __remove(self, node, e):
        """删除node为根的树中的e节点, 返回删除后的根"""

        if node is None: return None

        # 要删除的节点小于当前节点, 左递归, 大于, 右递归
        if e < node.data:
            node.left = self.__remove(node.left, e)
            retNode = node

        if e > node.data:
            node.right = self.__remove(node.right, e)
            retNode = node

        # 等于当前节点, 左边为空返回右树, 右边为空, 返回左树
        if node.left is None:
            self.size -= 1
            right_node = node.right
            node.right = None
            retNode = right_node

        if node.right is None:
            self.size -= 1
            left_node = node.left
            node.left = None
            retNode = left_node

        # 要删除的当前节点, 左右子树都不为空
        successor = self.min_node_search(node.right)
        successor.right = self.__del_min(node.right)
        successor.left = node.left

        retNode = successor

        node.left = node.right = None

        # 维护节点高度: 左右子树高度较大者加1
        node.height = max(self.get_height(retNode.left), self.get_height(retNode.right)) + 1

        # 计算平衡因子: 左右子树高度差大于1的话

        # if abs(self.get_balance_factor(node)) > 1: print("失衡")

        # 维护平衡
        # LL
        if self.get_balance_factor(retNode) > 1 and self.get_balance_factor(retNode.left) >= 0:
            return self.right_rotate(retNode)

        # LR: Y的X的的右子树更高, 先左旋, 后右旋
        if self.get_balance_factor(retNode) > 1 and self.get_balance_factor(retNode.left) < 0:
            node.left = self.left_rotate(retNode.left)
            return self.right_rotate(retNode)

        # RR
        if self.get_balance_factor(retNode) < -1 and self.get_balance_factor(retNode.right) <= 0:
            return self.left_rotate(retNode)

        # RL: Y的X的的右子树更高, 先左旋, 后右旋
        if self.get_balance_factor(retNode) < -1 and self.get_balance_factor(retNode.left) > 0:
            retNode.right = self.right_rotate(retNode.right)
            return self.left_rotate(retNode)

        return retNode

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

    t = AVL()
    t.add(0, 0)
    t.add(1, 1)
    t.add(2, 2)
    t.add(3, 3)
    t.add(4, 4)
    t.add(5, 5)

    print(t.is_bst())
    print(t.is_balanced())
    # t.pre_order_traveral(t.root)
    # t.pre_order_nr()
