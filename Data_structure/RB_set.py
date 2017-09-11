from RB_tree import RB_Tree
from node.RB_treeNode import RB_TreeNode


class RB_set:
    def __init__(self):
        self.__map = RB_Tree()
        self.__it = None

    def __len__(self):
        return self.__map.size

    def __contains__(self, k):
        node = self.__map.tree_search(k)
        return node != self.__map.nil

    def __iter__(self):
        self.__it= self.__map.begin()
        return self

    def __next__(self):
        if self.__it != self.__map.end():
            result = self.__it.key
            self.__it = self.__map.tree_successor(self.__it)
            return result
        else:
            raise StopIteration

    def add(self, k):
        node = self.__map.tree_search(k)
        if node == self.__map.nil:
            self.__map.tree_insert(RB_TreeNode(k))


if __name__ == "__main__":
    k_list = [1, 34, 2, 5, 1]
    my_set = RB_set()
    for k in k_list:
        my_set.add(k)
    
    for s in my_set:
        print(s)
    
