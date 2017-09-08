import math
from enum import Enum, auto


class HeapType(Enum):
    MAX = auto()
    MIN = auto()


class Heap(list):
    def __init__(self, iterable=[], heapType=HeapType.MAX):
        self.__heapsize = 0
        self.heap_type = heapType
        super().__init__([0] + iterable)
        if self.heap_type is HeapType.MAX:
            self.build_max_heap()

    def __len__(self):
        return super().__len__() - 1

    def __iter__(self):
        self.n = 1
        return self

    def __next__(self):
        if self.n < len(self):
            result = self[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def __str__(self):
        return "[{0}]".format(", ".join(str(val) for val in self[1:]))

    @property
    def heapsize(self):
        return self.__heapsize

    @heapsize.setter
    def heapsize(self, size):
        self.__heapsize = size

    def __left(self, i):
        return 2 * i

    def __right(self, i):
        return 2 * i + 1

    def __parent(self, i):
        return math.floor(i // 2)

    def heap_maximum(self):
        if self.heap_type is HeapType.MAX:
            return self[1]

    def heap_extract_maximum(self):
        if self.heapsize < 1:
            raise ValueError("Heap underflow.")

        max_value = self[1]
        self[1] = self[self.heapsize]
        self.heapsize -= 1
        self.max_heapify(1)
        return max_value

    def heap_increase_key(self, i, key):
        if key < self[i]:
            raise ValueError("New key is smaller than current key.")
        self[i] = key
        while i > 1 and self[self.__parent(i)] < self[i]:
            self[i], self[self.__parent(i)] = self[self.__parent(i)], self[i]
            i = self.__parent(i)
        
    def max_heap_insert(self, key):
        self.heapsize += 1
        self[self.heapsize] = -math.inf
        self.heap_increase_key(self.heapsize, key)

    def max_heapify(self, i):
        l = self.__left(i)
        r = self.__right(i)

        if l <= self.heapsize and self[l] > self[i]:
            largest = l
        else:
            largest = i

        if r <= self.heapsize and self[r] > self[largest]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        # bottom up to build the max heap
        self.heapsize = len(self)
        for i in reversed(range(1, math.floor(len(self) // 2) + 1)):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in reversed(range(2, len(self) + 1)):
            self[1], self[i] = self[i], self[1]
            self.heapsize -= 1
            self.max_heapify(1)


if __name__ == "__main__":
    l = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    heap = Heap(l)
    heap.heap_sort()
    for h in heap:
        print(h)
