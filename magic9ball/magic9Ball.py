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
if choice == "p":
    question = input("What is your question?: ")
    selection_value = len(question) % 10
    print("As far as", question,
          "is concerned, I predict: ", end="")
    if selection_value == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        if selection_value == 0:
            print("Yes, clearly.")
        elif selection_value == 1:
            print("No, I don't think so.")
        elif selection_value == 2:
            print("thats an interesting question.")
        elif selection_value == 3:
            print("Let me think some more.")
        elif selection_value == 4:
            print("Whats that again?")
        elif selection_value == 5:
            print("certainly")
        elif selection_value == 6:
            print("No, thats really not a good idea.")
        elif selection_value == 7:
            print("Try another question.")
        elif selection_value == 8:
            print("Dumb question, try again.")
        elif selection_value == 9:
            print("DUHHHHHHH, NO.")
        else:
            print()
    else:
        print("ERROR: selection_value cannot be above 9")

# Quit
if choice == "q":
    print("Oh darn...see ya later I guess :)")
