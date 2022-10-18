# Joseph Brehm       10.13.22
# Lab Week 8         Assignment 2


def sorter():
    a = int(input("Input an integer for A: "))
    b = int(input("Input an integer for B: "))
    c = int(input("Input an integer for C: "))
    unsorted = [a, b, c]
    for i in range(len(unsorted)):
        for j in range(i + 1, len(unsorted)):
            if unsorted[i] > unsorted[j]:
                unsorted[i], unsorted[j] = unsorted[j], unsorted[i]
    return unsorted


def main():
    print(sorter())


if __name__ == '__main__':
    main()
