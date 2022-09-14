# Joseph Brehm       #9.8.22
# Lab Week 3 - exercise 5
class1 = input("Class 1: ")
grade1 = int(input("Grade: "))
print()
class2 = input("Class 2: ")
grade2 = int(input("Grade: "))
print()
class3 = input("Class 3: ")
grade3 = int(input("Grade: "))
print()
class4 = input("Class 4: ")
grade4 = int(input("Grade: "))
print()

avg_grade = [grade1, grade2, grade3, grade4]
print("The average grade of {0}, {1}, {2}, and {3} is {4}".format(
    class1, class2, class3, class4, round((sum(avg_grade)/len(avg_grade)), 2)))
