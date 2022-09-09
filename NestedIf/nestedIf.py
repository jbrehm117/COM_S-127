# Joseph Brehm       9.9.22
# Nested If demo
import math


x = float(input("Input a float: "))
f = False
if x > 0.0:
    f = True
    if x < 20.0:
        x = x+5
        print("X was incremented")
        print("New value is {0}".format(x))
else:
    x = x-5
    print("X was decremented")
    print("New value is {0}".format(x))
print(x, f)
