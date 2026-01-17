# arithmetic operators
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)

# Comparison Operators
# In Python, Comparison (or Relational) operators compares values. It either returns True or False according to the condition.

a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)



# Logical Operators
# Python Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.
# The precedence of Logical Operators in Python is as follows:
#     Logical not
#     logical and
#     logical or

a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Bitwise Operators
# Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.
# Bitwise Operators in Python are as follows:
#     Bitwise NOT
#     Bitwise Shift
#     Bitwise AND
#     Bitwise XOR
#     Bitwise OR

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


# Identity Operators
# In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 
#     is          True if the operands are identical 
#     is not      True if the operands are not identical 

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership Operators
# In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.
#     in            True if value is found in the sequence
#     not in        True if value is not found in the sequence

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
    

# Ternary operator
 
a, b = 10, 20
min = a if a < b else b

print(min)

# Operator Precedence
# This is used in an expression with more than one operator with different precedence to determine which operation to perform first.

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")
    
    
# Operator Associativity
# If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. It can either be Left to Right or from Right to Left.

print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)