import math

from node.fibonacciHeap_treeNode import FibonacciHeap_TreeNode, Fibonacci_Nil
from node.linkedList_node import LinkedList_Node
from linked_list import Linked_List

class Fibonacci_heap:
    def __init__(self):
        self.n = 0
        self.nil = Fibonacci_Nil()
        self.min = self.nil
        self.root_list = Linked_List()

    def fib_heap_insert(self, x: FibonacciHeap_TreeNode):
        x.degree = 0
        x.p = self.nil
        x.child = self.nil
        x.mark = False
        self.root_list.insert(LinkedList_Node(x))
        if self.min == self.nil:
            self.min = x
        else:
            if x.key < self.min.key:
                self.min = x
        self.n += 1
    
    def fib_heap_union(self, H: 'Fibonacci_heap'):
        self.root_list.concat(H.root_list)
        if (self.min == self.nil) or (H.min != H.nil and H.min.key < self.min.key):
            self.min = H.min
        self.n += H.n
    
    def fib_heap_extract_min(self):
        z = self.min
        if z != self.nil:
            for x in z.child_list:
                self.root_list.insert(LinkedList_Node(x))
                x.p = self.nil

            z_node = self.root_list.search(z)
            self.root_list.delete(z_node)
            if self.root_list.empty():
                self.min = self.nil
            else:
                self.min = z_node.next
                self.consolidate()
            self.n -= 1
        return z

    def consolidate(self):
        A = [self.nil for _ in range(math.floor(math.log2(self.n)) + 1)]
        for w in self.root_list:
            x = w
            d = x.degree
            while A[d] != self.nil:
                y = A[d]
                if x.key > y.key:
                    y, x = x, y
                self.fib_heap_link(y, x)
                A[d] = self.nil
                d += 1
            A[d] = x
        self.min = self.nil
        for element in A:
            if element != self.nil:
                if self.min == self.nil:
                    self.root_list.insert(LinkedList_Node(element))
                    self.min = element
                else:
                    self.root_list.insert(LinkedList_Node(element))
                    if element.key < self.min.key:
                        self.min = element
    
    def fib_heap_link(self, y: FibonacciHeap_TreeNode, x: FibonacciHeap_TreeNode):
        y_node = self.root_list.search(y)
        self.root_list.delete(y_node)
        x.child_list.insert(LinkedList_Node(y))
        x.degree += 1
        y.mark = False

            


if __name__ == "__main__":
    pass
