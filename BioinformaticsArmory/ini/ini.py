import sys


def nucleotide_occurrences(sequence):
    occurrences = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for letter in sequence:
        occurrences[letter] += 1
    return occurrences


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_ini.txt'
        with open(filename) as file:
            sequence = file.read().strip()
            occurrences = nucleotide_occurrences(sequence)
            print(occurrences['A'], occurrences['C'], occurrences['G'], occurrences['T'])
