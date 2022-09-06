class Trie:
    """
    一颗多叉树, next存储每个子树
    """

    class Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = {}

    def __init__(self):
        self.root = self.Node()
        self.size = 0

    def add(self, word):
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                cur.next[c] = self.Node()
            cur = cur.next[c]

        if not cur.is_word:
            cur.is_word = True
            self.size += 1

    def contains(self, word):
        cur = self.root
        for c in word:
            if not cur.next.get(c):
                return False
            cur = cur.next[c]

        return cur.is_word

    def is_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            if not cur.next.get(c):
                return False
            cur = cur.next[c]

        return True

    def match(self, word):
        return self.__match(self.root, word, 0)

    def __match(self, node, word, index):
        """ 该节点的子树中是否匹配了该word """
        if index == len(word): return node.is_word

        c = word[index]
        if c != '.':
            if not node.next.get(c): return False
            return self.__match(node.next.get(c), word, index + 1)
        else:
            for k in node.next:
                if self.__match(node.next.get(k), word, index + 1): return True
            else:
                return False


if __name__ == '__main__':
    t = Trie()
    t.add("hello")
    t.add("ha")
    print(t.contains("he"))
    print(t.contains("ha"))
    print(t.contains("hello"))
    # print(t.match("he"))
    # print(t.match("ha"))
    # print(t.match("haa"))
    # print(t.match("h."))
    print(t.match("hello"))
