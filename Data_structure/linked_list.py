from node import LinkedList_Node, LinkedList_Nil


class Linked_List:
    def __init__(self):
        self.nil = LinkedList_Nil()
        # self.head = self.nil
        # self.tail = self.nil

    def insert(self, x: LinkedList_Node):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil
    
    def delete(self, x: LinkedList_Node):
        x.prev.next = x.next
        x.next.prev = x.prev
    
    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        return x

if __name__ == "__main__":
    key_list = [9, 16, 4, 1]
    link_list = Linked_List()
    for k in key_list:
        link_list.insert(LinkedList_Node(k))

        
