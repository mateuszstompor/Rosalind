import sys


def three_sum(s):
    temp = {}
    for i, value in enumerate(s):
        for j in range(i+1, len(s)):
            temp[value + s[j]] = (i, j)
    for i, value in enumerate(s):
        pos = temp.get(-value)
        if pos and i not in pos:
            return list(sorted([i+1, pos[0]+1, pos[1]+1]))


def parse(file):
    array_count, elements_count = [int(x) for x in file.readline().split()]
    sequences = [sequence.split() for sequence in file.read().split('\n')]
    for i in range(len(sequences)):
        sequences[i] = list(map(lambda x: int(x), sequences[i]))[:elements_count]
    return sequences[:array_count]


def print_sums(sequences):
    for sequence in sequences:
        indices = three_sum(sequence)
        if indices:
            print(indices[0], indices[1], indices[2])
        else:
            print(-1)


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_3sum.txt'
        try:
            with open(filename) as input_file:
                sequences = parse(input_file)
                print_sums(sequences)
        except IOError:
            print("Error while reading the file")

