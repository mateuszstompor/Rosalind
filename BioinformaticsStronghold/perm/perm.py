import sys


def swap(index_a, index_b, sequence):
    sequence[index_a], sequence[index_b] = sequence[index_b], sequence[index_a]


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def permutate(sequence, pivot):
    if pivot == len(sequence) - 1:
        return [sequence]
    results = []
    for i in range(pivot, len(sequence)):
        copy = sequence.copy()
        swap(pivot, i, copy)
        results += permutate(copy, pivot + 1)
    return results


def permutations(sequence):
    permutated_sequences = permutate(sequence, 0)
    return permutated_sequences


def possible_permutations(number):
    amount = factorial(number)
    numbers = [i + 1 for i in range(number)]
    return amount, permutations(numbers)


def display_result(number, permutations):
    print(amount)
    for permutation in permutations:
        for number in permutation:
            print(number, end=' ')
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        try:
            with open(sys.argv[1], 'r') as file:
                number = int(file.read())
                amount, permutations = possible_permutations(number)
                display_result(amount, permutations)
        except IOError:
            print("Error while trying to open the file")
