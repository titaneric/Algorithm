import math


class Fenwick_tree:
    def __init__(self, array: list):
        # Count the new array size
        self.newArr_size = 2 ** int(math.ceil(math.log2(len(array))) + 1)
        self.newArr = [0 for _ in range(self.newArr_size)]
        for _ in range(self.newArr_size - len(array)):
            array.append(0)
        # Start preprocessing
        for index in range(self.newArr_size):
            self.updateValue(index, array[index])
        # End preprocessing

    def updateValue(self, index: int, value: int):
        for i in self.updateRelatedIndex(index):
            self.newArr[i] += value

    def updateRelatedIndex(self, index: int):
        l = []
        v = index + 1
        newValue = v
        l.append(index)
        while newValue < self.newArr_size:
            bin_value = bin(newValue)
            newValue = newValue + int(bin_value[bin_value.rfind("1"):], 2)
            newIndex = newValue - 1
            l.append(newIndex)
        return l

    def prefixSumRelatedIndex(self, index: int):
        l = []
        v = index + 1
        newIndex = v
        l.append(index)
        while True:
            bin_index = bin(newIndex).lstrip("0b")
            bin_index_list = list(bin_index)
            bin_index_list[bin_index.rfind("1")] = "0"
            bin_index = "".join(s for s in bin_index_list)
            newIndex = int(bin_index, 2)
            if newIndex == 0:
                break
            else:
                l.append(newIndex)
        return l

    def prefixSum(self, end: int):
        return sum([self.newArr[i] for i in self.prefixSumRelatedIndex(end)])


if __name__ =="__main__":
    tree = Fenwick_tree([1, 2, 3, 4, 5, 6, 7, 8])
    print(tree.prefixSum(7))
