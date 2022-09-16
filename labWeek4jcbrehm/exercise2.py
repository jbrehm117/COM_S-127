# Joseph Brehm       9.15.22
# Lab Week 4 - Exercise 2

a = float(input("Input a float (a): "))
b = float(input("Input a float (b): "))
c = float(input("Input a float (c): "))
x = float(input("Input a float (x): "))
y = float(input("Input a float (y): "))
parabola = a * x ** 2 + b * x + c
if parabola == y:
    print("The point ({0},{1}) lies on the parabola y = {2}".format(
        x, y, "1 * x ** 2 + 0 * x + 0"))
else:
    print("The point ({0},{1}) does not lie on the parabola y = {2}".format(
        x, y, "1 * x ** 2 + 0 * x + 0"))
