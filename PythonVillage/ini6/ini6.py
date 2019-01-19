import sys


def count_word_occurence(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invoke the program passing a path to a file as an argument")
    else:
        with open(sys.argv[1]) as input_file:
            words = input_file.read().split()
            count = count_word_occurence(words)
            for key, value in count.items():
                print(key, value)
