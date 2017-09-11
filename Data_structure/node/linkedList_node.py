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