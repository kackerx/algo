class UnionFind:
    """
    parent的索引, 是元素e的值
    parent的值, 是元素e的集合id
    """

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.sz = [1 for i in range(size)]

    def size(self):
        return len(self.parent)

    def find(self, p):
        """ 查找元素p的根节点 """
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union_elements(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root == q_root: return

        if self.sz[p_root] < self.sz[q_root]:
            self.parent[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.parent[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]
