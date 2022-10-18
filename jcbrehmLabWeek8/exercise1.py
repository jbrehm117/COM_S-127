# Joseph Brehm       10.13.22
# Lab Week 8         Assignment 1


def main():
    a = int(input("Input an integer for A: "))
    b = int(input("Input an integer for B: "))
    product = 0
    for i in range(1, b+1):
        product = product+a
    print(product)


if __name__ == "__main__":
    main()
