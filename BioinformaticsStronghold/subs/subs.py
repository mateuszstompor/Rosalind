import sys


def motif_occurrence(dna, motif):
    result = []
    for i in range(0, len(dna)):
        stripped = dna[i:i+len(motif)]
        index = stripped.find(motif)
        if index >= 0:
            result.append(index + i + 1)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1], 'r') as file:
            dna = file.readline().strip()
            motif = file.readline().strip()
            print(*motif_occurrence(dna, motif))
