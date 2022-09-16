# Joseph Brehm       9.15.22
# Lab Week 4 - Exercise 1

sideLength1 = int(input("Input height: "))
sideLength2 = int(input("Input length: "))
perimeter = (2*sideLength1 + 2*sideLength2)
if sideLength1 == sideLength2:
    print(
        "The rectangle is a square and its perimeter is {0}".format(perimeter))
else:
    print(
        "The rectangle is not a square its perimeter is {0}".format(perimeter))
