import sys


def hamming_distance(seq_a, seq_b):
    return sum(seq_a[i] != seq_b[i] for i in range(len(seq_a)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1], 'r') as file:
            seq_a, seq_b = file.readline().strip(), file.readline().strip()
            print(hamming_distance(seq_a, seq_b))
