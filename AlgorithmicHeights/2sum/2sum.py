import sys


def two_sum(sequence):
    result = None
    for i in range(len(sequence)):
        for j in range(1, len(sequence)):
            if i != j and sequence[i] == -sequence[j]:
                result = i+1, j+1
    if result is not None:
        return (result[0], result[1]) if result[0] < result[1] else (result[1], result[0])


def parse(file):
    array_count, elements_count = [int(x) for x in file.readline().split()]
    sequences = [sequence.split() for sequence in file.read().split('\n')]
    for i in range(len(sequences)):
        sequences[i] = list(map(lambda x: int(x), sequences[i]))[:elements_count]
    return sequences[:array_count]


def print_two_sums(sequences):
    for sequence in sequences:
        indices = two_sum(sequence)
        if indices:
            print(indices[0], indices[1])
        else:
            print(-1)


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_2sum.txt'
        try:
            with open(filename) as input_file:
                sequences = parse(input_file)
                print_two_sums(sequences)
        except IOError:
            print("Error while reading the file")

