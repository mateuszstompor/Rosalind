import sys


def hypotenuse(side_a, side_b):
    return side_a ** 2 + side_b ** 2


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as file:
            numbers = file.read().split()
            print(hypotenuse(int(numbers[0]), int(numbers[1])))
