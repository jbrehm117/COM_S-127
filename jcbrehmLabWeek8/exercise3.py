# Joseph Brehm       10.13.22
# Lab Week 8         Assignment 3


def swap(a, b):
    a, b = b, a
    return a, b


x = int(input("Enter an Integer: "))
y = int(input("Enter an Integer: "))
x, y = swap(x, y)
print(x, y)
