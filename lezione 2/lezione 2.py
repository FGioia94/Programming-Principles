import this # List of python rules
# python documentation https://docs.python.org/3/
# Useful books: automate the boring stuff with python, python crash course

# sep: separator kwarg
"""
end: specifies the default end string that 
gets attached after printing, default is \n
"""
print("Hello", "World", sep = "%", end = "\n")
# \t adds 4 spaces (tab)
print("Hello", "World", sep = "%", end = "\t")

# Syntax errors: before running the code
# Runtime errors: during the code run

"""
This is a multi line comment
it is actually interpreted as a string
This also keeps the information about formatting 
like end lines
"""

# input() Requests an information to the user. 
# Once we hit enter, the function returns the value that we typed

# We can concatenate the print and the input functions like this 
print(input()) #"This is called "nested functions", usually not very elegant

# We can pass an argument to input, this argument gets printed before asking
input("come stai?")

# Also, we can use a variable instead
name = input()
print(name)

# The memory address remains THE SAME when reassicl
name = "b"
print(name) #output "b", memory address = same


'''
shortcuts
ctrl + ' : hides the terminal
shift + alt + up or down: copying a selected line
ctrl + d to select multiple parts with the same words'''
#
