# Joseph Brehm       #9.8.22
# Lab Week 3 - exercise 3
import math

a = int(input("Input an integer (a): "))
b = int(input("input an integer (c): "))
c = int(input("Input an integer (c): "))
if (c == 0 or a == c):
    print("C cannot = 0 and A cannot = C")
    # could also use the elif condition to do this, but since we haven't learned it in class I didn't
else:
    print(a+b+c)
    print(a % c)
    print(a*b/c)
    d = c - a
    print(round(c/d, 2))
    numList = [a, b, c]
    avg = sum(numList)/len(numList)
    print("The average is:", round(avg, 2))
