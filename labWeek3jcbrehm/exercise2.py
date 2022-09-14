# Joseph Brehm       #9.8.22
# Lab Week 3 - exercise 2
import math
from math import pi

r = int(input("Input an integer: "))
a = 4*pi*r**2
print("The volume of a sphere with the radius {0} is {1} and its area is {2}".format(
    r, round(a*r / 3, 2), round(a, 2)))
