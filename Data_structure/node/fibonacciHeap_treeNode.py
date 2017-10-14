import sys
sys.path.append("../Data_structure")
from linked_list import Linked_List

class FibonacciHeap_TreeNode:
    def __init__(self, k=None):
        self.degree = 0
        self.key = k
        self.p = None
        self.child_list = LinkedList()
        self.mark = False


class Fibonacci_Nil(FibonacciHeap_TreeNode):
    def __init__(self):
        super().__init__()