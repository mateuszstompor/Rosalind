import sys


def merge(seq_a, seq_b):
    seq_a = seq_a.copy()
    seq_b = seq_b.copy()
    result = []
    while seq_a and seq_b:
        if seq_a[0] > seq_b[0]:
            result.append(seq_b.pop(0))
        else:
            result.append(seq_a.pop(0))
    while seq_a:
        result.append(seq_a.pop(0))
    while seq_b:
        result.append(seq_b.pop(0))
    return result


def merge_sort(seq_a, seq_b):
    if len(seq_a) == 1 and len(seq_b) == 1:
        return merge(seq_a, seq_b)
    if len(seq_a) != 1:
        half = int(len(seq_a) / 2)
        seq_a = merge_sort(seq_a[:half], seq_a[half:])
    if len(seq_b) != 1:
        half = int(len(seq_b) / 2)
        seq_b = merge_sort(seq_b[:half], seq_b[half:])
    return merge(seq_a, seq_b)


def sorted(sequence):
    if len(sequence) == 1:
        return sequence
    else:
        half = int(len(sequence)/2)
        return merge_sort(sequence[:half], sequence[half:])


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        path = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_ms.txt'
        with open(path) as file:
            size = int(file.readline().strip())
            numbers = [int(x) for x in file.readline().split()][:size]
            for number in sorted(numbers):
                print(number, end=' ')
