import sys
import operator


def majority_element(sequence):
    count = {}
    for number in sequence:
        count[number] = count.get(number, 0) + 1
    maximum = max(count.items(), key=operator.itemgetter(1))[0]
    return maximum if count[maximum] > len(sequence)/2 else -1


def parse_sequences(file, sequence_length, sequences_amount):
    sequences = []
    for i in range(sequence_amount):
         sequences.append([int(x) for x in file.readline().split()][:sequence_length])
    return sequences


def majority_elements(sequences):
    return [majority_element(sequence) for sequence in sequences]


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_maj.txt'
        with open(filename) as file:
            sequence_amount, sequence_length = [int(x) for x in file.readline().split()]
            sequences = parse_sequences(file, sequence_length, sequence_amount)
            for element in majority_elements(sequences):
                print(element, end=' ')
