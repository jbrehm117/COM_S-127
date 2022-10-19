# Joseph Brehm       10.18.22
# Lab Week 9         Exercise 1

import random

x = int(input("Input an integer for A: "))
y = int(input("input an integer for B: "))


def main(x, y):
    list = []
    for i in range(x):
        randNumber = random.randint(x, x+y)
        list.append(randNumber)
    print(list)
    multiples = []
    for i in list:
        if i % y == 0:
            multiples.append(i)
    return multiples


returnedValues = main(x, y)
print(returnedValues)
