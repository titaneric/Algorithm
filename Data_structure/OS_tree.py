from RB_tree import RB_Tree
from node.OS_treeNode import OS_TreeNode, OS_Nil
from custom_exception import RangeError


class OS_tree(RB_Tree):
    def __init__(self):
        self.__nil = OS_Nil()
        self.__root = self.__nil
        self.__size = 0

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def nil(self):
        return self.__nil

    def tree_insert(self, z: OS_TreeNode):
        super().tree_insert(z)
        for node in self.path(start=z, end=self.root):
            node.size += 1

    def tree_delete(self, z: OS_TreeNode):
        super().tree_delete(z)
        for node in self.path(start=z, end=self.root):
            node.size -= 1

    def OS_select(self, i) -> OS_TreeNode:
        if not (1 <= i <= self.size):
            raise RangeError(
                "The given i must be in the range(1, {})".format(self.size + 1))

        return self.__OS_select(self.root, i)

    def __OS_select(self, x: OS_TreeNode, i):
        r = x.left.size + 1
        if r == i:
            return x
        elif i < r:
            return self.__OS_select(x.left, i)
        else:
            return self.__OS_select(x.right, i - r)

    def OS_rank(self, x: OS_TreeNode) -> int:
        r = x.left.size + 1
        y = x
        while y != self.root:
            if y == y.p.right:
                r += y.p.left.size + 1
            y = y.p
        return r


if __name__ == "__main__":
    tree = OS_tree()
    key_list = [1, 3, 5, 6, 7, 10]
    for k in key_list:
        tree.tree_insert(OS_TreeNode(k))

    for node in tree.levelorder_tree_walk():
        print(node.key, node.size)

    print()
    print(tree.OS_select(6).key)
    node_10 = tree.tree_search(10)
    print(tree.OS_rank(node_10))
    print(tree.size)
