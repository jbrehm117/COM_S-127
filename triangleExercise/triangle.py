# Joseph Brehm       9.9.22
# Triangle Checker
a = float(input("Input a float(A): "))
b = float(input("Input a float(B): "))
c = float(input("Input a float(C): "))
if ((a+b) > c or (a+c) < b or (b+c) > a):
    if (a == b == c):
        print("The triangle with sides {0}, {1}, {2}, is {3}".format(
            a, b, c, "Equilateral"))
    elif (a == b or b == c or a == c):
        print("The triangle with sides {0}, {1}, {2}, is {3}".format(
            a, b, c, "Isosceles"))
    elif (a != b or a != c or c != a):
        print("The triangle with sides {0}, {1}, {2}, is {3}".format(
            a, b, c, "Scalene"))
else:
    print("The triangle must have sides greater than 0")
