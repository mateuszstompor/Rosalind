import sys


def search_binarily(value, sequence, start_index, end_index):
    if start_index == end_index:
        return start_index if value == sequence[start_index] else None
    else:
        subarray_size = int((end_index - start_index)/2)
        left = search_binarily(value, sequence, start_index, start_index + subarray_size)
        right = search_binarily(value, sequence, start_index + subarray_size + 1, end_index)
        return left if left is not None else right


def index_of(value, sequence):
    index = search_binarily(value, sequence, 0, len(sequence) - 1)
    return -1 if index is None else index + 1


def indices(sequence, values):
    return [index_of(x, sequence) for x in values]


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_bins.txt'
        with open(filename) as file:
            sequence_size = int(file.readline().strip())
            numbers_size = int(file.readline().strip())
            sequence = [int(x) for x in file.readline().split()][:sequence_size]
            numbers = [int(x) for x in file.readline().split()][:numbers_size]
            for index in indices(sequence, numbers):
                print(index, end=" ")
