import sys


def complement(dna):
    mapping = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    return ''.join([mapping[letter] for letter in dna])[::-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1], 'r') as file:
            print(complement(file.read().strip()))
