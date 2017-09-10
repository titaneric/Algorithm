from queue import Queue
from typing import Iterator

from node import TreeNode, Color, OS_TreeNode, Pair


class BS_Tree:
    def __init__(self):
        self.__root = None
        self.__size = 0

    @property
    def root(self) -> TreeNode:
        return self.__root

    @root.setter
    def root(self, root: TreeNode):
        self.__root = root
    
    def leftmost(self):
        return self.tree_minimum()

    def rightmost(self):
        return self.tree_maximum()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def height(self):
        return self.calculate_depth(self.root) - 1

    def path(self, start: TreeNode, end: TreeNode) -> Iterator[TreeNode]:
        x = start
        while x != end.p:
            yield x
            x = x.p

    def calculate_depth(self, node: TreeNode, nil=None):
        if node is nil:
            return 0
        else:
            return max(self.calculate_depth(node.left),
                       self.calculate_depth(node.right)) + 1

    def levelorder_tree_walk(self, nil=None) -> Iterator[TreeNode]:
        q = Queue()
        q.put(self.root)
        while not q.empty():
            n = q.qsize()
            for _ in range(n):
                node = q.get()
                yield node
                if node.left is not nil:
                    q.put(node.left)
                if node.right is not nil:
                    q.put(node.right)

    def inorder_tree_walk(self, nil=None) -> Iterator[TreeNode]:
        yield from self.__inorder_tree_walk(self.root, nil=nil)

    def __inorder_tree_walk(self, x: TreeNode, nil=None):
        if x is not nil:
            yield from self.__inorder_tree_walk(x.left, nil=nil)
            yield x
            yield from self.__inorder_tree_walk(x.right, nil=nil)

    def postorder_tree_walk(self, nil=None) -> Iterator[TreeNode]:
        yield from self.__postorder_tree_walk(self.root, nil=nil)

    def __postorder_tree_walk(self, x: TreeNode, nil=None):
        if x is not nil:
            yield from self.__postorder_tree_walk(x.left, nil=nil)
            yield from self.__postorder_tree_walk(x.right, nil=nil)
            yield x

    def preorder_tree_walk(self, nil=None) -> Iterator[TreeNode]:
        yield from self.__preorder_tree_walk(self.root, nil=None)

    def __preorder_tree_walk(self, x: TreeNode, nil=None):
        if x is not nil:
            yield x
            yield from self.__preorder_tree_walk(x.left, nil=nil)
            yield from self.__preorder_tree_walk(x.right, nil=nil)

    def tree_minimum(self, x=None, nil=None) -> TreeNode:
        x = self.root if x is None else x
        while x.left is not nil:
            x = x.left
        return x

    def tree_maximum(self, x=None, nil=None) -> TreeNode:
        x = self.root if x is None else x
        while x.right is not nil:
            x = x.right
        return x

    def tree_successor(self, x: TreeNode, nil=None) -> TreeNode:
        if x.right is not nil:
            return self.tree_minimum(x.right, nil=nil)
        y = x.p
        while y is not nil and x == y.right:
            x = y
            y = y.p
        return y

    def tree_predecessor(self, x: TreeNode, nil=None) -> TreeNode:
        if x.left is not nil:
            return self.tree_maximum(x.left, nil=nil)
        y = x.p
        while y is not nil and x == y.left:
            x = y
            y = y.p
        return y

    def tree_search(self, k, iterative=True, nil=None) -> TreeNode:
        if not iterative:
            return self.__tree_search(self.root, k, nil=nil)
        else:
            return self.__iterative_tree_search(self.root, k, nil=nil)

    def __tree_search(self, x: TreeNode, k, nil=None) -> TreeNode:
        if x is nil or k == x.key:
            return x
        if k < x.key:
            return self.__tree_search(x.left, k, nil=nil)
        else:
            return self.__tree_search(x.right, k, nil=nil)

    def __iterative_tree_search(self, x: TreeNode, k, nil=None) -> TreeNode:
        while x is not nil and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_insert(self, z: TreeNode, nil=None):
        self.size += 1
        y = nil
        x = self.root
        while x is not nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u: TreeNode, v: TreeNode, nil=None):
        if u.p is nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if (v is not nil and nil is None) or (nil is not None):
            v.p = u.p

    def tree_delete(self, z: TreeNode, nil=None):
        self.size -= 1
        if nil is not None:
            y = z
            y_original_color = y.color

        if z.left is nil:
            if nil is not None:
                x = z.right
            self.transplant(z, z.right, nil=nil)
        elif z.right is nil:
            if nil is not None:
                x = z.left
            self.transplant(z, z.left, nil=nil)
        else:
            y = self.tree_minimum(z.right, nil=nil)
            if nil is not None:
                y_original_color = y.color
                x = y.right
            if y.p != z:
                self.transplant(y, y.right, nil=nil)
                y.right = z.right
                y.right.p = y
            elif nil is not None:
                x.p = y

            self.transplant(z, y, nil=nil)
            y.left = z.left
            y.left.p = y
            if nil is not None:
                y.color = z.color

        if nil is not None:
            return (y_original_color is Color.BLACK, x)


if __name__ == "__main__":
    tree = BS_Tree()
    key_list = [12, 5, 18, 2, 9, 15, 19, 13, 17]
    for key in key_list:
        tree.tree_insert(TreeNode(key))

    node13 = tree.tree_search(13)
    tree.tree_delete(node13)
    # tree.inorder_tree_walk()
    # print(tree.height)
    for node in tree.levelorder_tree_walk():
        print(node.key)
    