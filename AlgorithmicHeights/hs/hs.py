import sys
from math import floor
import time


def swap(index_a, index_b, sequence):
    sequence[index_b], sequence[index_a] = sequence[index_a], sequence[index_b]


class Heap:
    def __init__(self):
        self.sequence = []

    def insert(self, value):
        self.sequence.append(value)
        self.__heapify(len(self.sequence) - 1, len(self.sequence), self.sequence)

    def __heapify(self, index, size, sequence):
        if index == 0:
            return
        sibling = self.__sibling(index, size)
        if sibling is not None and sibling < index and sequence[index] > sequence[sibling]:
            swap(sibling, index, sequence)
            index = sibling
        parent_index = self.__parent(index)
        if sequence[index] > sequence[parent_index]:
            swap(index, parent_index, sequence)
            self.__heapify(parent_index, size, sequence)

    def __sibling(self, index, size):
        if index == 0:
            return None
        parent = self.__parent(index)
        if index == 2 * (parent + 1) - 1:
            return index + 1 if size > index + 1 else None
        else:
            return index - 1 if 0 <= index - 1 else None

    def __parent(self, index):
        return floor((index+1)/2) - 1

    def __children(self, index, size):
        left_child_index = 2 * (index + 1) - 1
        right_child_index = 2 * (index + 1)
        if right_child_index < size:
            return [left_child_index, right_child_index]
        elif left_child_index < size:
            return [left_child_index]
        else:
            return []

    def __down_heapify(self, sequence, length):
        stack = [0]
        while stack:
            index = stack.pop(0)
            children = self.__children(index, length)
            if len(children) == 2:
                if sequence[children[0]] > sequence[index]:
                    swap(children[0], index, sequence)
                    if sequence[children[1]] > sequence[children[0]]:
                        swap(children[0], children[1], sequence)
                        stack.append(children[1])
                    stack.append(children[0])
                elif sequence[children[1]] > sequence[index]:
                    swap(children[1], index, sequence)
                    stack.append(children[1])
            elif len(children) == 1 and sequence[children[0]] > sequence[index]:
                swap(children[0], index, sequence)
                stack.append(children[0])

    def sorted(self):
        sequence = self.sequence.copy()
        for i in range(len(sequence)):
            sequence_size = len(sequence) - i
            swap(sequence_size - 1, 0, sequence)
            self.__down_heapify(sequence, sequence_size - 1)
        return sequence

    def __str__(self):
        return self.sequence.__str__()


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_hs.txt'
        with open(filename) as file:
            start = time.time()
            size = int(file.readline().strip())
            heap = Heap()
            for number in [int(x) for x in file.readline().split()][:size]:
                heap.insert(number)
            sorted = heap.sorted()
            for i in range(len(sorted)):
                print(sorted[i], end=' ')
            print(f"Elapsed time: {time.time() - start:.4}")
