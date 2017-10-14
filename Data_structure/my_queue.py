class My_queue(list):
    def __init__(self, n=100):
        super().__init__([None for _ in range(n)])
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def enqueue(self, x):
        self[self.tail] = x
        if self.tail == self.__len__():
            self.tail = 0
            self.size = 0
        else:
            self.tail += 1
            self.size += 1
    
    def dequeue(self):
        x = self[self.head]
        self.size -= 1
        if self.head == self.__len__():
            self.head = 1
        else:
            self.head += 1
        return x

    def empty(self):
        return self.size == 0
    



if __name__ == "__main__":
    q = My_queue()
    q.enqueue(3)
    q.enqueue(5)
    q.enqueue(7)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size)
    
    


        