# Joseph Brehm       9.15.22
# Lab Week 4 - Exercise 4
import math
m1 = float(input("Input a float for slope 1: "))
m2 = float(input("Input a float for slope 2: "))
if m1 == m2:
    print(
        "The lines with the slopes of {0} and {1} are parallel to each other".format(m1, m2))
elif (1 + m1 * m2) == 0:
    print(
        "The lines with the slopes of {0} and {1} are perpendicular to each other".format(m1, m2))
else:
    angle = math.atan((m1 - m2) / (1 + m1 * m2))
    print(
        "The angle between the lines with the slopes {0} and {1} is {2}".format(m1, m2, angle))
