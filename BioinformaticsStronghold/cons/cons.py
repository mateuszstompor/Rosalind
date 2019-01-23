import numpy as np
import sys


class Dna:
    def __init__(self, sequence=[]):
        self.sequence = sequence

    def __str__(self):
        return self.sequence

    def __getitem__(self, item):
        return self.sequence[item]

    def __len__(self):
        return len(self.sequence)

class Record:
    def __init__(self, identifier, literal):
        self.identifier = identifier
        self.dna = Dna(literal)

    def __str__(self):
        return self.identifier + " " + str(self.dna)


class Parser:
    @staticmethod
    def parse(literal):
        raw_records = list(filter(None, literal.split('>')))
        processed_records = []
        for record in raw_records:
            lines = record.split('\n')
            identifier = lines.pop(0)
            dna = ''.join(lines)
            processed_records.append(Record(identifier, dna))
        return processed_records


def consensus_matrix(records):
    rows = 4
    columns = len(records[0].dna)
    result = np.zeros((rows, columns))
    mapping = ['A', 'C', 'G', 'T']
    for j in range(rows):
        for i in range(columns):
            result[j][i] = sum(1 if sequence.dna[i] == mapping[j] else 0 for sequence in records)
    return result


def consensus(records):
    m = consensus_matrix(records)
    indices = [max(range(len(m[:, i])), key=m[:, i].__getitem__) for i in range(m.shape[1])]
    sequence = list(map(lambda i: ['A', 'C', 'G', 'T'][i], indices))
    return ''.join(sequence), m


def print_consensus(records):
    c = consensus(records)
    print()
    print(c[0])
    for i in range(c[1].shape[0]):
        print(['A', 'C', 'G', 'T'][i] + ':', end=' ')
        for number in c[1][i, :]:
            print(int(number), end=' ')
        print()


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_cons.txt'
        try:
            with open(filename) as file:
                print_consensus(Parser.parse(file.read()))
        except IOError:
            print('Error while opening the file')
