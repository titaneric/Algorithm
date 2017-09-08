from Data_structure.node import B_TreeNode


class B_tree:
    def __init__(self, t):
        self.__root = None
        self.__t = t  # minimum degree
        self.B_tree_create()

    @property
    def root(self) -> B_TreeNode:
        return self.__root

    @root.setter
    def root(self, root: B_TreeNode):
        self.__root = root

    @property
    def t(self):
        return self.__t

    def B_tree_search(self, k):
        return self.root.searchNode(k)

    def B_tree_create(self):
        rooted_node = B_TreeNode()
        rooted_node.leaf = True
        rooted_node.n = 0
        self.root = rooted_node  # if the tree is non-empty, the root must have at least one key
        # notion: use pickle to write the tree node

    def B_tree_split_child(self, x: B_TreeNode, i):
        y = x.child_pointers[i]
        z = B_TreeNode()
        z.leaf = y.leaf
        z.n = self.t - 1
        # copy key from y.keys to z.keys
        for j in range(self.t - 1):
            z.keys[j] = y.keys[j + self.t]

        if not y.leaf:
            # copy child pointer from y.child_pointers to z.child_pointers
            for j in range(self.t):
                z.child_pointers[j] = y.child_pointers[j + self.t]
        median = y.keys[self.t - 1]  # median
        y.n = self.t - 1
        # shift child pointer right one unit
        x.n += 1
        for j in reversed(range(i + 1, x.n)):
            x.child_pointers[j + 1] = x.child_pointers[j]
        x.child_pointers[i + 1] = z
        # shift key right one unit
        for j in reversed(range(i, x.n - 1)):
            x.keys[j + 1] = x.keys[j]
        x.keys[i] = median

    def B_tree_insert(self, k):
        r = self.root
        # if the root is full, than run the recursion
        if r.n == 2 * self.t - 1:
            s = B_TreeNode()
            self.root = s
            s.leaf = False
            s.n = 0
            s.child_pointers[0] = r
            self.B_tree_split_child(s, 0)
            self.B_tree_insert_nonfull(s, k)
        else:
            self.B_tree_insert_nonfull(r, k)

    def B_tree_insert_nonfull(self, x: B_TreeNode, k):
        i = x.n - 1
        if x.leaf:
            x.n += 1
            while i >= 0 and x.keys and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1

            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            # if the node is full, split it
            if x.child_pointers[i].n == 2 * self.t - 1:
                self.B_tree_split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.B_tree_insert_nonfull(x.child_pointers[i], k)


if __name__ == "__main__":

    key_list = ["G", "M", "P", "X", "A", "C", "D", "E", "J", "K", "N", "O", "R", "S",
                "T", "U", "V", "Y", "Z"]
    """
    key_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]"
    """
    tree = B_tree(3)
    for k in key_list:
        tree.B_tree_insert(k)
