import sys


def insertion_sort(numbers, size):
    swaps = 0
    for i in range(2, min(len(numbers), size)):
        k = i
        while k > 0 and numbers[k] < numbers[k-1]:
            temporary = numbers[k]
            numbers[k] = numbers[k - 1]
            numbers[k - 1] = temporary
            swaps += 1
            k -= 1
    return swaps


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as file:
            amount = int(file.readline())
            numbers = [int(number) for number in file.readline().split()]
            print(insertion_sort(numbers, amount))

