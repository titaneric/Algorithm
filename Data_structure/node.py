from enum import Enum, auto


class LinkedList_Node:
    def __init__(self, k):
        self.prev = None
        self.next = None
        self.key = k

class LinkedList_Nil(LinkedList_Node):
    def __init__(self):
        super().__init__(None)
        self.prev = self
        self.next = self

class TreeNode:
    def __init__(self, val=None):
        if val is not None:
            self.key = val
        self.right = None
        self.left = None
        self.p = None


class Color(Enum):
    RED = auto()
    BLACK = auto()


class RB_TreeNode(TreeNode):
    def __init__(self, val=None):
        super().__init__(val)
        self.__color = None

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Nil(RB_TreeNode):
    def __init__(self):
        super().__init__()
        self.color = Color.BLACK


class OS_TreeNode(RB_TreeNode):
    def __init__(self, val=None):
        super().__init__(val)
        self.size = 0


class OS_Nil(Nil):
    def __init__(self):
        super().__init__()
        self.size = 0


class B_TreeNode:
    def __init__(self):
        self.leaf = False
        self.__n = 0
        self.keys = []  # at least t - 1 keys, at most 2t -1 keys
        self.child_pointers = []  # at least t children, at most 2t children

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        if not self.child_pointers and not self.leaf:
            self.child_pointers = [B_TreeNode]
        previous_n = self.__n
        self.__n = n
        data_len = min(previous_n, self.n)
        diff = abs(self.n - data_len)
        self.keys = self.keys[:data_len] + ["" for _ in range(diff)]
        if not self.leaf:
            self.child_pointers = self.child_pointers[:data_len + 1] + [
                B_TreeNode() for _ in range(diff)]

    def searchNode(self, key):
        i = 1
        while i <= self.n and k > self.keys[i]:
            i += 1
        if i <= self.n and k == self.keys[i]:
            return self, i
        elif self.leaf:
            return None
        else:
            return self.searchNode(self.child_pointers[i], k)

class FibonacciHeap_TreeNode:
    def __init__(self):
        self.degree = 0
        self.key = 0
        self.p = None
        self.child = None
        self.mark = False

class Fibonacci_Nil(FibonacciHeap_TreeNode):
    def __init__(self):
        super().__init__()


