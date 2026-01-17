#  creating and assigning variables
x = 5
name = "Samantha"  
print(x)
print(name)



# To use variables effectively, we must follow Python’s naming rules:

#     Variable names can only contain letters, digits and underscores (_).
#     A variable name cannot start with a digit.
#     Variable names are case-sensitive like myVar and myvar are different.
#     Avoid using Python keywords like if, else, for as variable names.


# VALID
age = 21
_colour = "lilac"
total_score = 90

# INVALID
# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen


# Dynamic Typing: Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
x = 10
x = "Now a string"

# Assigning Same Value: Python allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
a = b = c = 100
print(a, b, c)



# Type Casting a Variable

# Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others. Basic casting functions are:

#     int(): Converts compatible values to an integer.
#     float(): Transforms values into floating-point numbers.
#     str(): Converts any data type into a string.

s = "10"  
n = int(s)
cnt = 5
f = float(cnt) 
age = 25
s2 = str(age)  
print(n)  
print(f)  
print(s2)