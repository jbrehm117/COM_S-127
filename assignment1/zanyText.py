# Joseph Brehm             8.29.22
# Assignment 1

from tkinter import Variable

print("Zany Text!")
print()

print("By: Joseph Brehm")
print("COM S 127 Section D")
print()

"""
# Example 'Zany Text' - gathering input
print("Once upon a time, there was a <noun>.")
noun1 = input("noun: ")
print("It was a <adjective>, <adjective>, <adjective>", noun1)
adjective1 = input("adjective: ")
adjective2 = input("adjective: ")
adjective3 = input("adjective: ")
print("And, one day, it <past tense action> all over the <noun>!")
verb1 = input("past tense action: ")
noun2 = input("noun: ")

# Example 'Zany Text' - printing the final string
print("Once upon a time, there was a",
      noun1,
      ". It was a",
      adjective1, ",",
      adjective2, ",",
      adjective3,
      noun1,
      ". And, one day it",
      verb1,
      "all over the",
      noun2, "!")
"""

# TODO: Make three more 'Zany Texts' like the one above, and have all four run/ print out in order.
# There should be at least four (4) 'Zany Texts' in a completed assignment.

# Zany Text 1
print("My dog's name is <dogName>")
dogName = input("dog's name?")
print("She is <color> and likes to <verb>")
color = input("color?")
verb_1 = input("verb?")
print("One day <dog_name> decided to track mud all through the house,\
his/her owners were very <descriptive word>")
descriptive_word = input("descriptive word?")
print("They decided to <verb> the dog")
verb_2 = input("verb?")

print("My dog's name is", dogName, end=". ")
print("She is", color, "and likes to", verb_1, end=". ")
print("One day", dogName, "decided to track mud all through the house,\
his/her owners were very", descriptive_word, end=". ")
print("They decided to", verb_2, "the dog.")
print()

# Zany Text 2
print("Today is a <adjective> day")
adjective = input("adjective?")
print("There are <thing(s)> falling from the sky and <verbing(ing) our heads!!")
thing = input("Thing(s)?")
verb_3 = input("Verb(ing)?")
print("Everyone needs to get inside the <descriptive word> <place>")
descriptive_word = input("Descriptive word?")
place = input("place?")
print("Now we are all safe inside of the <place>")
print()

print("Today is a", adjective, "day. There are", thing, "falling from the sky and",
      verb_3, "our heads!! Everyone needs to get inside the", descriptive_word,
      place, "." + "Now we are all safe inside of the", place)
print()

# Zany Text 3
print("Sometimes my <noun> goes to <place>.")
noun = input("noun?")
place = input("place?")
print("At <place>, a lot of people <action_verb>")
action_verb = input("action verb?")
print("When the people are done <action_verb(ing)>, they go home and <verb>.")
verb = input("verb?")
print()

print("Sometimes my", noun, "goes to", place, "." + "At", place, "a lot of people",
      action_verb, "." + "When the people are done", action_verb, end="ing")
print(", they go home and", verb)
print()
