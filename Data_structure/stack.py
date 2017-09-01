from custom_exception import SizeError

class Stack(list):
    def __init__(self, n):
        super().__init__([None for _ in range(n)])
        self.top = -1

    def stack_empty(self):
        return self.top == -1

    def push(self, x):
        self.top += 1
        self[self.top] = x
    
    def pop(self):
        if self.stack_empty():
            raise SizeError("Underflow")
        else:
            return self[self.top + 1]

        
