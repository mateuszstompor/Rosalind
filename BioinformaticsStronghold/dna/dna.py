import sys


def count_nucleotides(sequence):
    a, c, g, t = 0, 0, 0, 0
    for character in sequence:
        if character == 'A':
            a += 1
        elif character == 'C':
            c += 1
        elif character == 'G':
            g += 1
        else:
            t += 1
    return a, c, g, t


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as file:
            literal = file.readline().strip()
            nucleotides = count_nucleotides(literal)
            print(nucleotides[0], nucleotides[1], nucleotides[2], nucleotides[3])
