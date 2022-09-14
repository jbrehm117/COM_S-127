# Joseph Brehm       #9.7.22

# > demo
x = int(input("Input an integer: "))
y = int(input("Input an integer: "))
print("It is {2} that the integer {0} is greater than {1}".format(x, y, x > y))
print()


# Conditional Logic
val1 = 3
val2 = 7
if val1 > val2:
    print("val1 is greater")
else:
    print("val2 is greater")
print()


# Comparison Operators with Conditional Logic
x = int(input("Input an integer: "))
y = int(input("Input an integer: "))
if x == y:
    print("{0} is equal to {1}".format(x, y))
elif x > y:
    print("{0} is greater than {1}".format(x, y))
elif x < y:
    print("{0} is less than {1}".format(x, y))
else:
    print("lmao, I didn't wanna do the rest of the comparision operators so uhmm lmao")
print()
