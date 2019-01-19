import sys


def even_number_lines(file):
    return [line for count, line in enumerate(file, start=0) if count % 2 == 1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as input_file:
            for line in even_number_lines(input_file):
                print(line, end='')
