str_example = input("Input a string: ")
print(type(str_example))  # type displays the type
int_example = int(input("Input an integer: "))
print(type(int_example))
float_example = float(input("input a float: "))
print(type(float_example))
bool_example = bool(int(input("Input a bool:")))
# bools read 0 as false and everything else as true
print(type(bool_example))
print(bool_example)


name = input("enter a name")
salary = input("Enter a salary: ")
company = input("Enter a company: ")
print()
print("Printing employee details")
print("-------------------------")
print("Name", "Salary", "Company")
print(name, salary, company)

# Program to check input type
number = input("Enter a number: ")
name = input("Enter a name: ")
print()
print("The type of number is", type(int(number)))
print("The type of name is", type(name))

# Calculator that only does addition
first_number = int(input("Enter a number: "))
second_number = int(input("Enter a second number:"))
sum = first_number + second_number
print("The sum is:", sum, "The type of sum is:", type(sum))

float_number = float(input("Enter a float number: "))
print("The float number is:", float_number)
print("The type of float_number is:", type(float_number))
