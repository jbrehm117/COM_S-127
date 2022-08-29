# Joseph Brehm        8.26.22
# Assignment #1

"""
This is a multi-line comment
It is really neat
"""

'''
This is also a multi-line comment
It is also really neat
'''


print('hello world')
print('Hello, world!', end="")
print('Hello, world!', end="abc")
# prints on the same line because the line was
# ended with nothing instead of the implied "new line character"

print('Hello, world!', end="\n")
print('Hello, world!')
# \n is a 'new line character'

print('This is a \nnew line')
print('This is a \ttab character')
# puts an indent in the code (tab key)

print('This is a \\ slash character')

print('This is a double quote \" ')
print('This is a single quote \' ')
# slash basically allows the code to print exactly what you type

name = input("What is your name?:")
print("Hello" + " " + name)
