import sys


def merge_in_order(seq_a, seq_b):
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


if __name__ == "__main__":
    print("There is possibility to pass a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_mer.txt'
        with open(filename) as file:
            size_a = int(file.readline().strip())
            seq_a = [int(number) for number in file.readline().split()][:size_a]
            size_b = int(file.readline().strip())
            seq_b = [int(number) for number in file.readline().split()][:size_b]
            for number in merge_in_order(seq_a, seq_b):
                print(number, end=' ')
