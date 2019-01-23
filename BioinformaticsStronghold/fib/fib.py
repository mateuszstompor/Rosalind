import sys


def rabbits(month, offspring_monthly):
    if month <= 0:
        return 0
    elif month == 1:
        return 1
    else:
        return rabbits(month-1, offspring_monthly) + offspring_monthly * rabbits(month-2, offspring_monthly)


if __name__ == "__main__":
    print("There is possibility of passing a path to file containing data as a first argument")
    if len(sys.argv) > 2:
        print('Wrong Invocation! Pass a path to file or do not pass anything')
    else:
        filename = sys.argv[1] if len(sys.argv) == 2 else 'rosalind_fib.txt'
        try:
            with open(filename) as file:
                months, offspring_monthly = [int(x) for x in file.read().split()]
                print(rabbits(months, offspring_monthly))
        except IOError:
            print('Error while opening the file')

