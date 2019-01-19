import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as file:
            literal = file.readline()
            ranges = [int(number) for number in file.readline().split()]
            print(literal[ranges[0]: ranges[1] + 1], literal[ranges[2]: ranges[3] + 1])
