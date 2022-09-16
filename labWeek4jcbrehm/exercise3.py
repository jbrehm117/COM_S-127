# Joseph Brehm       9.15.22
# Lab Week 4 - Exercise 3
y1 = float(input("Input a float (y1): "))
y2 = float(input("Input a float (y2): "))
x1 = float(input("Input a float (x1): "))
x2 = float(input("Input a float (x2): "))
if (x2 - x1 == 0) or ((x2 - x1 == 0) and (y2 - y1 == 0)):
    print("The slope of line described by the points ({0}, {1})({2}, {3}) is undefined".format(
        x1, y1, x2, y2))
else:
    m = (y2 - y1) / (x2 - x1)
    if m == 0:
        print("The slope of line described by the points ({0}, {1})({2}, {3}) is horizontal".format(
            x1, y1, x2, y2))
    else:
        print("The slope of line described by the points ({0}, {1})({2}, {3}) is {4}".format(
            x1, y1, x2, y2, m))
