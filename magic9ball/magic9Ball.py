# Joseph Brehm            9.13.22
# Assignment 2

print("Welcome to the Magic 9 Ball...")
print()

print("By: Joseph Brehm")
print("[COM S 127 D]")
print()

print("What would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")
print()

# Calculator
if choice == "c":
    operator = input("Choose an operator: [+], [-], [*], [/], [%], [**]")
    leftSide = int(
        input("Input an integer for the left side of the equation: "))
    rightSide = int(
        input("Input an integer for the right side of the equation: "))
    if operator == "+":
        print(leftSide + rightSide)
    elif operator == "-":
        print(leftSide - rightSide)
    elif operator == "*":
        print(leftSide * rightSide)
    elif operator == "/":
        if (rightSide == 0):
            print("ERROR: Right side of equation cannot = 0")
        else:
            print(leftSide / rightSide)
    elif operator == "%":
        if (rightSide == 0):
            print("ERROR: Right side of equation cannot = 0")
        else:
            print(leftSide % rightSide)
    elif operator == "**":
        print(leftSide ** rightSide)
    else:
        print("ERROR: You must enter either \"+\", \"-\", \"*\", \"/\", \"%\", or \"**\"")
elif choice == "p":
    print("p")
elif choice == "q":
    print("q")
else:
    print("ERROR: I did not understand your input... Please try again...")

# Prediction


# 'p' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'p' section, take in input from the user asking them "What is your question?: " or something similar (use your imagination)
# TODO: print a string stating print("As far as '", question, "' is concerned, I predict: ") or something similar (use your imagination)
# TODO: use then length of the question string the user input to generate a 'prediction selection value' within the following range:
# from 0 through (<the number of predictions>-1)
# HINT: there is a built in function to find the range of a string
# HINT: one of the operators used in the 'c' section of the script will return a value within the range 'from 0 through (<the number of predictions>-1)'
# when applied to <the length of the question string> on the left side of the operator, and <the number of predictions> on the right side
# TODO: write at least ten (10) 'predictions' and use conditional logic to select which one to print after the 'prediction selection value'
# from above is calculated (use your imagination)
# TODO: if the computation to produce a 'prediction selection value' creates a value outside the range 'from 0 through (<the number of predictions>-1)'
# then have the script print an error message to that effect. NOTE: If the calculation of a 'prediction selection value' is done properly, this
# error message should **never** be seen.
# HINT: if you write ten (10) 'predictions,' then <the number of predictions> will be 10. This means that the range of the 'prediction
# selection value' will be between 0 and 9. After selecting a value between 0 and 9 by way of the length of the 'question' string, one of
# the operators from the 'c' option, and <the number of predictions>, you will print out a 'prediction' corresponding to this value.
# ---------------------------------------------------------------------------------------------------------------------------------------------

# 'q' option tasks ----------------------------------------------------------------------------------------------------------------------------
# TODO: inside the 'q' option, print out a message stating "Maybe next time...", or "Goodbye!", or something else to that effect
# (use your imagination)
# ---------------------------------------------------------------------------------------------------------------------------------------------
