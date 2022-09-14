# Joseph Brehm       #9.8.22
# Lab Week 3 - exercise 1
import math
from math import sqrt


a = int(input("Input an integer: "))
b = int(input("Input an integer: "))
c = int(input("Input an integer: "))
aPlusBPlusC = a+b+c
s = aPlusBPlusC/2
x = s*((s-a)*(s-b)*(s-c))
print(sqrt(x))
