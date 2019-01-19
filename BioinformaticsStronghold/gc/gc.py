#!/usr/bin/python3

import sys


class Dna:
    def __init__(self, identifier, literal):
        self.identifier = identifier
        self.literal = literal

    def gc_rate(self):
        cg_literal = self.literal.replace('T', '').replace('A', '')
        rate = len(cg_literal)/len(self.literal)
        return round(rate * 100, 6)


def highest_gc_rate(sequences):
    sequences.sort(key=lambda element: element.gc_rate(), reverse=True)
    best_result = sequences[0]
    return best_result.identifier, best_result.gc_rate()


def process_input(file):
    literal = file.read()
    records = list(filter(None, literal.split('>')))
    processed_records = []
    for record in records:
        lines = record.split()
        identifier = lines.pop(0)
        dna = ''.join(lines)
        processed_records.append(Dna(identifier, dna))
    return processed_records


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1], 'r') as file:
            sequences = process_input(file)
            result = highest_gc_rate(sequences)
            print(result[0])
            print(result[1])
