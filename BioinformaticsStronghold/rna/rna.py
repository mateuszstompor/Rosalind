import sys


def rna(dna):
    return dna.replace('T', 'U')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1], 'r') as file:
            print(rna(file.read()))
