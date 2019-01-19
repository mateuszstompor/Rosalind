import sys
from enum import Enum


class Nucleotide(Enum):
    ADENINE = 'A'
    CYTOSINE = 'C'
    GUANINE = 'G'
    THYMINE = 'T'

    def complement(self):
        if self.value == 'A':
            return Nucleotide('T')
        elif self.value == 'T':
            return Nucleotide('A')
        elif self.value == 'C':
            return Nucleotide('G')
        else:
            return Nucleotide('C')

    def __str__(self):
        return str(self.value)


class Amino(Enum):
    ALANINE = 'A'
    ARGININE = 'R'
    ASPARAGINE = 'N'
    ASPARTIC_ACID = 'D'
    CYSTEINE = 'C'
    GLUTAMIC_ACID = 'E'
    GLUTAMINE = 'Q'
    GLYCINE = 'G'
    HISTIDINE = 'H'
    ISOLEUCINE = 'I'
    LEUCINE = 'L'
    LYSINE = 'K'
    METHIONINE = 'M'
    PHENYLALANINE = 'F'
    PROLINE = 'P'
    SERINE = 'S'
    THREONINE = 'T'
    TRYPTOPHAN = 'W'
    TYROSINE = 'Y'
    VALINE = 'V'

    def __str__(self):
        return str(self.value)


class Protein:
    def __init__(self, aminos):
        self.aminos = aminos

    def __str__(self):
        return ''.join([str(amino) for amino in self.aminos])


class Dna:
    class Codon:
        class InvalidLength(Exception):
            pass

        def __init__(self, values):
            if len(values) != 3:
                raise Dna.Codon.InvalidLength('Codon must have 3 nucleotides')
            self.values = values

        def is_start(self):
            return str(self) == 'ATG'

        def is_end(self):
            raw_value = str(self)
            return raw_value == 'TAG' or raw_value == 'TAA' or raw_value == 'TGA'

        def __str__(self):
            return ''.join([str(nucleotide) for nucleotide in self.values])

        def __getitem__(self, index):
            return self.values[index]

        def amino(self):
            map = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
                   'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
                   'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
                   'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
                   'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
                   'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
                   'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
                   'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*', 'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'}
            value = map[str(self)]
            if value == '*':
                return None
            else:
                return Amino(value)

    def __init__(self, v=[]):
        if isinstance(v, str):
            self.nucleotides = [Nucleotide(letter) for letter in v]
        else:
            self.nucleotides = v

    def codon(self, index):
        start_index = index * 3
        return Dna.Codon(self.nucleotides[start_index: start_index + 3])

    def reversed(self):
        return Dna(self.nucleotides[::-1])

    def complement(self):
        return Dna(list(map(lambda x: x.complement(), self.nucleotides)))

    def cut_before_nearest_stop_codon(self):
        index = None
        for i in range(0, len(self.nucleotides), 3):
            try:
                nucleotides = self.nucleotides[i:i + 3]
                if len(nucleotides) != 3:
                    break
                codon = Dna.Codon(nucleotides)
                if codon.is_end():
                    index = i
                    break
            except IndexError:
                break
        if index:
            dna = Dna()
            dna.nucleotides = self.nucleotides[:index]
            return dna

    def protein(self):
        aminos = []
        for i in range(0, len(self.nucleotides), 3):
            amino = Dna.Codon(self.nucleotides[i:i+3]).amino()
            if amino is not None:
                aminos.append(amino)
            else:
                break
        return Protein(aminos)

    def open_reading_frames(self):
        result = []
        for i in range(0, len(self.nucleotides) - 2):
            codon = Dna.Codon(self.nucleotides[i:i+3])
            if codon.is_start():
                dna = Dna()
                dna.nucleotides = self.nucleotides[i:]
                cut = dna.cut_before_nearest_stop_codon()
                if cut:
                    result.append(cut)
        return result

    def __str__(self):
        return ''.join(str(nucleotide) for nucleotide in self.nucleotides)


class Record:
    def __init__(self, identifier, literal):
        self.identifier = identifier
        self.dna = Dna(literal)

    def error_rate(self, precision):
        cg_literal = self.literal.replace('T', '').replace('A', '')
        rate = len(cg_literal)/len(self.literal)
        return round(rate * 100, precision)


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


def process_input(file):
    literal = file.read()
    processed_records = Parser.parse(literal)
    for record in processed_records:
        result = set()
        for frame in record.dna.open_reading_frames():
            result.add(str(frame.protein()))
        for frame in record.dna.reversed().complement().open_reading_frames():
            result.add(str(frame.protein()))
        for value in result:
            print(value)


if len(sys.argv) != 2:
    sys.stderr.write('Wrong invocation! Pass a path to the input file as an argument')
    sys.exit(1)
else:
    try:
        with open(sys.argv[1], 'r') as file:
            process_input(file)
    except IOError:
        sys.stderr.write('IO Error')
        sys.exit(1)
