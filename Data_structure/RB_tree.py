from BS_tree import BS_Tree
from node import Nil, RB_TreeNode, Color, OS_TreeNode


class RB_Tree(BS_Tree):
    def __init__(self):
        self.__nil = Nil()
        self.__root = self.__nil
        self.__size = 0

    @property
    def root(self) -> RB_TreeNode:
        return self.__root

    @root.setter
    def root(self, root: RB_TreeNode):
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

    @property
    def height(self):
        return self.calculate_depth(self.root) - 1

    def calculate_depth(self, node: RB_TreeNode):
        return super().calculate_depth(node, nil=self.nil)

    def tree_successor(self, x):
        return super().tree_successor(x, nil=self.nil)

    def tree_predecessor(self, x):
        return super().tree_predecessor(x, nil=self.nil)

    def tree_maximum(self):
        return super().tree_maximum(self.root, nil=self.nil)

    def tree_minimum(self):
        return super().tree_minimum(self.root, nil=self.nil)

    def levelorder_tree_walk(self):
        yield from super().levelorder_tree_walk(nil=self.nil)

    def inorder_tree_walk(self):
        yield from super().inorder_tree_walk(nil=self.nil)

    def postorder_tree_walk(self):
        yield from super().postorder_tree_walk(nil=self.nil)

    def preorder_tree_walk(self):
        yield from super().preorder_tree_walk(nil=self.nil)

    def tree_search(self, k):
        return super().tree_search(k, nil=self.nil)

    def left_rotate(self, x: RB_TreeNode):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p is self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        if isinstance(x, OS_TreeNode):
            y.size = x.size
            x.size = x.left.size + x.right.size + 1

    def right_rotate(self, y: RB_TreeNode):
        x = y.left
        y.left = x.right
        if x.right is not self.nil:
            x.right.p = y
        x.p = y.p
        if y.p is self.nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else: 
            y.p.right = x
        x.right = y
        y.p = x
        if isinstance(x, OS_TreeNode):
            x.size = y.size
            y.size = y.left.size + y.right.size + 1

    def tree_insert(self, z: RB_TreeNode):
        super().tree_insert(z, nil=self.nil)
        z.left, z.right, z.color = (self.nil, self.nil, Color.RED)
        self.RB_insert_fixup(z)

    def RB_insert_fixup(self, z: RB_TreeNode):
        while z.p.color is Color.RED:
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color is Color.RED:
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                elif z == z.p.right:
                    z = z.p
                    self.left_rotate(z)
                elif z == z.p.left:
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color is Color.RED:
                    z.p.color = Color.BLACK
                    y.color = Color.BLACK
                    z.p.p.color = Color.RED
                    z = z.p.p
                elif z == z.p.left:
                    z = z.p
                    self.right_rotate(z)
                elif z == z.p.right:
                    z.p.color = Color.BLACK
                    z.p.p.color = Color.RED
                    self.left_rotate(z.p.p)
        self.root.color = Color.BLACK

    def tree_delete(self, z):
        determined_fixup, x = super().tree_delete(z, nil=self.nil)
        if determined_fixup:
            self.RB_delete_fixup(x)

    def RB_delete_fixup(self, x: RB_TreeNode):
        while x != self.root and x.color is Color.BLACK:
            if x == x.p.left:
                w = x.p.right
                if w.color is Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color is Color.BLACK and w.right.color is Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                elif w.right.color is Color.BLACK:
                    w.left.color = Color.BLACK
                    w.color = Color.RED
                    self.right_rotate(w)
                    w = x.p.right
                elif w.right.color is Color.RED:
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color is Color.RED:
                    w.color = Color.BLACK
                    x.p.color = Color.RED
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.left.color is Color.BLACK and w.right.color is Color.BLACK:
                    w.color = Color.RED
                    x = x.p
                elif w.left.color is Color.BLACK:
                    w.right.color = Color.BLACK
                    w.color = Color.RED
                    self.left_rotate(w)
                    w = x.p.left
                elif w.left.color is Color.RED:
                    w.color = x.p.color
                    x.p.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.right_rotate(x.p)
                    x = self.root
        x.color = Color.BLACK


if __name__ == "__main__":
    # Test the rotation
    '''
    key_list = [7, 4, 11, 3, 6, 9, 18, 2, 14, 19, 12, 17, 22, 20]
    tree = RB_Tree()
    for key in key_list:
        tree.tree_insert(RB_TreeNode(key))

    tree.inorder_tree_walk()
    print()
    node11 = tree.tree_search(11)
    tree.left_rotate(node11)
    tree.inorder_tree_walk()
    print()
    node18 = tree.tree_search(18)
    tree.left_rotate(node18)
    tree.inorder_tree_walk()
    '''
    k_list = [11, 2, 14, 1, 7, 15, 5, 8]
    tree1 = RB_Tree()
    for k in k_list:
        tree1.tree_insert(RB_TreeNode(k))

    for k in tree1.levelorder_tree_walk():
        print(k.key)
    # tree1.inorder_tree_walk()
    tree1.tree_insert(RB_TreeNode(4))
    node4 = tree1.tree_search(4)
    tree1.tree_delete(node4)
    # tree1.inorder_tree_walk()
