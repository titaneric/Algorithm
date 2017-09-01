class Queue(list):
    def __init__(self, n):
        super().__init__([None for _ in range(n)])
        self.head = 0
        self.tail = 0
    
    def enqueue(self, x):
        self[self.tail] = x
        if self.tail == self.__len__():
            self.tail = 0
        else:
            self.tail += 1
    
    def dequeue(self):
        x = self[self.head]
        if self.head == self.__len__():
            self.head = 1
        else:
            self.head += 1
        return x

        