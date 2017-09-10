import copy

from RB_tree import RB_Tree
from node import RB_TreeNode


class RB_set:
    def __init__(self):
        self.__map = RB_Tree()
        self.__iter_key = None

    def __len__(self):
        return self.__map.size

    def __contains__(self, k):
        node = self.__map.tree_search(k)
        return node != self.__map.nil

    def __iter__(self):
        self.__iter_key = self.__map.begin().key
        return self

    def __next__(self):
        node = self.__map.tree_search(self.__iter_key)
        if node != self.__map.end():
            result = self.__iter_key
            next_node = self.__map.tree_successor(node)
            print("node is", next_node.key)
            self.__iter_key = next_node.key
            print("change to", self.__iter_key)
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
    
