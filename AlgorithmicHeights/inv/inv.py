import sys

# Unfortunately this solution is too slow and exceeds limit of 5 minutes
# Check cpp version of the algorithm which is located in the same directory


def bubble_sort(sequence):
    inversion_count = 0
    for i in range(len(sequence)):
        for j in range(1, len(sequence)):
            if sequence[j] < sequence[j-1]:
                sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
                inversion_count += 1
    return inversion_count


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_inv.txt'
        try:
            with open(filename) as file:
                size = int(file.readline())
                sequence = [int(x) for x in file.readline().split()][:size]
                print(bubble_sort(sequence))
        except IOError:
            print('Error while opening the file')
