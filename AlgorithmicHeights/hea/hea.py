import sys
from math import floor


def swap(index_a, index_b, sequence):
    sequence[index_b], sequence[index_a] = sequence[index_a], sequence[index_b]


class Heap:
    def __init__(self):
        self.sequence = []

    def insert(self, value):
        self.sequence.append(value)
        self.heapify(len(self.sequence) - 1)

    def heapify(self, index):
        if index == 0:
            return
        sibling = self.sibling(index)
        if sibling is not None and sibling < index and self.sequence[index] > self.sequence[sibling]:
            swap(sibling, index, self.sequence)
            index = sibling
        parent_index = self.parent(index)
        if self.sequence[index] > self.sequence[parent_index]:
            swap(index, parent_index, self.sequence)
            self.heapify(parent_index)

    def sibling(self, index):
        if index == 0:
            return None
        parent = self.parent(index)
        if index == 2 * (parent + 1) - 1:
            return index + 1 if len(self.sequence) > index + 1 else None
        else:
            return index - 1 if 0 <= index - 1 else None

    def parent(self, index):
        return floor((index+1)/2) - 1

    def __str__(self):
        return self.sequence.__str__()


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_hea.txt'
        with open(filename) as file:
            size = int(file.readline().strip())
            sequence = [int(x) for x in file.readline().split()][:size]
            heap = Heap()
            for number in sequence:
                heap.insert(number)
            for i in range(len(heap.sequence)):
                print(heap.sequence[i], end=' ')
