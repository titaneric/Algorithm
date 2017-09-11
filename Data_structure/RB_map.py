from RB_tree import RB_Tree
from node.RB_treeNode import RB_TreeNode
from custom_exception import KeyError


class Pair:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def __eq__(self, other):
        return self.key == other.key

    def __ne__(self, other):
        return self.key != other.key

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key


class RB_map:
    def __init__(self):
        self.__map = RB_Tree()

    def __len__(self):
        return self.__map.size

    def __contains__(self, k):
        node = self.__map.tree_search(Pair(k, None))
        return node != self.__map.nil

    def __setitem__(self, k, v):
        node = self.__map.tree_search(Pair(k, None))
        if node != self.__map.nil:
            node.key.value = v
        else:
            self.__map.tree_insert(RB_TreeNode(Pair(k, v)))

    def __getitem__(self, k):
        node = self.__map.tree_search(Pair(k, None))
        if node != self.__map.nil:
            return node.key.value
        else:
            raise KeyError("Key {} doesn't exist!".format(k))

    def __delitem__(self, k):
        node = self.__map.tree_search(Pair(k, None))
        if node != self.__map.nil:
            self.__map.tree_delete(node)
        else:
            raise KeyError("Key {} doesn't exist!".format(k))

    def items(self):
        for node in self.__map.inorder_tree_walk():
            yield (node.key.key, node.key.value)

    def keys(self):
        for node in self.__map.inorder_tree_walk():
            yield node.key.key

    def values(self):
        for node in self.__map.inorder_tree_walk():
            yield node.key.value


if __name__ == "__main__":
    my_map = RB_map()
    my_map["test"] = 1
    my_map["da"] = 2
    my_map["a"] = 12

    for k, v in my_map.items():
        print(k, v)
