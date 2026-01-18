def fun():
    return "Hello"
    

if __name__ == "__main__":
  print("This is inside a function "+ fun())


# Types of Function Arguments
# Python supports various types of arguments that can be passed at the time of the function call. In Python, we have the following function argument types in Python, Let's explore them one by one.
# 1. Default Arguments
# A default argument is a parameter that assumes a default value if a value is not provided in the function call for that argument.

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
myFun(10)

# Output

# x:  10
# y:  50

# 2. Keyword Arguments
# In keyword arguments, values are passed by explicitly specifying the parameter names, so the order doesn’t matter.

def student(fname, lname):
    print(fname, lname)
  
student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')


# Output
# Geeks Practice
# Geeks Practice
 
# 3. Positional Arguments
# In positional arguments, values are assigned to parameters based on their order in the function call.

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
print("Case-1:")
nameAge("Suraj", 27)
print("\nCase-2:")
nameAge(27, "Suraj")


# Output

# Case-1:
# Hi, I am Suraj
# My age is  27

# Case-2:
# Hi, I am 27
# My age is  Suraj



# 4. Arbitrary Arguments

# In Python Arbitrary Keyword Arguments, *args and **kwargs can pass a variable number of arguments to a function using special symbols. There are two special symbols:
#     *args in Python (Non-Keyword Arguments)
#     **kwargs in Python (Keyword Arguments)

# This code separately shows non-keyword (*args) and keyword (**kwargs) arguments in the same function

def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Function call with both types of arguments
myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


def demo(*args, **kwargs):
  print(args)
  print(kwargs)
  print(type(args))
  print(type(kwargs))

demo('Good',1,2,x=2,y=4)



# Function within Functions
# A function defined inside another function is called an inner function (or nested function). 
# It can access variables from the enclosing function’s scope and is often used to keep logic protected and organized.

def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()

# Anonymous Functions

# In Python, an anonymous function means that a function is without a name. 
# As we already know the def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.
def cube(x): return x*x*x   # without lambda
cube_l = lambda x : x*x*x  # with lambda

print(cube(7))
print(cube_l(7))

# Return Statement in Function
# The return statement ends a function and sends a value back to the caller. It can return any data type, 
# multiple values (packed into a tuple), or None if no value is given.

# Syntax:
#     return [expression]
# Parameters: return ends the function, [expression] is the optional value to return (defaults to None).

def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))


# Pass by Reference and Pass by Value

# In Python, variables are references to objects. When we pass them to a function, 
# the behavior depends on whether the object is mutable (like lists, dictionaries) or immutable (like integers, strings, tuples).

#     Mutable objects: Changes inside the function affect the original object.
#     Immutable objects: The original value remains unchanged.

# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified