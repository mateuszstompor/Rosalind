import sys


def sum_even_numbers(start_index, end_index):
    total = 0
    for i in range(start_index, end_index):
        if i % 2 == 1:
            total += i
    return total


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as file:
            range_start, range_end = [int(number) for number in file.readline().split()]
            print(sum_even_numbers(range_start, range_end + 1))

