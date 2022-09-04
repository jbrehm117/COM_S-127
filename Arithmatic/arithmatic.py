import math

# exopnent operator demo **
val1 = int(input("input an integer: "))
val2 = int(input("input an integer: "))
print(val1**val2)
print()


# modulus operator demo %
val1 = int(input("input an integer: "))
val2 = int(input("input an integer: "))
print(val1 % val2)
print()

# floor division demo //
val1 = int(input("input an integer: "))
val2 = int(input("input an integer: "))
print(val1 // val2)
print()

# pow function demo
val1 = int(input("input an integer: "))
val2 = int(input("input an integer: "))
print(pow(val1, val2))
print()

# format string demo
num = int(input("Enter an integer: "))
print("The square of {0} is {1}".format(num, pow(num, 2)))

# min() function demo
vals = [1, 2, 3, 4, 5]
print("The min of {0} is {1}".format(vals, min(vals)))
print()

# max() function demo
max_val = [1, 2, 3, 4, 5]
print("The max of {0}, is {1}".format(max_val, max(max_val)))
print()

# round() function demo
value = float(input("enter a float: "))
print("The rounded value of {0} is {1}".format(value, round(value)))
print()

# sum() demo
sum_values = [1, 3]
print("The sum of {0} is {1}".format(sum_values, sum(sum_values)))
print()

# Len() function demo
values = [123, 45645, 3409645, 434343]
print("The lenght of {0} is {1}".format(values, len(values)))
string_values = ("there are a lot of letters in here")
print("the length of {0} is {1}".format(string_values, len(string_values)))
print()
