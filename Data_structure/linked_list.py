from node.linkedList_node import LinkedList_Node, LinkedList_Nil


class Linked_List:
    def __init__(self):
        self.nil = LinkedList_Nil()
    
    def __iter__(self):
        self.__iter = self.nil.next
        return self

    def __next__(self):
        if self.__iter != self.nil:
            result = self.__iter.key
            self.__iter = self.__iter.next
            return result
        else:
            raise StopIteration

    @property
    def begin(self):
        return self.nil.next

    @property
    def end(self):
        return self.nil

    def empty(self):
        return self.nil.next == self.nil and self.nil.prev == self.nil

    @property
    def size(self):
        return self.distance(self.begin, self.end)

    def distance(self, begin: LinkedList_Node, end: LinkedList_Node):
        cur = begin
        n = 0
        while cur != end:
            cur = cur.next
            n += 1
        return n

    def insert(self, x: LinkedList_Node):
        x.next = self.nil.next
        self.nil.next.prev = x
        self.nil.next = x
        x.prev = self.nil

    def delete(self, x: LinkedList_Node):
        x.prev.next = x.next
        x.next.prev = x.prev

    def clear(self):
        cur = self.nil.next
        while cur != self.nil:
            tmp = cur
            cur = cur.next
            self.delete(tmp)

    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        return x

    def concat(self, other: 'Linked_List'):
        other.nil.prev.next = self.nil.next
        self.nil.next.prev = other.nil.prev
        self.nil.next = other.nil.next
        other.nil.next.prev = self.nil



if __name__ == "__main__":
    key_list = [9, 16, 4, 1]
    link_list = Linked_List()
    for k in key_list:
        link_list.insert(LinkedList_Node(k))

    # print(link_list.size)

    k_list = [1, 2, 3, 4]
    l = Linked_List()
    for k in k_list:
        l.insert(LinkedList_Node(k))
    
    link_list.concat(l)
    for k in link_list:
        print(k)

